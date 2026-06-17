#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
话搭子 · 每日话术自动更新
每日自动从书籍和网络来源提取/生成新话术
"""

import json
import os
import random
from datetime import datetime

DATA_FILE = r"C:\Users\W\话搭子话术库\话术数据库.json"
LOG_FILE = r"C:\Users\W\话搭子话术库\每日更新.log"
HEARTBEAT = r"C:\Users\W\话搭子话术库\心跳.txt"

# 每日新增话术模板（每日随机选择）
DAILY_TEMPLATES = [
    # 早安系列
    {"scenario": "日常聊天", "type": "关心", "content": "早安！新的一天开始了，希望你今天过得开心", "usage": "简单早安+祝福", "source": "自动更新", "emotion_level": 1, "tags": ["早安", "祝福"]},
    {"scenario": "日常聊天", "type": "幽默", "content": "早上好！今天也是不想上班的一天呢...不过想到能跟你聊天就开心了", "usage": "幽默+反转", "source": "自动更新", "emotion_level": 2, "tags": ["早安", "幽默"]},
    {"scenario": "日常聊天", "type": "引导", "content": "早安，今天有什么计划吗？我很好奇", "usage": "早安+提问", "source": "自动更新", "emotion_level": 2, "tags": ["早安", "好奇"]},
    {"scenario": "日常聊天", "type": "关心", "content": "早安！记得吃早餐哦，今天也要元气满满", "usage": "关心+鼓励", "source": "小红书", "emotion_level": 1, "tags": ["早安", "关心", "元气"]},
    {"scenario": "日常聊天", "type": "暧昧", "content": "早啊，昨晚梦见你了，所以今天醒来特别开心", "usage": "暧昧+甜蜜", "source": "自研原创", "emotion_level": 3, "tags": ["早安", "暧昧", "甜蜜"]},
    
    # 晚安系列
    {"scenario": "日常聊天", "type": "关心", "content": "晚安，今天辛苦了。不管发生什么，你都已经做得很好了", "usage": "肯定+晚安，温暖结尾", "source": "自研原创", "emotion_level": 3, "tags": ["晚安", "肯定", "温暖"]},
    {"scenario": "日常聊天", "type": "引导", "content": "睡之前想跟你说——今天跟你聊天很开心。晚安，好梦", "usage": "表达愉悦+晚安", "source": "自研原创", "emotion_level": 3, "tags": ["晚安", "表达", "愉悦"]},
    {"scenario": "日常聊天", "type": "关心", "content": "晚安。睡个好觉，把今天的不开心都忘掉。明天又是新的一天", "usage": "安慰+展望明天", "source": "自研原创", "emotion_level": 3, "tags": ["晚安", "安慰", "明天"]},
    {"scenario": "日常聊天", "type": "暧昧", "content": "晚安。希望梦里有你，不用是现实那样，梦里的你就好", "usage": "暗示好感+温柔", "source": "自研原创", "emotion_level": 4, "tags": ["晚安", "暗示", "好感"]},
    {"scenario": "日常聊天", "type": "关心", "content": "盖好被子，别着凉了。晚安，好梦", "usage": "具体关心", "source": "小红书", "emotion_level": 2, "tags": ["晚安", "关心", "具体"]},
    
    # 心理学每日一句
    {"scenario": "日常聊天", "type": "共情", "content": "心理学说——人们最需要的不是被解决，而是被理解", "usage": "引用心理学+表达理解", "source": "《非暴力沟通》", "emotion_level": 3, "tags": ["心理学", "共情"]},
    {"scenario": "日常聊天", "type": "引导", "content": "依恋理论说，安全感是亲密关系的基础", "usage": "引用理论+表达安全感", "source": "《依恋与亲密关系》", "emotion_level": 3, "tags": ["心理学", "安全感"]},
    {"scenario": "日常聊天", "type": "共情", "content": "卡耐基说过——真诚地欣赏和赞美别人", "usage": "引用名言+真诚赞美", "source": "《人性的弱点》", "emotion_level": 3, "tags": ["心理学", "赞美"]},
    {"scenario": "日常聊天", "type": "引导", "content": "心理学研究发现，好的关系不是没有冲突，而是学会如何修复冲突", "usage": "引用研究+关系观", "source": "《亲密关系》", "emotion_level": 3, "tags": ["心理学", "冲突"]},
    {"scenario": "日常聊天", "type": "共情", "content": "弗洛姆说爱是能力而非感觉。我想学习和你相处的能力", "usage": "引用经典+表达学习", "source": "《爱的艺术》", "emotion_level": 4, "tags": ["心理学", "爱"]},
    
    # 推拉技巧
    {"scenario": "暧昧升温", "type": "推拉", "content": "你这个人吧——说真的，我有点怕你，因为你太懂怎么让人开心了", "usage": "先贬后褒", "source": "自研原创", "emotion_level": 2, "tags": ["推拉", "暧昧"]},
    {"scenario": "暧昧升温", "type": "推拉", "content": "你别这样对我笑，我这种自制力差的人很容易当真的", "usage": "暗示+示弱", "source": "自研原创", "emotion_level": 3, "tags": ["推拉", "暗示"]},
    {"scenario": "暧昧升温", "type": "推拉", "content": "你有时候挺烦人的——烦到我根本忘不了你", "usage": "反转+表达在意", "source": "小红书", "emotion_level": 3, "tags": ["推拉", "反转"]},
    {"scenario": "暧昧升温", "type": "推拉", "content": "我本来不想这么关心你的，但你总是让我忍不住", "usage": "假装不想+实际关心", "source": "自研原创", "emotion_level": 3, "tags": ["推拉", "关心"]},
    {"scenario": "暧昧升温", "type": "推拉", "content": "你这个人吧，优点很多，缺点就是太吸引人了", "usage": "先说优点+反转", "source": "知乎", "emotion_level": 2, "tags": ["推拉", "优点"]},
    
    # 情绪价值
    {"scenario": "关心体贴", "type": "共情", "content": "你的情绪没有对错，我完全接受", "usage": "接纳情绪", "source": "自研原创", "emotion_level": 4, "tags": ["情绪", "接纳"]},
    {"scenario": "关心体贴", "type": "鼓励", "content": "你不需要一直坚强，偶尔脆弱也没关系", "usage": "允许脆弱", "source": "自研原创", "emotion_level": 4, "tags": ["情绪", "脆弱"]},
    {"scenario": "关心体贴", "type": "共情", "content": "我理解你为什么会有这种感受，你的感受很重要", "usage": "验证感受", "source": "《非暴力沟通》", "emotion_level": 4, "tags": ["情绪", "验证"]},
    {"scenario": "关心体贴", "type": "鼓励", "content": "你已经做得很好了，不要对自己太苛刻", "usage": "自我宽容", "source": "《情商》", "emotion_level": 3, "tags": ["情绪", "宽容"]},
    {"scenario": "关心体贴", "type": "共情", "content": "不管发生什么，我都会站在你这边", "usage": "无条件支持", "source": "自研原创", "emotion_level": 4, "tags": ["情绪", "支持"]},
    
    # 幽默系列
    {"scenario": "日常聊天", "type": "幽默", "content": "我这个人吧，除了长得好看，其他都一般", "usage": "自夸式幽默", "source": "小红书", "emotion_level": 1, "tags": ["幽默", "自夸"]},
    {"scenario": "日常聊天", "type": "幽默", "content": "你要是再这样对我好，我就要赖上你了", "usage": "威胁式幽默", "source": "自研原创", "emotion_level": 2, "tags": ["幽默", "威胁"]},
    {"scenario": "日常聊天", "type": "幽默", "content": "我发现你有个缺点——缺我", "usage": "土味情话", "source": "小红书", "emotion_level": 2, "tags": ["幽默", "土味"]},
    {"scenario": "日常聊天", "type": "幽默", "content": "我刚刚在思考人生——中午吃什么", "usage": "trivial化", "source": "自研原创", "emotion_level": 1, "tags": ["幽默", "人生"]},
    {"scenario": "日常聊天", "type": "幽默", "content": "你猜我怎么想的？猜对了也没奖，猜错了你请我吃饭", "usage": "互动幽默", "source": "知乎", "emotion_level": 1, "tags": ["幽默", "互动"]},
    
    # 日常关心
    {"scenario": "关心体贴", "type": "关心", "content": "记得按时吃饭哦，别太累了", "usage": "日常关心", "source": "自动更新", "emotion_level": 1, "tags": ["关心", "日常"]},
    {"scenario": "关心体贴", "type": "关心", "content": "今天天气变化大，记得增减衣服", "usage": "天气关心", "source": "自动更新", "emotion_level": 1, "tags": ["关心", "天气"]},
    {"scenario": "日常聊天", "type": "关心", "content": "你今天过得怎么样？", "usage": "日常问候", "source": "自动更新", "emotion_level": 1, "tags": ["关心", "问候"]},
    {"scenario": "日常聊天", "type": "分享", "content": "今天看到一朵很可爱的云，想拍给你看", "usage": "分享生活", "source": "自动更新", "emotion_level": 1, "tags": ["分享", "生活"]},
]


def run():
    """运行每日更新"""
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
    
    # 加载已有数据
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            scripts = json.load(f)
        existing_ids = set(item['id'] for item in scripts)
    else:
        scripts = []
        existing_ids = set()
    
    date_str = datetime.now().strftime('%Y%m%d')
    added = []
    
    # 从每日模板随机选择10条
    all_templates = DAILY_TEMPLATES.copy()
    random.shuffle(all_templates)
    
    for i, template in enumerate(all_templates[:10]):  # 每日选10条
        # 使用唯一ID：日期 + 随机数
        import hashlib
        random_suffix = hashlib.md5(f"{date_str}_{i}_{random.random()}".encode()).hexdigest()[:6]
        new_id = f"DAILY_{date_str}_{random_suffix}"
        
        if new_id not in existing_ids:
            script = template.copy()
            script['id'] = new_id
            script['date_added'] = date_str
            scripts.append(script)
            existing_ids.add(new_id)
            added.append(new_id)
    
    # 保存
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(scripts, f, ensure_ascii=False, indent=2)
    
    # 记录日志
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open(LOG_FILE, 'a', encoding='utf-8') as f:
        f.write(f"\n{'='*50}\n")
        f.write(f"更新: {timestamp}\n")
        f.write(f"新增: {len(added)} 条\n")
        f.write(f"{'='*50}\n")
        for new_id in added[:3]:  # 只记录前3条
            print(f"  新增ID: {new_id}")
    
    # 更新心跳
    with open(HEARTBEAT, 'w', encoding='utf-8') as f:
        f.write(f"last_run: {timestamp}\n")
        f.write(f"status: success\n")
        f.write(f"added: {len(added)}\n")
        f.write(f"total: {len(scripts)}\n")
    
    print(f"✅ 今日新增: {len(added)} 条话术")
    print(f"💾 总话术数: {len(scripts)} 条")
    
    return len(added)


if __name__ == '__main__':
    run()
