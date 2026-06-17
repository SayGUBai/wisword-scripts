#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
话搭子 · 高情商话术库 V1
包含分类体系、话术数据、搜索功能
"""

import json
import os
from datetime import datetime

# 话术库根目录
ROOT_DIR = r"C:\Users\W\话搭子话术库"
DATA_FILE = os.path.join(ROOT_DIR, "话术数据库.json")

# 话术数据结构
# {
#   "id": 唯一ID,
#   "scenario": 场景分类,
#   "type": 话术类型,
#   "content": 话术内容,
#   "usage": 使用说明,
#   "source": 来源,
#   "emotion_level": 情绪层次(1-4),
#   "gender": 适用性别,
#   "tags": 标签列表
# }

# ==================== 第一批话术数据 ====================

SCRIPTS = [
    # ---- 破冰开场 ----
    {
        "id": "IC001",
        "scenario": "破冰开场",
        "type": "幽默",
        "content": "你好，我是XXX。刚才看到你，觉得不认识了聊一下会后悔，所以决定冒险打个招呼😄",
        "usage": "初次见面，真诚+幽默",
        "source": "自研原创",
        "emotion_level": 1,
        "gender": "通用",
        "tags": ["初次", "打招呼", "幽默"]
    },
    {
        "id": "IC002",
        "scenario": "破冰开场",
        "type": "好奇",
        "content": "看你朋友圈/资料，感觉你是个很有意思的人，忍不住想认识一下",
        "usage": "赞美+好奇，降低防备",
        "source": "小红书",
        "emotion_level": 1,
        "gender": "通用",
        "tags": ["初次", "赞美", "好奇"]
    },
    {
        "id": "IC003",
        "scenario": "破冰开场",
        "type": "共鸣",
        "content": "你也喜欢XXX啊！我也是！这是不是说明我们至少有一点品味相似？😏",
        "usage": "寻找共同点，制造共鸣",
        "source": "自研原创",
        "emotion_level": 1,
        "gender": "通用",
        "tags": ["初次", "共同点", "轻松"]
    },
    {
        "id": "IC004",
        "scenario": "破冰开场",
        "type": "好奇",
        "content": "我发现一个有趣的事——你给人的第一印象和深入了解后反差好大，你是属于哪种类型？",
        "usage": "制造悬念，引导对方分享",
        "source": "知乎",
        "emotion_level": 2,
        "gender": "通用",
        "tags": ["初次", "引导", "好奇"]
    },
    {
        "id": "IC005",
        "scenario": "破冰开场",
        "type": "幽默",
        "content": "说实话，我本来想准备一个超帅的开场白，但看到你之后大脑一片空白，还是直接说你好吧",
        "usage": "示弱+真诚，拉近距离",
        "source": "自研原创",
        "emotion_level": 1,
        "gender": "通用",
        "tags": ["初次", "真诚", "示弱"]
    },

    # ---- 暧昧升温 ----
    {
        "id": "AM001",
        "scenario": "暧昧升温",
        "type": "推拉",
        "content": "你这个人吧，有时候真的挺让人讨厌的——讨厌到让我总想找你聊天",
        "usage": "先贬后褒，推拉技巧",
        "source": "小红书",
        "emotion_level": 2,
        "gender": "通用",
        "tags": ["暧昧", "推拉", "反转"]
    },
    {
        "id": "AM002",
        "scenario": "暧昧升温",
        "type": "试探",
        "content": "我最近发现一个严重的问题——我好像越来越习惯跟你聊天了，这可怎么办？",
        "usage": "表达在意但不直接表白",
        "source": "自研原创",
        "emotion_level": 2,
        "gender": "通用",
        "tags": ["暧昧", "试探", "好感"]
    },
    {
        "id": "AM003",
        "scenario": "暧昧升温",
        "type": "赞美",
        "content": "你知道吗？每次跟你聊天我都觉得时间过得好快，这是不是你的问题？😏",
        "usage": "赞美+调侃，制造暧昧氛围",
        "source": "小红书",
        "emotion_level": 2,
        "gender": "通用",
        "tags": ["暧昧", "赞美", "调侃"]
    },
    {
        "id": "AM004",
        "scenario": "暧昧升温",
        "type": "推拉",
        "content": "你别对我这么好，我这种自制力差的人很容易误会的",
        "usage": "暗示好感，引导对方继续",
        "source": "知乎",
        "emotion_level": 3,
        "gender": "通用",
        "tags": ["暧昧", "暗示", "推拉"]
    },
    {
        "id": "AM005",
        "scenario": "暧昧升温",
        "type": "引导",
        "content": "如果哪天你无聊了，记得找我。如果哪天我不在了，你就找别人吧——不过我很快会回来的",
        "usage": "表达重视+安全感",
        "source": "自研原创",
        "emotion_level": 3,
        "gender": "通用",
        "tags": ["暧昧", "安全感", "引导"]
    },

    # ---- 日常聊天 ----
    {
        "id": "DT001",
        "scenario": "日常聊天",
        "type": "分享",
        "content": "刚刚看到一个东西突然想到你了——[分享相关内容]，你是不是也这样？",
        "usage": "分享+关联对方，制造连接感",
        "source": "自研原创",
        "emotion_level": 2,
        "gender": "通用",
        "tags": ["日常", "分享", "连接"]
    },
    {
        "id": "DT002",
        "scenario": "日常聊天",
        "type": "关心",
        "content": "今天过得怎么样？不是客套的那种——我是真的想知道你今天开不开心",
        "usage": "真诚关心，区分客套",
        "source": "知乎",
        "emotion_level": 2,
        "gender": "通用",
        "tags": ["日常", "关心", "真诚"]
    },
    {
        "id": "DT003",
        "scenario": "日常聊天",
        "type": "延续",
        "content": "你刚才说的那个事情后来怎么样了？我很好奇后续",
        "usage": "延续对方话题，表示关注",
        "source": "《非暴力沟通》",
        "emotion_level": 2,
        "gender": "通用",
        "tags": ["日常", "延续", "关注"]
    },
    {
        "id": "DT004",
        "scenario": "日常聊天",
        "type": "幽默",
        "content": "我发现我们有个共同点——都在等对方先找对方聊天，看来我们很有默契嘛😂",
        "usage": "幽默化解尴尬",
        "source": "小红书",
        "emotion_level": 1,
        "gender": "通用",
        "tags": ["日常", "幽默", "默契"]
    },
    {
        "id": "DT005",
        "scenario": "日常聊天",
        "type": "引导",
        "content": "如果你现在只能用三个词形容今天，你会选哪三个？",
        "usage": "有趣的问题，引导分享",
        "source": "自研原创",
        "emotion_level": 2,
        "gender": "通用",
        "tags": ["日常", "引导", "趣味"]
    },

    # ---- 关心体贴 ----
    {
        "id": "GX001",
        "scenario": "关心体贴",
        "type": "共情",
        "content": "我能感受到你现在很难受，不想说也没关系，我就在这里陪着你",
        "usage": "不催促+陪伴感",
        "source": "《非暴力沟通》",
        "emotion_level": 3,
        "gender": "通用",
        "tags": ["关心", "共情", "陪伴"]
    },
    {
        "id": "GX002",
        "scenario": "关心体贴",
        "type": "鼓励",
        "content": "你不用急着好起来，我会等你。但我也相信你能跨过这道坎——只是不需要一个人",
        "usage": "接纳情绪+肯定能力",
        "source": "《情商》",
        "emotion_level": 3,
        "gender": "通用",
        "tags": ["关心", "鼓励", "接纳"]
    },
    {
        "id": "GX003",
        "scenario": "关心体贴",
        "type": "共情",
        "content": "换做是我，遇到这种事也会觉得委屈。你的感受是合理的",
        "usage": "验证对方情绪合理性",
        "source": "《非暴力沟通》",
        "emotion_level": 3,
        "gender": "通用",
        "tags": ["关心", "共情", "验证"]
    },
    {
        "id": "GX004",
        "scenario": "关心体贴",
        "type": "行动",
        "content": "我现在能为你做点什么？哪怕只是安静地听你说",
        "usage": "主动提供具体帮助",
        "source": "自研原创",
        "emotion_level": 3,
        "gender": "通用",
        "tags": ["关心", "行动", "倾听"]
    },
    {
        "id": "GX005",
        "scenario": "关心体贴",
        "type": "鼓励",
        "content": "你已经做得很好了，不需要做到完美才值得被认可",
        "usage": "肯定+减压",
        "source": "《人性的弱点》",
        "emotion_level": 3,
        "gender": "通用",
        "tags": ["关心", "肯定", "减压"]
    },

    # ---- 吵架和好 ----
    {
        "id": "CH001",
        "scenario": "吵架和好",
        "type": "道歉",
        "content": "我冷静下来想了想，刚才我说的那些话确实不太妥。我不是故意要伤害你的",
        "usage": "先认错+承认不当",
        "source": "《非暴力沟通》",
        "emotion_level": 3,
        "gender": "通用",
        "tags": ["道歉", "冷静", "承认"]
    },
    {
        "id": "CH002",
        "scenario": "吵架和好",
        "type": "共情",
        "content": "我能理解你为什么会生气。如果是被这样说，我也会不舒服",
        "usage": "换位思考+认可情绪",
        "source": "《亲密关系》",
        "emotion_level": 3,
        "gender": "通用",
        "tags": ["和好", "共情", "换位"]
    },
    {
        "id": "CH003",
        "scenario": "吵架和好",
        "type": "表达",
        "content": "我们的关系比这场争吵重要得多，我不想因为一时冲动失去你",
        "usage": "表达重视+给台阶",
        "source": "自研原创",
        "emotion_level": 4,
        "gender": "通用",
        "tags": ["和好", "重视", "挽回"]
    },
    {
        "id": "CH004",
        "scenario": "吵架和好",
        "type": "引导",
        "content": "你觉得我们怎么避免下次再为同样的事吵架？我想听听你的想法",
        "usage": "引导对方参与解决",
        "source": "《关键对话》",
        "emotion_level": 3,
        "gender": "通用",
        "tags": ["和好", "引导", "解决"]
    },
    {
        "id": "CH005",
        "scenario": "吵架和好",
        "type": "道歉",
        "content": "对不起，我不该那样说话。我不一定能完全理解你的感受，但我愿意学",
        "usage": "真诚道歉+表达学习意愿",
        "source": "自研原创",
        "emotion_level": 4,
        "gender": "通用",
        "tags": ["道歉", "真诚", "学习"]
    },

    # ---- 拒绝 ----
    {
        "id": "JF001",
        "scenario": "拒绝",
        "type": "委婉",
        "content": "谢谢你想到我/找我，不过这次我可能不太方便/不合适。但真的很感谢你",
        "usage": "先感谢+再拒绝",
        "source": "《人性的弱点》",
        "emotion_level": 1,
        "gender": "通用",
        "tags": ["拒绝", "委婉", "感谢"]
    },
    {
        "id": "JF002",
        "scenario": "拒绝",
        "type": "真诚",
        "content": "我理解你很希望我答应，但我确实没办法答应你。抱歉",
        "usage": "清晰表达+不找借口",
        "source": "自研原创",
        "emotion_level": 2,
        "gender": "通用",
        "tags": ["拒绝", "清晰", "真诚"]
    },
    {
        "id": "JF003",
        "scenario": "拒绝",
        "type": "替代",
        "content": "这个我可能不太行，但你可以试试XXX，我觉得那个更适合你",
        "usage": "拒绝+提供替代方案",
        "source": "知乎",
        "emotion_level": 1,
        "gender": "通用",
        "tags": ["拒绝", "替代", "建议"]
    },
    {
        "id": "JF004",
        "scenario": "拒绝",
        "type": "幽默",
        "content": "你这个想法很有创意，但我可能接不住哈哈。换个人试试？",
        "usage": "幽默化解+不伤人",
        "source": "小红书",
        "emotion_level": 1,
        "gender": "通用",
        "tags": ["拒绝", "幽默", "轻松"]
    },

    # ---- 表白 ----
    {
        "id": "BB001",
        "scenario": "表白",
        "type": "真诚",
        "content": "我不知道你会怎么回答，但我不想再藏着了。我喜欢你，不是一时冲动，是慢慢确定的",
        "usage": "真诚+不施压",
        "source": "自研原创",
        "emotion_level": 4,
        "gender": "通用",
        "tags": ["表白", "真诚", "确定性"]
    },
    {
        "id": "BB002",
        "scenario": "表白",
        "type": "引导",
        "content": "跟你在一起的时候，我觉得自己是最放松/最真实的。这种感觉对我来说很重要",
        "usage": "表达感受+暗示心意",
        "source": "《亲密关系》",
        "emotion_level": 4,
        "gender": "通用",
        "tags": ["表白", "感受", "暗示"]
    },
    {
        "id": "BB003",
        "scenario": "表白",
        "type": "试探",
        "content": "如果我说我喜欢你，你觉得我会是认真的吗？",
        "usage": "试探+留退路",
        "source": "知乎",
        "emotion_level": 3,
        "gender": "通用",
        "tags": ["表白", "试探", "留余地"]
    },
    {
        "id": "BB004",
        "scenario": "拒绝",
        "type": "体面",
        "content": "你很好，真的很感谢你喜欢我。只是我对你的感觉没有到那一步。希望你不要因此否定自己",
        "usage": "拒绝+肯定对方价值",
        "source": "自研原创",
        "emotion_level": 3,
        "gender": "通用",
        "tags": ["拒绝表白", "体面", "肯定"]
    },

    # ---- 维系关系 ----
    {
        "id": "WH001",
        "scenario": "维系关系",
        "type": "表达",
        "content": "今天也想跟你说——有你在身边，我觉得很幸运。不用特意做什么，就这样也很好",
        "usage": "日常表达感激",
        "source": "自研原创",
        "emotion_level": 4,
        "gender": "通用",
        "tags": ["维系", "感激", "日常"]
    },
    {
        "id": "WH002",
        "scenario": "维系关系",
        "type": "引导",
        "content": "你觉得我们最近相处得怎么样？有什么想跟我说的吗？",
        "usage": "主动沟通+关心关系",
        "source": "《亲密关系》",
        "emotion_level": 4,
        "gender": "通用",
        "tags": ["维系", "沟通", "关心"]
    },
    {
        "id": "WH003",
        "scenario": "维系关系",
        "type": "行动",
        "content": "这周末我们去XXX吧，就我们两个人，放松一下",
        "usage": "主动创造二人时光",
        "source": "自研原创",
        "emotion_level": 3,
        "gender": "通用",
        "tags": ["维系", "行动", "约会"]
    },
]


def init_db():
    """初始化数据库"""
    os.makedirs(ROOT_DIR, exist_ok=True)
    
    # 加载已有数据
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            existing = json.load(f)
        existing_ids = set(item['id'] for item in existing)
        new_scripts = [s for s in SCRIPTS if s['id'] not in existing_ids]
        scripts = existing + new_scripts
    else:
        scripts = SCRIPTS.copy()
    
    # 保存
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(scripts, f, ensure_ascii=False, indent=2)
    
    return scripts


def search_scripts(keyword, scenario=None, script_type=None):
    """搜索话术"""
    if not os.path.exists(DATA_FILE):
        scripts = init_db()
    else:
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            scripts = json.load(f)
    
    results = []
    for s in scripts:
        match = True
        if keyword and keyword not in s['content'] and keyword not in s.get('usage', ''):
            match = False
        if scenario and s['scenario'] != scenario:
            match = False
        if script_type and s['type'] != script_type:
            match = False
        if match:
            results.append(s)
    
    return results


def get_scripts_by_scenario(scenario):
    """按场景获取话术"""
    results = search_scripts('', scenario=scenario)
    return results


def get_random_script(scenario=None):
    """获取随机话术"""
    results = get_scripts_by_scenario(scenario) if scenario else []
    if not results:
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            results = json.load(f)
    import random
    return random.choice(results)


def add_script(script):
    """添加新话术"""
    scripts = init_db()
    scripts.append(script)
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(scripts, f, ensure_ascii=False, indent=2)
    return script


def get_statistics():
    """获取数据库统计"""
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, 'r', encoding='utf-8') as f:
        scripts = json.load(f)
    
    stats = {
        'total': len(scripts),
        'by_scenario': {},
        'by_type': {},
        'by_source': {}
    }
    for s in scripts:
        stats['by_scenario'][s['scenario']] = stats['by_scenario'].get(s['scenario'], 0) + 1
        stats['by_type'][s['type']] = stats['by_type'].get(s['type'], 0) + 1
        stats['by_source'][s['source']] = stats['by_source'].get(s['source'], 0) + 1
    
    return stats


if __name__ == '__main__':
    # 初始化数据库
    scripts = init_db()
    
    # 统计
    stats = get_statistics()
    print("=" * 50)
    print("  话搭子 · 高情商话术库")
    print("=" * 50)
    print(f"\n📊 当前数据量: {stats['total']} 条话术")
    print("\n📁 按场景分布:")
    for scenario, count in stats['by_scenario'].items():
        print(f"   {scenario}: {count} 条")
    print("\n🏷️  按类型分布:")
    for script_type, count in stats['by_type'].items():
        print(f"   {script_type}: {count} 条")
    print(f"\n💾 数据文件: {DATA_FILE}")
    print("=" * 50)
    
    # 示例：搜索话术
    print("\n🔍 搜索示例：'你好'")
    results = search_scripts('你好')
    for r in results[:3]:
        print(f"   [{r['scenario']}] {r['content'][:30]}...")
    
    # 示例：随机话术
    print("\n🎲 随机话术示例:")
    r = get_random_script()
    print(f"   [{r['scenario']}/{r['type']}] {r['content']}")
    print(f"   💡 用法: {r['usage']}")
