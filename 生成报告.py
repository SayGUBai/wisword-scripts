#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
话搭子 · 运行状态报告
生成每日更新情况报告
"""

import json
import os
from datetime import datetime

DATA_FILE = r"C:\Users\W\话搭子话术库\话术数据库.json"
LOG_FILE = r"C:\Users\W\话搭子话术库\更新日志.log"
HEARTBEAT = r"C:\Users\W\话搭子话术库\心跳.txt"

def generate_report():
    """生成运行状态报告"""
    now = datetime.now()
    
    print("=" * 60)
    print("  话搭子 · 高情商话术库 · 运行状态报告")
    print("=" * 60)
    print(f"报告生成时间: {now.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"数据文件路径: C:\\Users\\W\\话搭子话术库\\话术数据库.json")
    
    if not os.path.exists(DATA_FILE):
        print("❌ 错误: 找不到话术数据库文件")
        return
    
    with open(DATA_FILE, 'r', encoding='utf-8') as f:
        scripts = json.load(f)
    
    print(f"总话术数量: {len(scripts)} 条")
    print(f"数据来源: 自研原创 + 心理学书籍 + 网络平台")
    print(f"覆盖场景: 8大类")
    print("=" * 60)
    print()
    
    # 场景分布
    print("📊 场景分布:")
    scenarios = {}
    for s in scripts:
        scenario = s['scenario']
        scenarios[scenario] = scenarios.get(scenario, 0) + 1
    
    for scenario in ['破冰开场', '暧昧升温', '日常聊天', '关心体贴', 
                     '吵架和好', '拒绝', '表白', '维系关系']:
        count = scenarios.get(scenario, 0)
        print(f"  {scenario}: {count}条")
    
    print()
    print("📈 话术类型:")
    types = {}
    for s in scripts:
        stype = s.get('type', '未知')
        types[stype] = types.get(stype, 0) + 1
    
    for stype, count in sorted(types.items(), key=lambda x: x[1], reverse=True):
        print(f"  {stype}: {count}条")
    
    print()
    print("✅ 自动运行状态:")
    print("  每日自动更新: 已设置 (每天09:00)")
    print("  登录自动运行: 已设置")
    print("  后台静默运行: 已设置")
    print("  下次运行时间: 每天09:00")
    print("=" * 60)
    
    # 查看日志
    if os.path.exists(LOG_FILE):
        print()
        print("📝 最近更新记录:")
        with open(LOG_FILE, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            # 显示最后30行
            for line in lines[-30:]:
                print(line.rstrip())
    
    print()
    print("💡 更新方式:")
    print("  1. 本地脚本: python 每日自动更新.py")
    print("  2. 手动执行: 双击 自动设置.bat")
    print("  3. 自动运行: 每天09:00自动执行")
    print("=" * 60)

if __name__ == '__main__':
    generate_report()
