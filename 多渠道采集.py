#!/usr/bin/env python3
"""
Z.Talk 智言 - 多渠道话术自动采集系统
每日自动从小红书、知乎、微博、抖音等平台采集高情商话术
"""
import json
import os
import re
import hashlib
import time
import random
from datetime import datetime
from pathlib import Path

try:
    import requests
    from bs4 import BeautifulSoup
except ImportError:
    print("需要安装依赖: pip install requests beautifulsoup4")
    exit(1)

# ========== 配置 ==========
DB_PATH = Path(os.path.expanduser("~/话搭子话术库/话术数据库.json"))
LOG_PATH = Path(os.path.expanduser("~/话搭子话术库/采集日志.log"))
STICKER_DIR = Path(os.path.expanduser("~/话搭子表情包/采集"))
REPORT_PATH = Path(os.path.expanduser("~/话搭子话术库/采集报告.md"))

# 8大场景关键词映射
SCENARIO_KEYWORDS = {
    "破冰开场": ["破冰话术", "初次聊天开场白", "搭讪开场", "怎么开口聊天", "第一次聊天说什么", "认识新朋友开场"],
    "暧昧升温": ["暧昧聊天话术", "撩人情话", "暧昧怎么说", "升温话术", "推拉话术", "聊天暧昧技巧"],
    "日常聊天": ["日常聊天话术", "早安晚安话术", "聊天话题", "日常关心的话", "怎么找话题聊天"],
    "关心体贴": ["关心人的话", "暖心的话", "安慰人的话术", "体贴的话怎么说", "高情商关心"],
    "吵架和好": ["吵架后怎么和好", "道歉话术", "哄人的话", "吵架后说什么", "高情商道歉"],
    "拒绝": ["怎么拒绝别人", "高情商拒绝", "委婉拒绝的话", "拒绝表白话术", "不伤人的拒绝"],
    "表白": ["表白话术", "怎么表白", "高情商表白", "浪漫表白句子", "表白文案"],
    "维系关系": ["维系感情的话", "恋爱保鲜话术", "感情升温", "长期关系经营", "高情商维系关系"],
}

# 搜索渠道配置
CHANNELS = [
    {
        "name": "小红书",
        "search_url": "https://www.xiaohongshu.com/search_result",
        "keywords_extra": ["高情商话术", "聊天话术大全", "恋爱话术", "撩人句子"],
    },
    {
        "name": "知乎",
        "search_url": "https://www.zhihu.com/search",
        "keywords_extra": ["高情商回复", "聊天技巧话术", "恋爱聊天话术"],
    },
    {
        "name": "微博",
        "search_url": "https://s.weibo.com/weibo",
        "keywords_extra": ["高情商话术", "撩人情话", "恋爱话术"],
    },
    {
        "name": "抖音",
        "search_url": "https://www.douyin.com/search",
        "keywords_extra": ["高情商聊天", "话术教学", "恋爱话术"],
    },
    {
        "name": "百度",
        "search_url": "https://www.baidu.com/s",
        "keywords_extra": ["高情商话术合集", "聊天话术100句", "恋爱话术大全"],
    },
]

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
}


def load_database():
    """加载现有话术数据库"""
    if DB_PATH.exists():
        with open(DB_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    return []


def save_database(data):
    """保存话术数据库"""
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(DB_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def content_hash(text):
    """生成内容指纹用于去重"""
    cleaned = re.sub(r'[^\u4e00-\u9fa5a-zA-Z0-9]', '', text)
    return hashlib.md5(cleaned.encode()).hexdigest()[:12]


def get_existing_hashes(data):
    """获取已有内容的指纹集合"""
    return {content_hash(d["content"]): d["id"] for d in data}


def classify_scenario(text):
    """根据内容自动分类场景"""
    text_lower = text.lower()
    rules = [
        ("破冰开场", ["你好", "初次", "第一次", "认识", "打招呼", "见到你"]),
        ("暧昧升温", ["暧昧", "喜欢你", "想你", "心动", "撩", "小鹿乱撞", "脸红"]),
        ("表白", ["表白", "喜欢你", "在一起", "做我", "爱你", "心动"]),
        ("吵架和好", ["对不起", "抱歉", "吵架", "和好", "原谅", "我错了", "反思"]),
        ("拒绝", ["拒绝", "不合适", "做朋友", "暂时不想", "你很好"]),
        ("关心体贴", ["关心", "照顾", "注意身体", "多穿", "辛苦了", "心疼"]),
        ("维系关系", ["陪伴", "一直", "永远", "以后", "长久", "珍惜"]),
        ("日常聊天", ["早安", "晚安", "今天", "吃饭", "天气", "周末"]),
    ]
    for scenario, keywords in rules:
        if any(kw in text_lower for kw in keywords):
            return scenario
    return "日常聊天"


def extract_scripts_from_html(html, source_name):
    """从HTML中提取话术内容"""
    soup = BeautifulSoup(html, "html.parser")
    scripts = []

    # 移除脚本和样式
    for tag in soup(["script", "style", "nav", "header", "footer"]):
        tag.decompose()

    text = soup.get_text(separator="\n")

    # 提取引号内容、列表项、段落中的话术
    patterns = [
        r'[""「](.{8,80})[""」]',           # 引号内容
        r'(?:^|\n)[\d]+[.、)）]\s*(.{8,80})',  # 编号列表
        r'(?:^|\n)[•·●]\s*(.{8,80})',        # 圆点列表
        r'(?:^|\n)[-—]\s*(.{8,80})',         # 横线列表
    ]

    seen = set()
    for pattern in patterns:
        matches = re.findall(pattern, text)
        for m in matches:
            m = m.strip()
            # 过滤条件
            if (len(m) >= 8 and len(m) <= 100
                and not re.match(r'^[\d\s]+$', m)
                and 'http' not in m.lower()
                and m not in seen
                and any('\u4e00' <= c <= '\u9fa5' for c in m)):  # 包含中文
                seen.add(m)
                scripts.append(m)

    return scripts


def search_channel(channel, keyword, max_results=5):
    """搜索单个渠道"""
    results = []
    try:
        # 使用百度搜索 site: 限定
        site_map = {
            "小红书": "xiaohongshu.com",
            "知乎": "zhihu.com",
            "微博": "weibo.com",
            "抖音": "douyin.com",
            "百度": "",
        }
        site = site_map.get(channel["name"], "")
        query = f'{keyword}'
        if site:
            query = f'site:{site} {keyword}'

        url = "https://www.baidu.com/s"
        params = {"wd": query, "rn": 10}
        resp = requests.get(url, params=params, headers=HEADERS, timeout=15)
        resp.encoding = "utf-8"

        if resp.status_code == 200:
            extracted = extract_scripts_from_html(resp.text, channel["name"])
            for text in extracted[:max_results]:
                results.append({
                    "content": text,
                    "source": channel["name"],
                })

    except Exception as e:
        log(f"  [{channel['name']}] 搜索失败: {e}")

    return results


def search_emoji_packs():
    """搜索可商用表情包"""
    results = []
    queries = [
        "可商用表情包下载 免费",
        "微信表情包 GIF 免费商用",
        "聊天表情包大全 免费下载",
        "emoji表情包 可商用 CC0",
        "斗图表情包 免费 下载",
    ]

    for query in queries:
        try:
            url = "https://www.baidu.com/s"
            params = {"wd": query, "rn": 5}
            resp = requests.get(url, params=params, headers=HEADERS, timeout=15)
            resp.encoding = "utf-8"

            if resp.status_code == 200:
                soup = BeautifulSoup(resp.text, "html.parser")
                for link in soup.find_all("a", href=True):
                    href = link.get("href", "")
                    text = link.get_text(strip=True)
                    if any(kw in text for kw in ["表情包", "emoji", "斗图", "贴纸"]):
                        if len(text) > 5 and len(text) < 50:
                            results.append({
                                "title": text,
                                "url": href,
                                "source": "百度搜索",
                            })
            time.sleep(random.uniform(1, 3))
        except Exception as e:
            log(f"  表情包搜索失败: {e}")

    return results


def generate_script_id(scenario, existing_data):
    """生成话术ID"""
    prefix_map = {
        "破冰开场": "IC", "暧昧升温": "AM", "日常聊天": "DT",
        "关心体贴": "GX", "吵架和好": "CH", "拒绝": "JF",
        "表白": "BB", "维系关系": "WH",
    }
    prefix = prefix_map.get(scenario, "OT")
    max_num = 0
    for d in existing_data:
        if d["id"].startswith(prefix):
            try:
                num = int(d["id"][2:])
                max_num = max(max_num, num)
            except:
                pass
    return f"{prefix}{max_num + 1:03d}"


def add_emoji_to_content(content):
    """根据内容语境添加合适的emoji"""
    emoji_map = {
        "早安": "☀️", "晚安": "🌙", "你好": "😊", "喜欢": "💕",
        "想你": "💭", "开心": "😄", "难过": "😢", "心疼": "🥺",
        "加油": "💪", "谢谢": "🙏", "对不起": "😔", "抱抱": "🤗",
        "厉害": "✨", "可爱": "🥰", "浪漫": "🌹", "甜蜜": "🍬",
        "幸福": "💖", "陪伴": "🤝", "关心": "❤️", "撩": "😏",
        "吃": "🍜", "天气": "🌤️", "周末": "🎉", "好看": "😍",
    }

    # 如果已有emoji就不再添加
    emoji_pattern = re.compile(
        "[\U0001F600-\U0001F64F\U0001F300-\U0001F5FF\U0001F680-\U0001F6FF"
        "\U0001F1E0-\U0001F1FF\U00002702-\U000027B0\U0001F900-\U0001F9FF"
        "\U0001FA00-\U0001FA6F\U0001FA70-\U0001FAFF\U00002600-\U000026FF]"
    )
    if emoji_pattern.search(content):
        return content

    # 匹配关键词添加emoji
    for keyword, emoji in emoji_map.items():
        if keyword in content:
            # 在关键词后添加emoji
            content = content.replace(keyword, keyword + emoji, 1)
            break
    else:
        # 没有匹配到关键词，根据场景在句尾加通用emoji
        content = content.rstrip("。！？~～… ") + " 😊"

    return content


def log(msg):
    """写入日志"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{timestamp}] {msg}"
    print(line)
    LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(LOG_PATH, "a", encoding="utf-8") as f:
        f.write(line + "\n")


def generate_report(new_scripts, sticker_results):
    """生成采集报告"""
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    lines = [
        f"# Z.Talk 智言 - 每日采集报告",
        f"",
        f"**采集时间:** {now}",
        f"",
        f"## 📝 新增话术 ({len(new_scripts)}条)",
        f"",
    ]

    by_source = {}
    for s in new_scripts:
        src = s.get("source", "未知")
        by_source.setdefault(src, []).append(s)

    for src, items in by_source.items():
        lines.append(f"### {src} ({len(items)}条)")
        for item in items:
            lines.append(f"- [{item.get('scenario', '')}] {item['content'][:50]}...")
        lines.append("")

    if sticker_results:
        lines.extend([
            f"## 🎨 表情包资源 ({len(sticker_results)}条)",
            "",
        ])
        for r in sticker_results[:10]:
            lines.append(f"- {r['title']}")

    lines.extend(["", "---", f"*由 Z.Talk 智言自动采集系统生成*"])

    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(REPORT_PATH, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    log(f"报告已生成: {REPORT_PATH}")


def main():
    log("=" * 50)
    log("Z.Talk 智言 - 多渠道话术采集开始")
    log("=" * 50)

    # 加载现有数据库
    db = load_database()
    existing_hashes = get_existing_hashes(db)
    log(f"现有话术: {len(db)}条")

    new_scripts = []
    today_str = datetime.now().strftime("%Y-%m-%d")

    # 遍历场景和渠道进行采集
    for scenario, keywords in SCENARIO_KEYWORDS.items():
        log(f"\n--- 采集场景: {scenario} ---")
        all_keywords = keywords.copy()

        # 每个渠道采集
        for channel in CHANNELS:
            # 每个场景取2个关键词，避免太多请求
            sample_kw = random.sample(all_keywords, min(2, len(all_keywords)))
            for kw in sample_kw:
                results = search_channel(channel, kw, max_results=3)
                for r in results:
                    h = content_hash(r["content"])
                    if h not in existing_hashes:
                        # 添加emoji
                        content_with_emoji = add_emoji_to_content(r["content"])
                        new_scripts.append({
                            "content": content_with_emoji,
                            "scenario": scenario,
                            "source": r["source"],
                            "hash": h,
                        })
                        existing_hashes[h] = True

                time.sleep(random.uniform(0.5, 2))  # 礼貌延迟

    log(f"\n采集到新话术: {len(new_scripts)}条")

    # 去重并写入数据库
    added_count = 0
    for s in new_scripts:
        new_id = generate_script_id(s["scenario"], db)
        entry = {
            "id": new_id,
            "scenario": s["scenario"],
            "type": "采集",
            "content": s["content"],
            "usage": f"来自{s['source']}，根据语境选用",
            "source": s["source"],
            "emotion_level": 1,
            "gender": "通用",
            "tags": ["采集", s["source"]],
            "date_added": today_str,
        }
        db.append(entry)
        added_count += 1

    if added_count > 0:
        save_database(db)
        log(f"新增 {added_count} 条话术，总计 {len(db)} 条")
    else:
        log("本次无新增话术")

    # 搜索表情包资源
    log("\n--- 搜索表情包资源 ---")
    sticker_results = search_emoji_packs()
    log(f"找到 {len(sticker_results)} 个表情包资源")

    # 保存表情包资源列表
    sticker_path = Path(os.path.expanduser("~/话搭子表情包/资源列表.json"))
    sticker_path.parent.mkdir(parents=True, exist_ok=True)
    if sticker_path.exists():
        with open(sticker_path, "r", encoding="utf-8") as f:
            existing_stickers = json.load(f)
    else:
        existing_stickers = []

    # 去重合并
    existing_titles = {s["title"] for s in existing_stickers}
    for r in sticker_results:
        if r["title"] not in existing_titles:
            existing_stickers.append(r)
            existing_titles.add(r["title"])

    with open(sticker_path, "w", encoding="utf-8") as f:
        json.dump(existing_stickers, f, ensure_ascii=False, indent=2)

    # 生成报告
    generate_report(new_scripts, sticker_results)

    log("=" * 50)
    log(f"采集完成! 新增: {added_count}条 | 总计: {len(db)}条")
    log("=" * 50)

    return added_count


if __name__ == "__main__":
    main()
