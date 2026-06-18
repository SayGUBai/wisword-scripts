#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Z.Talk · 每日话术更新脚本
每日自动从书籍和网络来源提取/生成新话术
"""

import json
import os
from datetime import datetime

DATA_FILE = r"C:\Users\W\Z.Talk话术库\话术数据库.json"
LOG_FILE = r"C:\Users\W\Z.Talk话术库\更新日志.log"

# 每日新增话术模板
DAILY_SCRIPTS = {
    # ---- 早安系列 ----
    "morning": [
        {
            "id_template": "DT_MORNING_{date}",
            "scenario": "日常聊天",
            "type": "关心",
            "content": "早安。不用回复，就是想告诉你——新的一天开始了，你比昨天更接近想要的生活",
            "usage": "早安+鼓励，不给回复压力",
            "source": "自研原创",
            "emotion_level": 2,
            "gender": "通用",
            "tags": ["早安", "鼓励", "不施压"]
        },
        {
            "id_template": "DT_MORNING_{date}",
            "scenario": "日常聊天",
            "type": "幽默",
            "content": "早上好！今天也是不想跟你聊天的……骗你的，其实超想聊的😄",
            "usage": "幽默+反转+表达好感",
            "source": "自研原创",
            "emotion_level": 1,
            "gender": "通用",
            "tags": ["早安", "幽默", "反转"]
        },
        {
            "id_template": "DT_MORNING_{date}",
            "scenario": "日常聊天",
            "type": "引导",
            "content": "早安。今天有什么期待的事吗？我很好奇你的计划",
            "usage": "早安+开放式提问",
            "source": "自研原创",
            "emotion_level": 2,
            "gender": "通用",
            "tags": ["早安", "引导", "好奇"]
        },
    ],
    
    # ---- 晚安系列 ----
    "night": [
        {
            "id_template": "DT_NIGHT_{date}",
            "scenario": "日常聊天",
            "type": "关心",
            "content": "晚安。今天辛苦了。不管发生什么，你都已经做得很好了。明天见",
            "usage": "肯定+晚安，温暖结尾",
            "source": "自研原创",
            "emotion_level": 3,
            "gender": "通用",
            "tags": ["晚安", "肯定", "温暖"]
        },
        {
            "id_template": "DT_NIGHT_{date}",
            "scenario": "日常聊天",
            "type": "引导",
            "content": "睡之前想跟你说——今天跟你聊天很开心。晚安，好梦",
            "usage": "表达愉悦+晚安",
            "source": "自研原创",
            "emotion_level": 3,
            "gender": "通用",
            "tags": ["晚安", "表达", "愉悦"]
        },
    ],
    
    # ---- 晚安系列 ----
    "night": [
        {
            "id_template": "DT_NIGHT_{date}",
            "scenario": "日常聊天",
            "type": "关心",
            "content": "晚安。睡个好觉，把今天的不开心都忘掉。明天又是新的一天",
            "usage": "安慰+展望明天",
            "source": "自研原创",
            "emotion_level": 3,
            "gender": "通用",
            "tags": ["晚安", "安慰", "明天"]
        },
        {
            "id_template": "DT_NIGHT_{date}",
            "scenario": "日常聊天",
            "type": "暧昧",
            "content": "晚安。希望梦里有你，不用是现实那样，梦里的你就好",
            "usage": "暗示好感+温柔",
            "source": "自研原创",
            "emotion_level": 4,
            "gender": "通用",
            "tags": ["晚安", "暗示", "好感"]
        },
    ],
    
    # ---- 情感心理学每日一句 ----
    "psychology": [
        {
            "id_template": "PSY_{date}",
            "scenario": "日常聊天",
            "type": "共情",
            "content": "你知道吗？心理学说——人们最需要的不是被解决，而是被理解。所以我不是要来给你答案的，我只是想懂你",
            "usage": "引用心理学+表达理解意愿",
            "source": "《非暴力沟通》",
            "emotion_level": 3,
            "gender": "通用",
            "tags": ["心理学", "共情", "理解"]
        },
        {
            "id_template": "PSY_{date}",
            "scenario": "日常聊天",
            "type": "引导",
            "content": "依恋理论说，安全感是亲密关系的基础。我想让你知道——在我这里，你是安全的",
            "usage": "引用依恋理论+表达安全感",
            "source": "《依恋与亲密关系》",
            "emotion_level": 4,
            "gender": "通用",
            "tags": ["心理学", "安全感", "依恋"]
        },
        {
            "id_template": "PSY_{date}",
            "scenario": "日常聊天",
            "type": "共情",
            "content": "卡耐基说过——真诚地欣赏和赞美别人。我不是在赞美你，我是在陈述一个事实",
            "usage": "引用名言+真诚赞美",
            "source": "《人性的弱点》",
            "emotion_level": 3,
            "gender": "通用",
            "tags": ["心理学", "赞美", "事实"]
        },
    ],
    
    # ---- 推拉技巧系列 ----
    "push_pull": [
        {
            "id_template": "PP_{date}_1",
            "scenario": "暧昧升温",
            "type": "推拉",
            "content": "你这个人吧——说真的，我有点怕你。因为你太懂怎么让人开心了",
            "usage": "先贬后褒，制造情绪波动",
            "source": "自研原创",
            "emotion_level": 2,
            "gender": "通用",
            "tags": ["推拉", "暧昧", "反转"]
        },
        {
            "id_template": "PP_{date}_2",
            "scenario": "暧昧升温",
            "type": "推拉",
            "content": "你别这样对我笑。我这种人定力很差，很容易当真的",
            "usage": "暗示+示弱，引导对方",
            "source": "自研原创",
            "emotion_level": 3,
            "gender": "通用",
            "tags": ["推拉", "暗示", "示弱"]
        },
    ],
}


def add_daily_scripts():
    """添加每日话术"""
    date_str = datetime.now().strftime("%Y%m%d")
    added = []
    
    # 加载已有数据
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            scripts = json.load(f)
        existing_ids = set(item['id'] for item in scripts)
    else:
        scripts = []
        existing_ids = set()
    
    # 遍历每日模板
    for category, daily_list in DAILY_SCRIPTS.items():
        for script in daily_list:
            # 生成唯一ID（带日期和随机后缀）
            import random
            rand_suffix = random.randint(10, 99)
            new_id = script['id_template'].format(date=date_str).replace('{date}', f"{date_str}_{rand_suffix}")
            
            if new_id not in existing_ids:
                new_script = script.copy()
                new_script['id'] = new_id
                new_script['date_added'] = date_str
                scripts.append(new_script)
                existing_ids.add(new_id)
                added.append(new_script)
    
    # 保存
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(scripts, f, ensure_ascii=False, indent=2)
    
    return added


def log_update(added_count, added_scripts):
    """记录更新日志"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    with open(LOG_FILE, 'a', encoding='utf-8') as f:
        f.write(f"\n{'='*60}\n")
        f.write(f"更新日志: {timestamp}\n")
        f.write(f"新增话术: {added_count} 条\n")
        f.write(f"{'='*60}\n")
        
        for s in added_scripts[:5]:  # 只记录前5条
            f.write(f"  [{s['scenario']}] {s['content'][:40]}...\n")
        
        if added_count > 5:
            f.write(f"  ... 还有 {added_count - 5} 条\n")


if __name__ == '__main__':
    print("  Z.Talk · 每日话术更新")
    print("=" * 50)
    
    added = add_daily_scripts()
    log_update(len(added), added)
    
    print(f"\n✅ 今日新增: {len(added)} 条话术")
    
    # 显示新增的示例
    if added:
        print("\n📝 今日新增示例:")
        for s in added[:5]:
            print(f"   [{s['scenario']}] {s['content'][:35]}...")
        if len(added) > 5:
            print(f"   ... 还有 {len(added) - 5} 条")
    
    print("=" * 50)
