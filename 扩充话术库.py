#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Z.Talk · 大规模扩充高情商话术库 V2
目标：从69条扩充到200+条
"""

import json
import os
import random
from datetime import datetime

DATA_FILE = r"C:\Users\W\Z.Talk话术库\话术数据库.json"

# ==================== 新增话术数据 ====================

NEW_SCRIPTS = [
    # ========== 破冰开场（扩充到20条）==========
    {"scenario": "破冰开场", "type": "好奇", "content": "刚听朋友提起你，说你特别有意思，今天终于见到了", "usage": "第三方背书+赞美", "source": "自研原创", "emotion_level": 2, "tags": ["破冰", "赞美", "第三方"]},
    {"scenario": "破冰开场", "type": "幽默", "content": "你好，我是XXX。刚才看到你，觉得不认识了聊一下会后悔，所以决定冒险打个招呼😄", "usage": "真诚+幽默", "source": "自研原创", "emotion_level": 2, "tags": ["破冰", "真诚", "幽默"]},
    {"scenario": "破冰开场", "type": "分享", "content": "你也喜欢这家店啊！我每次心情不好的时候来这儿就觉得特别治愈", "usage": "共同兴趣+感受分享", "source": "小红书", "emotion_level": 2, "tags": ["破冰", "共同点", "感受"]},
    {"scenario": "破冰开场", "type": "好奇", "content": "看你朋友圈发的照片，你好像去过好多地方，你最推荐哪里？", "usage": "朋友圈+提问", "source": "知乎", "emotion_level": 1, "tags": ["破冰", "朋友圈", "提问"]},
    {"scenario": "破冰开场", "type": "赞美", "content": "你的穿搭很有品味诶，这个搭配在哪里买的？", "usage": "具体赞美+请教", "source": "小红书", "emotion_level": 1, "tags": ["破冰", "赞美", "具体"]},
    {"scenario": "破冰开场", "type": "好奇", "content": "你是做什么工作的呀？我总觉得你身上有一种很特别的气质", "usage": "提问+模糊赞美", "source": "自研原创", "emotion_level": 2, "tags": ["破冰", "提问", "气质"]},
    {"scenario": "破冰开场", "type": "幽默", "content": "你好，我是来交朋友的。不收手续费，还倒贴零食那种", "usage": "自嘲式幽默", "source": "知乎", "emotion_level": 1, "tags": ["破冰", "幽默", "自嘲"]},
    {"scenario": "破冰开场", "type": "分享", "content": "我发现一个超棒的咖啡馆，要不要一起去试试？就当帮我判断值不值得推荐给其他人", "usage": "邀请+给对方价值", "source": "自研原创", "emotion_level": 2, "tags": ["破冰", "邀请", "价值"]},
    {"scenario": "破冰开场", "type": "好奇", "content": "你平时周末都喜欢做些什么？我最近在找一个新的爱好", "usage": "生活话题+求助", "source": "小红书", "emotion_level": 1, "tags": ["破冰", "生活", "求助"]},
    {"scenario": "破冰开场", "type": "赞美", "content": "你的声音好好听，跟你聊天感觉很舒服", "usage": "细节赞美+感受", "source": "自研原创", "emotion_level": 2, "tags": ["破冰", "细节", "感受"]},
    {"scenario": "破冰开场", "type": "幽默", "content": "我这个人不太会聊天，但我觉得你值得我用最大的诚意来聊", "usage": "示弱+真诚", "source": "知乎", "emotion_level": 3, "tags": ["破冰", "示弱", "真诚"]},
    {"scenario": "破冰开场", "type": "好奇", "content": "你看起来不像本地人诶，你的口音好特别，是哪里的呀？", "usage": "观察+好奇", "source": "小红书", "emotion_level": 1, "tags": ["破冰", "观察", "好奇"]},
    {"scenario": "破冰开场", "type": "分享", "content": "你也养猫啊！我家那只天天拆家，你有没有什么对付办法？", "usage": "共同兴趣+求助", "source": "自研原创", "emotion_level": 1, "tags": ["破冰", "共同点", "求助"]},
    {"scenario": "破冰开场", "type": "好奇", "content": "你看起来好年轻啊，你是不是偷偷吃了防腐剂？", "usage": "夸张赞美", "source": "小红书", "emotion_level": 1, "tags": ["破冰", "赞美", "幽默"]},
    {"scenario": "破冰开场", "type": "赞美", "content": "你笑起来很好看诶，让人看了心情都会变好", "usage": "具体赞美+影响", "source": "自研原创", "emotion_level": 2, "tags": ["破冰", "赞美", "笑容"]},
    {"scenario": "破冰开场", "type": "好奇", "content": "看你朋友圈发的书，你也喜欢看村上春树？你觉得《挪威的森林》怎么样？", "usage": "朋友圈+具体话题", "source": "知乎", "emotion_level": 2, "tags": ["破冰", "读书", "话题"]},
    {"scenario": "破冰开场", "type": "幽默", "content": "你好，我是来拓展社交圈的。目前进展顺利，因为已经跟你说话了", "usage": "幽默+目的性", "source": "知乎", "emotion_level": 1, "tags": ["破冰", "幽默", "社交"]},
    {"scenario": "破冰开场", "type": "分享", "content": "我也喜欢健身！你一般练什么部位？我最近在纠结要不要加练腿部", "usage": "共同兴趣+具体问题", "source": "小红书", "emotion_level": 1, "tags": ["破冰", "健身", "具体"]},
    {"scenario": "破冰开场", "type": "好奇", "content": "你第一眼给我的感觉是——你是一个很有趣的人。后来发现果然如此", "usage": "第一印象+确认", "source": "自研原创", "emotion_level": 3, "tags": ["破冰", "印象", "确认"]},
    {"scenario": "破冰开场", "type": "赞美", "content": "你讲话的逻辑好清晰，跟你聊天感觉脑子都被理顺了", "usage": "能力赞美+感受", "source": "自研原创", "emotion_level": 2, "tags": ["破冰", "能力", "逻辑"]},
    
    # ========== 暧昧升温（扩充到30条）==========
    {"scenario": "暧昧升温", "type": "推拉", "content": "你这个人吧——说真的，我有点怕你，因为你太懂怎么让人开心了", "usage": "先贬后褒", "source": "自研原创", "emotion_level": 2, "tags": ["推拉", "暧昧", "赞美"]},
    {"scenario": "暧昧升温", "type": "推拉", "content": "你别这样对我笑，我这种自制力差的人很容易当真的", "usage": "暗示+示弱", "source": "自研原创", "emotion_level": 3, "tags": ["推拉", "暗示", "自制力"]},
    {"scenario": "暧昧升温", "type": "推拉", "content": "你有时候挺烦人的——烦到我根本忘不了你", "usage": "反转+表达在意", "source": "小红书", "emotion_level": 3, "tags": ["推拉", "反转", "在意"]},
    {"scenario": "暧昧升温", "type": "推拉", "content": "我本来不想这么关心你的，但你总是让我忍不住", "usage": "假装不想+实际关心", "source": "自研原创", "emotion_level": 3, "tags": ["推拉", "关心", "忍不住"]},
    {"scenario": "暧昧升温", "type": "推拉", "content": "你这个人吧，优点很多，缺点就是太吸引人了", "usage": "先说优点+反转", "source": "知乎", "emotion_level": 2, "tags": ["推拉", "优点", "吸引人"]},
    {"scenario": "暧昧升温", "type": "暧昧", "content": "我发现跟你聊天有个副作用——每次看完手机都会傻笑", "usage": "副作用+暗示", "source": "自研原创", "emotion_level": 3, "tags": ["暧昧", "副作用", "傻笑"]},
    {"scenario": "暧昧升温", "type": "试探", "content": "你理想型是什么样的？我好奇一下，不是认真的", "usage": "试探+假装随便", "source": "知乎", "emotion_level": 3, "tags": ["试探", "理想型", "假装"]},
    {"scenario": "暧昧升温", "type": "暧昧", "content": "你知不知道，你认真说话的时候特别迷人", "usage": "观察+赞美", "source": "自研原创", "emotion_level": 3, "tags": ["暧昧", "观察", "迷人"]},
    {"scenario": "暧昧升温", "type": "试探", "content": "我们认识多久了？怎么感觉像是认识了好久好久", "usage": "时间感知+暗示", "source": "小红书", "emotion_level": 3, "tags": ["试探", "时间", "熟悉感"]},
    {"scenario": "暧昧升温", "type": "推拉", "content": "你最近对我这么好，我差点以为你喜欢我了——还好我知道你不是", "usage": "假意+反转", "source": "知乎", "emotion_level": 4, "tags": ["推拉", "反转", "喜欢"]},
    {"scenario": "暧昧升温", "type": "暧昧", "content": "跟你聊天有个问题——我现在跟别人聊天都觉得没意思了", "usage": "对比+暗示特殊性", "source": "自研原创", "emotion_level": 3, "tags": ["暧昧", "对比", "特殊"]},
    {"scenario": "暧昧升温", "type": "试探", "content": "你相信一见钟情还是日久生情？我先回答——后者，因为前者太冒险了", "usage": "提问+自我暴露", "source": "小红书", "emotion_level": 2, "tags": ["试探", "爱情观", "暴露"]},
    {"scenario": "暧昧升温", "type": "暧昧", "content": "我刚刚在听一首歌，歌词突然戳到我了——因为想到了你", "usage": "触发+关联", "source": "自研原创", "emotion_level": 4, "tags": ["暧昧", "歌曲", "关联"]},
    {"scenario": "暧昧升温", "type": "推拉", "content": "你别总回我消息这么快，我容易上瘾", "usage": "反向表达+暗示", "source": "知乎", "emotion_level": 3, "tags": ["推拉", "反向", "上瘾"]},
    {"scenario": "暧昧升温", "type": "暧昧", "content": "我发现自己有个问题——每次看到好玩的东西，第一个想分享的人是你", "usage": "自我觉察+暗示", "source": "自研原创", "emotion_level": 4, "tags": ["暧昧", "觉察", "分享"]},
    {"scenario": "暧昧升温", "type": "试探", "content": "你有没有过这种感觉——明明才认识不久，却觉得对方很懂你", "usage": "感受共鸣+暗示", "source": "小红书", "emotion_level": 3, "tags": ["试探", "共鸣", "懂你"]},
    {"scenario": "暧昧升温", "type": "暧昧", "content": "你笑起来的样子，让我想起夏天的风——很舒服，让人舍不得移开视线", "usage": "比喻+赞美", "source": "自研原创", "emotion_level": 3, "tags": ["暧昧", "比喻", "笑容"]},
    {"scenario": "暧昧升温", "type": "推拉", "content": "你这个人太危险了，明明什么都没做，却让我心跳加速", "usage": "指控+反转", "source": "知乎", "emotion_level": 4, "tags": ["推拉", "危险", "心跳"]},
    {"scenario": "暧昧升温", "type": "暧昧", "content": "跟你聊天有个好处——原本糟糕的心情瞬间就好了", "usage": "好处+暗示重要性", "source": "自研原创", "emotion_level": 3, "tags": ["暧昧", "好处", "心情"]},
    {"scenario": "暧昧升温", "type": "试探", "content": "你觉得两个人在一起最重要的是什么？我觉得是——聊天聊得来", "usage": "提问+给出自己的答案", "source": "小红书", "emotion_level": 2, "tags": ["试探", "关系观", "聊天"]},
    {"scenario": "暧昧升温", "type": "暧昧", "content": "我刚刚做了一个梦，梦里你在跟我吵架。醒来第一件事就是想跟你说——幸好是梦", "usage": "梦境+表达在意", "source": "自研原创", "emotion_level": 4, "tags": ["暧昧", "梦境", "在意"]},
    {"scenario": "暧昧升温", "type": "推拉", "content": "你对我这么好，我都不知道该怎么回报你了——要不你请我喝杯奶茶吧", "usage": "感谢+小要求", "source": "知乎", "emotion_level": 3, "tags": ["推拉", "感谢", "邀约"]},
    {"scenario": "暧昧升温", "type": "暧昧", "content": "你知道吗？你说话的声音有一种魔力，让我每次都想多听几句", "usage": "细节赞美+魔力", "source": "自研原创", "emotion_level": 3, "tags": ["暧昧", "声音", "魔力"]},
    {"scenario": "暧昧升温", "type": "试探", "content": "你周末一般怎么过？我刚好有个想法，在犹豫要不要告诉你", "usage": "生活+悬念", "source": "小红书", "emotion_level": 3, "tags": ["试探", "周末", "悬念"]},
    {"scenario": "暧昧升温", "type": "暧昧", "content": "我发现你有一个特别好的优点——你总是能注意到别人忽略的细节", "usage": "观察+赞美细节", "source": "自研原创", "emotion_level": 3, "tags": ["暧昧", "观察", "细节"]},
    {"scenario": "暧昧升温", "type": "推拉", "content": "你再这样对我好下去，我可就要当真了——到时候你别怪我", "usage": "警告+暗示", "source": "知乎", "emotion_level": 4, "tags": ["推拉", "警告", "当真"]},
    {"scenario": "暧昧升温", "type": "暧昧", "content": "跟你待在一起的时间总是过得特别快，是不是你有什么超能力？", "usage": "感受+幽默", "source": "自研原创", "emotion_level": 2, "tags": ["暧昧", "时间", "幽默"]},
    {"scenario": "暧昧升温", "type": "试探", "content": "你相信缘分吗？我觉得我跟你的相遇应该就是", "usage": "哲学提问+暗示", "source": "小红书", "emotion_level": 4, "tags": ["试探", "缘分", "相遇"]},
    {"scenario": "暧昧升温", "type": "暧昧", "content": "我最近发现一首很好听的歌，歌词写的就是我现在的心情——下次唱给你听", "usage": "音乐+暗示", "source": "自研原创", "emotion_level": 4, "tags": ["暧昧", "音乐", "心情"]},
    {"scenario": "暧昧升温", "type": "推拉", "content": "你这个人真的很奇怪——明明不熟，却让我觉得像认识了好久", "usage": "奇怪+反转+熟悉感", "source": "知乎", "emotion_level": 3, "tags": ["推拉", "奇怪", "熟悉"]},
    
    # ========== 日常聊天（扩充到40条）==========
    {"scenario": "日常聊天", "type": "关心", "content": "早安！新的一天开始了，希望你今天过得开心", "usage": "简单早安+祝福", "source": "自动更新", "emotion_level": 1, "tags": ["早安", "祝福"]},
    {"scenario": "日常聊天", "type": "幽默", "content": "早上好！今天也是不想上班的一天呢...不过想到能跟你聊天就开心了", "usage": "幽默+反转", "source": "自动更新", "emotion_level": 2, "tags": ["早安", "幽默"]},
    {"scenario": "日常聊天", "type": "引导", "content": "早安，今天有什么计划吗？我很好奇", "usage": "早安+提问", "source": "自动更新", "emotion_level": 2, "tags": ["早安", "好奇"]},
    {"scenario": "日常聊天", "type": "关心", "content": "早安！记得吃早餐哦，今天也要元气满满", "usage": "关心+鼓励", "source": "小红书", "emotion_level": 1, "tags": ["早安", "关心", "元气"]},
    {"scenario": "日常聊天", "type": "暧昧", "content": "早啊，昨晚梦见你了，所以今天醒来特别开心", "usage": "暧昧+甜蜜", "source": "自研原创", "emotion_level": 3, "tags": ["早安", "暧昧", "甜蜜"]},
    {"scenario": "日常聊天", "type": "关心", "content": "晚安，今天辛苦了。不管发生什么，你都已经做得很好了", "usage": "肯定+晚安，温暖结尾", "source": "自研原创", "emotion_level": 3, "tags": ["晚安", "肯定", "温暖"]},
    {"scenario": "日常聊天", "type": "引导", "content": "睡之前想跟你说——今天跟你聊天很开心。晚安，好梦", "usage": "表达愉悦+晚安", "source": "自研原创", "emotion_level": 3, "tags": ["晚安", "表达", "愉悦"]},
    {"scenario": "日常聊天", "type": "关心", "content": "晚安。睡个好觉，把今天的不开心都忘掉。明天又是新的一天", "usage": "安慰+展望明天", "source": "自研原创", "emotion_level": 3, "tags": ["晚安", "安慰", "明天"]},
    {"scenario": "日常聊天", "type": "暧昧", "content": "晚安。希望梦里有你，不用是现实那样，梦里的你就好", "usage": "暗示好感+温柔", "source": "自研原创", "emotion_level": 4, "tags": ["晚安", "暗示", "好感"]},
    {"scenario": "日常聊天", "type": "关心", "content": "盖好被子，别着凉了。晚安，好梦", "usage": "具体关心", "source": "小红书", "emotion_level": 2, "tags": ["晚安", "关心", "具体"]},
    {"scenario": "日常聊天", "type": "分享", "content": "今天看到一朵很可爱的云，想拍给你看", "usage": "分享生活", "source": "自动更新", "emotion_level": 1, "tags": ["分享", "生活"]},
    {"scenario": "日常聊天", "type": "分享", "content": "我刚吃到一家超好吃的餐厅，下次带你去", "usage": "美食+未来邀约", "source": "小红书", "emotion_level": 2, "tags": ["分享", "美食", "邀约"]},
    {"scenario": "日常聊天", "type": "引导", "content": "你今天有没有遇到什么有趣的事？我想听", "usage": "主动倾听+引导", "source": "自研原创", "emotion_level": 2, "tags": ["引导", "倾听", "有趣"]},
    {"scenario": "日常聊天", "type": "共情", "content": "听起来你今天过得挺累的，辛苦啦", "usage": "认可+共情", "source": "自研原创", "emotion_level": 2, "tags": ["共情", "认可", "辛苦"]},
    {"scenario": "日常聊天", "type": "幽默", "content": "我刚刚在思考人生——中午吃什么", "usage": "trivial化", "source": "自研原创", "emotion_level": 1, "tags": ["幽默", "人生"]},
    {"scenario": "日常聊天", "type": "引导", "content": "你最近有没有听到什么好听的歌？我想分享一下我最近循环的歌单", "usage": "音乐+分享", "source": "小红书", "emotion_level": 1, "tags": ["引导", "音乐", "分享"]},
    {"scenario": "日常聊天", "type": "关心", "content": "今天降温了，出门多穿点，别感冒了", "usage": "天气+关心", "source": "小红书", "emotion_level": 1, "tags": ["关心", "天气", "降温"]},
    {"scenario": "日常聊天", "type": "幽默", "content": "我发现一个规律——每次跟你聊天，时间都过得特别快", "usage": "观察+暗示", "source": "自研原创", "emotion_level": 2, "tags": ["幽默", "观察", "时间"]},
    {"scenario": "日常聊天", "type": "引导", "content": "你周末一般喜欢做什么？我最近在找新的活动", "usage": "生活话题+求助", "source": "知乎", "emotion_level": 1, "tags": ["引导", "周末", "求助"]},
    {"scenario": "日常聊天", "type": "分享", "content": "我刚看完一部电影，剧情超棒，强烈推荐你看", "usage": "推荐+感受", "source": "小红书", "emotion_level": 1, "tags": ["分享", "电影", "推荐"]},
    {"scenario": "日常聊天", "type": "共情", "content": "我能理解你的感受，换做是我也会这样想", "usage": "理解+认同", "source": "自研原创", "emotion_level": 3, "tags": ["共情", "理解", "认同"]},
    {"scenario": "日常聊天", "type": "引导", "content": "你小时候最喜欢做什么？我超好奇别人的童年", "usage": "童年话题+好奇", "source": "知乎", "emotion_level": 1, "tags": ["引导", "童年", "好奇"]},
    {"scenario": "日常聊天", "type": "关心", "content": "你吃饭了吗？别又忙起来就忘了", "usage": "关心+提醒", "source": "自研原创", "emotion_level": 1, "tags": ["关心", "吃饭", "提醒"]},
    {"scenario": "日常聊天", "type": "幽默", "content": "我刚刚在路上看到一只猫，长得特别像你——慵懒又可爱", "usage": "动物类比+赞美", "source": "小红书", "emotion_level": 2, "tags": ["幽默", "猫", "赞美"]},
    {"scenario": "日常聊天", "type": "引导", "content": "你有没有什么特别想去的地方？我做个攻略", "usage": "旅行+主动", "source": "自研原创", "emotion_level": 2, "tags": ["引导", "旅行", "主动"]},
    {"scenario": "日常聊天", "type": "分享", "content": "我今天遇到了一件特别搞笑的事，一定要讲给你听", "usage": "悬念+分享欲", "source": "自研原创", "emotion_level": 2, "tags": ["分享", "搞笑", "悬念"]},
    {"scenario": "日常聊天", "type": "共情", "content": "你不需要每次都那么坚强，在我面前可以做真实的自己", "usage": "接纳+安全感", "source": "自研原创", "emotion_level": 4, "tags": ["共情", "接纳", "安全感"]},
    {"scenario": "日常聊天", "type": "引导", "content": "你最喜欢哪个季节？我觉得夏天最适合跟你一起散步", "usage": "季节+隐含邀约", "source": "自研原创", "emotion_level": 3, "tags": ["引导", "季节", "隐含"]},
    {"scenario": "日常聊天", "type": "关心", "content": "看你最近发朋友圈好像很忙，要注意休息哦", "usage": "关注+关心", "source": "小红书", "emotion_level": 2, "tags": ["关心", "关注", "休息"]},
    {"scenario": "日常聊天", "type": "幽默", "content": "你知道我最喜欢你哪一点吗？你什么都好，就是太完美了让我有压力", "usage": "反转赞美", "source": "知乎", "emotion_level": 2, "tags": ["幽默", "反转", "完美"]},
    {"scenario": "日常聊天", "type": "分享", "content": "我刚学会了一道菜，下次做给你尝尝——不好吃算我输", "usage": "技能+邀约+自信", "source": "自研原创", "emotion_level": 2, "tags": ["分享", "做菜", "邀约"]},
    {"scenario": "日常聊天", "type": "引导", "content": "你相信星座吗？我觉得你的星座特质在你身上体现得特别明显", "usage": "星座+具体化", "source": "小红书", "emotion_level": 1, "tags": ["引导", "星座", "具体"]},
    {"scenario": "日常聊天", "type": "共情", "content": "你的感受是最重要的，不用为了迎合别人委屈自己", "usage": "肯定+鼓励做自己", "source": "自研原创", "emotion_level": 4, "tags": ["共情", "肯定", "做自己"]},
    {"scenario": "日常聊天", "type": "关心", "content": "今天工作/学习累不累？别给自己太大压力", "usage": "关心+减压", "source": "自研原创", "emotion_level": 2, "tags": ["关心", "压力", "减压"]},
    {"scenario": "日常聊天", "type": "幽默", "content": "我刚刚在想，要是每天都能跟你聊天就好了——然后发现今天是周一", "usage": "愿望+现实反差", "source": "自研原创", "emotion_level": 2, "tags": ["幽默", "愿望", "反差"]},
    {"scenario": "日常聊天", "type": "引导", "content": "你觉得自己最大的优点是什么？我帮你补充几个", "usage": "提问+赞美铺垫", "source": "知乎", "emotion_level": 2, "tags": ["引导", "优点", "赞美"]},
    {"scenario": "日常聊天", "type": "分享", "content": "今天路过一家花店，看到一束花特别好看，第一时间想到了你", "usage": "触发+关联", "source": "自研原创", "emotion_level": 3, "tags": ["分享", "触发", "关联"]},
    {"scenario": "日常聊天", "type": "共情", "content": "不管发生什么，我都站在你这边。你不需要一个人扛", "usage": "支持+分担", "source": "自研原创", "emotion_level": 4, "tags": ["共情", "支持", "分担"]},
    {"scenario": "日常聊天", "type": "引导", "content": "你小时候的梦想是什么？我觉得了解这个能更懂你", "usage": "梦想+深度了解", "source": "知乎", "emotion_level": 2, "tags": ["引导", "梦想", "深度"]},
    {"scenario": "日常聊天", "type": "关心", "content": "你最近睡眠怎么样？别熬夜了，对身体不好", "usage": "健康关心", "source": "小红书", "emotion_level": 2, "tags": ["关心", "睡眠", "健康"]},
    
    # ========== 关心体贴（扩充到20条）==========
    {"scenario": "关心体贴", "type": "共情", "content": "你的情绪没有对错，我完全接受", "usage": "接纳情绪", "source": "自研原创", "emotion_level": 4, "tags": ["情绪", "接纳"]},
    {"scenario": "关心体贴", "type": "鼓励", "content": "你不需要一直坚强，偶尔脆弱也没关系", "usage": "允许脆弱", "source": "自研原创", "emotion_level": 4, "tags": ["情绪", "脆弱"]},
    {"scenario": "关心体贴", "type": "共情", "content": "我理解你为什么会有这种感受，你的感受很重要", "usage": "验证感受", "source": "《非暴力沟通》", "emotion_level": 4, "tags": ["情绪", "验证"]},
    {"scenario": "关心体贴", "type": "鼓励", "content": "你已经做得很好了，不要对自己太苛刻", "usage": "自我宽容", "source": "《情商》", "emotion_level": 3, "tags": ["情绪", "宽容"]},
    {"scenario": "关心体贴", "type": "共情", "content": "不管发生什么，我都会站在你这边", "usage": "无条件支持", "source": "自研原创", "emotion_level": 4, "tags": ["情绪", "支持"]},
    {"scenario": "关心体贴", "type": "关心", "content": "你最近是不是压力很大？想聊聊的话我随时都在", "usage": "观察+邀请", "source": "自研原创", "emotion_level": 3, "tags": ["关心", "压力", "邀请"]},
    {"scenario": "关心体贴", "type": "共情", "content": "难过是正常的，不用逼自己马上好起来", "usage": "允许悲伤", "source": "自研原创", "emotion_level": 4, "tags": ["共情", "悲伤", "允许"]},
    {"scenario": "关心体贴", "type": "鼓励", "content": "你比自己想象的更强大，只是暂时没发现而已", "usage": "赋能+肯定", "source": "知乎", "emotion_level": 3, "tags": ["鼓励", "赋能", "肯定"]},
    {"scenario": "关心体贴", "type": "关心", "content": "你吃饭了吗？我给你点个外卖吧", "usage": "关心+行动", "source": "小红书", "emotion_level": 2, "tags": ["关心", "行动", "外卖"]},
    {"scenario": "关心体贴", "type": "共情", "content": "你不用向任何人证明什么，你本身就很棒", "usage": "肯定+不需要证明", "source": "自研原创", "emotion_level": 4, "tags": ["共情", "肯定", "本身"]},
    {"scenario": "关心体贴", "type": "鼓励", "content": "慢慢来，比较快。不用着急，我会陪你", "usage": "耐心+陪伴", "source": "自研原创", "emotion_level": 4, "tags": ["鼓励", "耐心", "陪伴"]},
    {"scenario": "关心体贴", "type": "关心", "content": "你看起来不太开心，发生什么事了吗？", "usage": "观察+询问", "source": "自研原创", "emotion_level": 2, "tags": ["关心", "观察", "询问"]},
    {"scenario": "关心体贴", "type": "共情", "content": "你的感受是合理的，换做是我也会这样", "usage": "验证+共情", "source": "自研原创", "emotion_level": 4, "tags": ["共情", "验证", "合理"]},
    {"scenario": "关心体贴", "type": "鼓励", "content": "每一次跌倒都是为了更好地站起来，你已经很棒了", "usage": "挫折+鼓励", "source": "知乎", "emotion_level": 3, "tags": ["鼓励", "挫折", "棒"]},
    {"scenario": "关心体贴", "type": "关心", "content": "天气冷了，记得多喝热水，照顾好自己", "usage": "天气+关心", "source": "小红书", "emotion_level": 1, "tags": ["关心", "天气", "热水"]},
    {"scenario": "关心体贴", "type": "共情", "content": "你不需要完美，真实的样子就足够好了", "usage": "接纳+真实", "source": "自研原创", "emotion_level": 4, "tags": ["共情", "接纳", "真实"]},
    {"scenario": "关心体贴", "type": "鼓励", "content": "你已经走了很远的路了，停下来休息一下也没关系", "usage": "认可努力+允许休息", "source": "自研原创", "emotion_level": 4, "tags": ["鼓励", "认可", "休息"]},
    {"scenario": "关心体贴", "type": "关心", "content": "你最近气色不太好，是不是没休息好？", "usage": "观察+关心", "source": "自研原创", "emotion_level": 2, "tags": ["关心", "观察", "气色"]},
    {"scenario": "关心体贴", "type": "共情", "content": "你不是一个人，有我陪着你呢", "usage": "陪伴+ reassurance", "source": "自研原创", "emotion_level": 4, "tags": ["共情", "陪伴", "reassurance"]},
    {"scenario": "关心体贴", "type": "鼓励", "content": "你比自己以为的更有力量，相信我", "usage": "信任+赋能", "source": "自研原创", "emotion_level": 4, "tags": ["鼓励", "信任", "力量"]},
    
    # ========== 吵架和好（扩充到20条）==========
    {"scenario": "吵架和好", "type": "道歉", "content": "对不起，我刚才语气重了。我不是那个意思，我只是太在意你了", "usage": "道歉+解释+在意", "source": "自研原创", "emotion_level": 4, "tags": ["道歉", "语气", "在意"]},
    {"scenario": "吵架和好", "type": "共情", "content": "我理解你为什么生气了，如果换做是我，我也会不舒服", "usage": "换位思考+认可", "source": "自研原创", "emotion_level": 4, "tags": ["共情", "换位", "认可"]},
    {"scenario": "吵架和好", "type": "表达", "content": "我生气不是因为不在乎你，恰恰是因为太在乎了才会失控", "usage": "解释情绪根源", "source": "自研原创", "emotion_level": 4, "tags": ["表达", "情绪", "在乎"]},
    {"scenario": "吵架和好", "type": "道歉", "content": "我反思了一下，这件事确实是我的错。你能给我一个弥补的机会吗？", "usage": "反思+认错+请求", "source": "知乎", "emotion_level": 4, "tags": ["道歉", "反思", "弥补"]},
    {"scenario": "吵架和好", "type": "共情", "content": "我知道你现在不想理我，但我还是想说——你对我来说很重要", "usage": "尊重空间+表达重视", "source": "自研原创", "emotion_level": 4, "tags": ["共情", "空间", "重视"]},
    {"scenario": "吵架和好", "type": "表达", "content": "我不想赢这场争吵，我只想赢回你", "usage": "态度+关系优先", "source": "小红书", "emotion_level": 5, "tags": ["表达", "关系", "优先"]},
    {"scenario": "吵架和好", "type": "道歉", "content": "我说话没过脑子，伤到你了真的很抱歉。以后我会注意的", "usage": "承认错误+承诺改变", "source": "自研原创", "emotion_level": 4, "tags": ["道歉", "承诺", "改变"]},
    {"scenario": "吵架和好", "type": "共情", "content": "你的感受是第一位的，我的面子不重要", "usage": "感受优先", "source": "自研原创", "emotion_level": 4, "tags": ["共情", "感受", "面子"]},
    {"scenario": "吵架和好", "type": "表达", "content": "吵架不是为了分对错，是为了让我们更了解彼此", "usage": "重构争吵意义", "source": "知乎", "emotion_level": 3, "tags": ["表达", "争吵", "了解"]},
    {"scenario": "吵架和好", "type": "道歉", "content": "我错了，不该那样对你说话。原谅我好不好？", "usage": "直接认错+请求原谅", "source": "自研原创", "emotion_level": 4, "tags": ["道歉", "认错", "原谅"]},
    {"scenario": "吵架和好", "type": "共情", "content": "我知道我的话让你难过了，我真的不是故意的", "usage": "承认伤害+无意", "source": "自研原创", "emotion_level": 4, "tags": ["共情", "伤害", "无意"]},
    {"scenario": "吵架和好", "type": "表达", "content": "比起我们的矛盾，我更害怕失去你", "usage": "恐惧+珍视", "source": "小红书", "emotion_level": 5, "tags": ["表达", "恐惧", "珍视"]},
    {"scenario": "吵架和好", "type": "道歉", "content": "冷静下来想了想，我确实有些话说过头了。对不起", "usage": "冷静反思+道歉", "source": "自研原创", "emotion_level": 4, "tags": ["道歉", "冷静", "过头"]},
    {"scenario": "吵架和好", "type": "共情", "content": "你不需要为生气道歉，你有权利感到不开心", "usage": "允许情绪", "source": "自研原创", "emotion_level": 4, "tags": ["共情", "允许", "权利"]},
    {"scenario": "吵架和好", "type": "表达", "content": "我希望我们能好好聊聊，不是吵，是聊。因为我在乎你的想法", "usage": "邀请沟通+在乎", "source": "自研原创", "emotion_level": 4, "tags": ["表达", "沟通", "在乎"]},
    {"scenario": "吵架和好", "type": "道歉", "content": "我不该在你难过的时候还说那些话。你比我的自尊心重要多了", "usage": "具体认错+优先级", "source": "自研原创", "emotion_level": 5, "tags": ["道歉", "具体", "优先级"]},
    {"scenario": "吵架和好", "type": "共情", "content": "我明白你不是在无理取闹，你的感受是有道理的", "usage": "认可合理性", "source": "知乎", "emotion_level": 4, "tags": ["共情", "认可", "道理"]},
    {"scenario": "吵架和好", "type": "表达", "content": "我们可以有不同的看法，但这不影响我爱你/在乎你", "usage": "区分观点与感情", "source": "自研原创", "emotion_level": 4, "tags": ["表达", "观点", "感情"]},
    {"scenario": "吵架和好", "type": "道歉", "content": "我保证以后不会再这样了。你可以监督我", "usage": "承诺+邀请监督", "source": "自研原创", "emotion_level": 3, "tags": ["道歉", "承诺", "监督"]},
    {"scenario": "吵架和好", "type": "共情", "content": "谢谢你愿意告诉我你的感受，这说明你还在乎这段关系", "usage": "感谢+正向解读", "source": "自研原创", "emotion_level": 4, "tags": ["共情", "感谢", "正向"]},
    
    # ========== 拒绝（扩充到15条）==========
    {"scenario": "拒绝", "type": "体面", "content": "谢谢你这么欣赏我，但我现在不想谈恋爱。你的好我不会忘记的", "usage": "感谢+原因+肯定", "source": "自研原创", "emotion_level": 3, "tags": ["拒绝", "感谢", "体面"]},
    {"scenario": "拒绝", "type": "委婉", "content": "你是个很好的人，只是——我们可能不太合适", "usage": "肯定+不合适", "source": "知乎", "emotion_level": 2, "tags": ["拒绝", "肯定", "不合适"]},
    {"scenario": "拒绝", "type": "体面", "content": "我很珍惜我们现在的关系，不想让它变成别的样子", "usage": "珍惜+现状", "source": "自研原创", "emotion_level": 3, "tags": ["拒绝", "珍惜", "现状"]},
    {"scenario": "拒绝", "type": "委婉", "content": "你值得一个全心全意对你的人，而我现在给不了", "usage": "肯定对方+诚实", "source": "小红书", "emotion_level": 3, "tags": ["拒绝", "肯定", "诚实"]},
    {"scenario": "拒绝", "type": "体面", "content": "你的心意我收到了，真的很感动。但我没办法回应同样的感情", "usage": "感谢+诚实", "source": "自研原创", "emotion_level": 3, "tags": ["拒绝", "感谢", "诚实"]},
    {"scenario": "拒绝", "type": "委婉", "content": "我现在把重心放在自己身上，暂时没有精力经营一段关系", "usage": "自我聚焦+时机", "source": "知乎", "emotion_level": 2, "tags": ["拒绝", "自我", "时机"]},
    {"scenario": "拒绝", "type": "体面", "content": "我很感激你对我的好，但我不想给你错误的信号", "usage": "感谢+避免误导", "source": "自研原创", "emotion_level": 3, "tags": ["拒绝", "感谢", "信号"]},
    {"scenario": "拒绝", "type": "委婉", "content": "我觉得我们更适合做朋友，你觉得呢？", "usage": "重新定义关系", "source": "小红书", "emotion_level": 2, "tags": ["拒绝", "朋友", "重新定义"]},
    {"scenario": "拒绝", "type": "体面", "content": "你的勇敢让我很佩服，但我确实没有那种感觉", "usage": "赞美勇气+诚实", "source": "自研原创", "emotion_level": 3, "tags": ["拒绝", "赞美", "感觉"]},
    {"scenario": "拒绝", "type": "委婉", "content": "也许未来的某一天我们会合适，但不是现在", "usage": "未来可能性+现在否定", "source": "知乎", "emotion_level": 2, "tags": ["拒绝", "未来", "现在"]},
    {"scenario": "拒绝", "type": "体面", "content": "你很好，是我还没有准备好进入一段关系", "usage": "肯定对方+自我归因", "source": "自研原创", "emotion_level": 3, "tags": ["拒绝", "肯定", "准备"]},
    {"scenario": "拒绝", "type": "委婉", "content": "我不想耽误你，你值得更好的", "usage": "为对方着想", "source": "小红书", "emotion_level": 3, "tags": ["拒绝", "耽误", "更好"]},
    {"scenario": "拒绝", "type": "体面", "content": "谢谢你的喜欢，这是我收到过很珍贵的礼物", "usage": "肯定喜欢本身", "source": "自研原创", "emotion_level": 3, "tags": ["拒绝", "肯定", "珍贵"]},
    {"scenario": "拒绝", "type": "委婉", "content": "我对你没有那种心动的感觉，这是我最诚实的回答", "usage": "诚实+感觉", "source": "自研原创", "emotion_level": 3, "tags": ["拒绝", "诚实", "心动"]},
    {"scenario": "拒绝", "type": "体面", "content": "我很珍惜你这个人，所以不想用虚假的感情来回应你", "usage": "珍惜+真诚", "source": "自研原创", "emotion_level": 4, "tags": ["拒绝", "珍惜", "真诚"]},
    
    # ========== 表白（扩充到15条）==========
    {"scenario": "表白", "type": "真诚", "content": "我不知道该怎么说，但我想让你知道——跟你在一起的每一刻，我都觉得很幸福", "usage": "感受+幸福", "source": "自研原创", "emotion_level": 5, "tags": ["表白", "感受", "幸福"]},
    {"scenario": "表白", "type": "真诚", "content": "我喜欢你。不是随便说说的那种喜欢，是认真想过之后的那种", "usage": "认真+确认", "source": "知乎", "emotion_level": 5, "tags": ["表白", "认真", "确认"]},
    {"scenario": "表白", "type": "真诚", "content": "你愿意做我女朋友/男朋友吗？如果不能，我也希望你知道——你是我见过最好的人", "usage": "请求+无压力", "source": "自研原创", "emotion_level": 5, "tags": ["表白", "请求", "无压"]},
    {"scenario": "表白", "type": "表达", "content": "遇见你之前，我没想过恋爱。遇见你之后，我没想过别人", "usage": "对比+唯一性", "source": "小红书", "emotion_level": 5, "tags": ["表白", "对比", "唯一"]},
    {"scenario": "表白", "type": "真诚", "content": "我喜欢你的笑容，喜欢你的性格，喜欢你的一切。包括你的不完美", "usage": "全面赞美+接纳", "source": "自研原创", "emotion_level": 5, "tags": ["表白", "全面", "接纳"]},
    {"scenario": "表白", "type": "表达", "content": "我想和你一起经历生活中的每一件小事，大到旅行，小到吃一顿饭", "usage": "日常+陪伴", "source": "自研原创", "emotion_level": 4, "tags": ["表白", "日常", "陪伴"]},
    {"scenario": "表白", "type": "真诚", "content": "我不想再只做你的朋友了。我喜欢你，认真地、很久的那种", "usage": "关系升级+时间", "source": "知乎", "emotion_level": 5, "tags": ["表白", "升级", "时间"]},
    {"scenario": "表白", "type": "表达", "content": "你出现在我的生活里，一切都变得不一样了。变得更好了", "usage": "影响+正面变化", "source": "自研原创", "emotion_level": 4, "tags": ["表白", "影响", "变化"]},
    {"scenario": "表白", "type": "真诚", "content": "我喜欢你，不是因为你是谁，而是因为在你身边我是谁", "usage": "自我+对方", "source": "小红书", "emotion_level": 5, "tags": ["表白", "自我", "对方"]},
    {"scenario": "表白", "type": "表达", "content": "我想成为那个让你每天早上醒来都觉得开心的人", "usage": "愿景+开心", "source": "自研原创", "emotion_level": 4, "tags": ["表白", "愿景", "开心"]},
    {"scenario": "表白", "type": "真诚", "content": "我准备好了，准备好以恋人的身份站在你身边。你呢？", "usage": "准备+反问", "source": "自研原创", "emotion_level": 5, "tags": ["表白", "准备", "反问"]},
    {"scenario": "表白", "type": "表达", "content": "你是我唯一想分享所有事情的人，不管是开心的还是难过的", "usage": "唯一性+分享", "source": "自研原创", "emotion_level": 4, "tags": ["表白", "唯一", "分享"]},
    {"scenario": "表白", "type": "真诚", "content": "我喜欢你。你可以慢慢考虑，不用急着回答我", "usage": "表白+给空间", "source": "知乎", "emotion_level": 4, "tags": ["表白", "空间", "耐心"]},
    {"scenario": "表白", "type": "表达", "content": "我不想错过你。哪怕只有万分之一的可能，我也想试试", "usage": "决心+勇气", "source": "自研原创", "emotion_level": 5, "tags": ["表白", "决心", "勇气"]},
    {"scenario": "表白", "type": "真诚", "content": "你是我做过最好的决定——决定认识你", "usage": "回顾+肯定", "source": "自研原创", "emotion_level": 5, "tags": ["表白", "回顾", "肯定"]},
    
    # ========== 维系关系（扩充到15条）==========
    {"scenario": "维系关系", "type": "表达", "content": "谢谢你一直以来的陪伴，有你真好", "usage": "感谢+陪伴", "source": "自研原创", "emotion_level": 4, "tags": ["维系", "感谢", "陪伴"]},
    {"scenario": "维系关系", "type": "表达", "content": "不管多忙，我都想跟你说——我很在乎你", "usage": "忙碌+在乎", "source": "自研原创", "emotion_level": 4, "tags": ["维系", "忙碌", "在乎"]},
    {"scenario": "维系关系", "type": "行动", "content": "这周末我们去看那场你想看的电影吧？我订票", "usage": "记住喜好+行动", "source": "小红书", "emotion_level": 3, "tags": ["维系", "记住", "行动"]},
    {"scenario": "维系关系", "type": "表达", "content": "和你在一起的每一天，我都觉得是一种幸运", "usage": "幸运+日常", "source": "自研原创", "emotion_level": 4, "tags": ["维系", "幸运", "日常"]},
    {"scenario": "维系关系", "type": "表达", "content": "你最近有什么想要的吗？我想给你一个小惊喜", "usage": "关心+惊喜", "source": "知乎", "emotion_level": 3, "tags": ["维系", "关心", "惊喜"]},
    {"scenario": "维系关系", "type": "共情", "content": "我知道我们都有自己的生活，但你永远是我的优先级", "usage": "优先级+确认", "source": "自研原创", "emotion_level": 5, "tags": ["维系", "优先级", "确认"]},
    {"scenario": "维系关系", "type": "表达", "content": "谢谢你包容我的不完美，我会努力变得更好", "usage": "感谢+成长", "source": "自研原创", "emotion_level": 4, "tags": ["维系", "感谢", "成长"]},
    {"scenario": "维系关系", "type": "行动", "content": "我学了一道新菜，今晚做给你尝尝？", "usage": "行动+日常关怀", "source": "小红书", "emotion_level": 2, "tags": ["维系", "行动", "做菜"]},
    {"scenario": "维系关系", "type": "表达", "content": "和你在一起之后，我变成了更好的自己", "usage": "成长+感恩", "source": "自研原创", "emotion_level": 4, "tags": ["维系", "成长", "感恩"]},
    {"scenario": "维系关系", "type": "共情", "content": "不管发生什么，我都会一直在你身边。说到做到", "usage": "承诺+坚定", "source": "自研原创", "emotion_level": 5, "tags": ["维系", "承诺", "坚定"]},
    {"scenario": "维系关系", "type": "表达", "content": "我想和你一起变老，一起经历人生的每一个阶段", "usage": "长期愿景", "source": "知乎", "emotion_level": 5, "tags": ["维系", "长期", "愿景"]},
    {"scenario": "维系关系", "type": "行动", "content": "你上次说想看的那个展览这周末开幕，一起去吧", "usage": "记住+邀约", "source": "自研原创", "emotion_level": 3, "tags": ["维系", "记住", "邀约"]},
    {"scenario": "维系关系", "type": "表达", "content": "和你在一起的平淡日子，其实就是我想要的浪漫", "usage": "平淡+浪漫", "source": "自研原创", "emotion_level": 4, "tags": ["维系", "平淡", "浪漫"]},
    {"scenario": "维系关系", "type": "共情", "content": "我知道你最近很辛苦，让我来帮你分担一些", "usage": "观察+分担", "source": "自研原创", "emotion_level": 4, "tags": ["维系", "观察", "分担"]},
    {"scenario": "维系关系", "type": "表达", "content": "你是我做过最正确的决定，没有之一", "usage": "肯定+唯一", "source": "自研原创", "emotion_level": 5, "tags": ["维系", "肯定", "唯一"]},
]


def run():
    """运行大规模扩充"""
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
    
    # 合并已有数据和新数据
    all_scripts = scripts + NEW_SCRIPTS
    
    for script in all_scripts:
        if 'id' not in script:
            # 新话术没有ID，生成唯一ID
            import hashlib
            random_suffix = hashlib.md5(f"{script['content'][:50]}_{datetime.now().microsecond}_{random.random()}".encode()).hexdigest()[:8]
            script['id'] = f"EXPAND_{random_suffix}"
            script.setdefault('date_added', date_str)
        sid = script['id']
        if sid not in existing_ids:
            scripts.append(script)
            existing_ids.add(sid)
            added.append(sid)
    
    # 保存
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(scripts, f, ensure_ascii=False, indent=2)
    
    # 记录日志
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log_file = r"C:\Users\W\Z.Talk话术库\扩充日志.log"
    with open(log_file, 'a', encoding='utf-8') as f:
        f.write(f"\n{'='*60}\n")
        f.write(f"大规模扩充: {timestamp}\n")
        f.write(f"新增: {len(added)} 条\n")
        f.write(f"总计: {len(scripts)} 条\n")
        f.write(f"{'='*60}\n")
        for sid in added[:10]:
            f.write(f"  {sid}\n")
        if len(added) > 10:
            f.write(f"  ... 共 {len(added)} 条\n")
    
    # 更新心跳
    heartbeat = r"C:\Users\W\Z.Talk话术库\心跳.txt"
    with open(heartbeat, 'w', encoding='utf-8') as f:
        f.write(f"last_run: {timestamp}\n")
        f.write(f"status: success\n")
        f.write(f"added: {len(added)}\n")
        f.write(f"total: {len(scripts)}\n")
    
    print(f"✅ 新增: {len(added)} 条话术")
    print(f"💾 总话术数: {len(scripts)} 条")
    print(f"📊 目标: 200+ 条")
    if len(scripts) >= 200:
        print(f"🎉 目标达成！")
    else:
        remaining = 200 - len(scripts)
        print(f"⏳ 还需 {remaining} 条")
    
    return len(added)


if __name__ == '__main__':
    run()
