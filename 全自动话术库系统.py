#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Z.Talk · 全自动话术库系统 - 主程序
自动运行，无需人工干预
"""

import json
import os
import time
from datetime import datetime

# ==================== 配置 ====================
ROOT_DIR = r"C:\Users\W\Z.Talk话术库"
DATA_FILE = os.path.join(ROOT_DIR, "话术数据库.json")
LOG_FILE = os.path.join(ROOT_DIR, "更新日志.log")
CHECKPOINT_FILE = os.path.join(ROOT_DIR, "checkpoint.json")
HEARTBEAT_FILE = os.path.join(ROOT_DIR, "heartbeat.txt")

# 自动运行配置
RUN_INTERVAL_MINUTES = 6  # 每6小时检查一次
MAX_DAILY_UPDATES = 10    # 每日最多新增10条


def load_scripts():
    """加载话术"""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []


def save_scripts(scripts):
    """保存话术"""
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(scripts, f, ensure_ascii=False, indent=2)


def check_and_update():
    """检查并更新话术库"""
    scripts = load_scripts()
    existing_ids = set(s['id'] for s in scripts)
    
    # 导入话术数据
    from scripts_data import SCRIPTS
    
    # 添加新话术
    added = []
    for script in SCRIPTS:
        if script['id'] not in existing_ids:
            scripts.append(script)
            added.append(script['id'])
            existing_ids.add(script['id'])
    
    if added:
        save_scripts(scripts)
        log_update(added)
        return added
    return []


def check_daily_update():
    """检查是否需要每日更新"""
    if not os.path.exists(CHECKPOINT_FILE):
        create_checkpoint()
        return True
    
    with open(CHECKPOINT_FILE, 'r', encoding='utf-8') as f:
        checkpoint = json.load(f)
    
    today = datetime.now().strftime('%Y-%m-%d')
    if checkpoint.get('date') != today:
        create_checkpoint()
        return True
    return False


def create_checkpoint():
    """创建检查点"""
    checkpoint = {
        'date': datetime.now().strftime('%Y-%m-%d'),
        'total_scripts': len(load_scripts()) if os.path.exists(DATA_FILE) else 0,
        'last_update': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    with open(CHECKPOINT_FILE, 'w', encoding='utf-8') as f:
        json.dump(checkpoint, f, ensure_ascii=False, indent=2)


def log_update(added):
    """记录更新日志"""
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    with open(LOG_FILE, 'a', encoding='utf-8') as f:
        f.write(f"\n{'='*60}\n")
        f.write(f"更新日志: {timestamp}\n")
        f.write(f"新增话术: {len(added)} 条\n")
        f.write(f"ID列表: {', '.join(added[:10])}\n")
        if len(added) > 10:
            f.write(f"  ... 还有 {len(added) - 10} 条\n")
        f.write(f"{'='*60}\n")


def update_heartbeat():
    """更新心跳文件"""
    with open(HEARTBEAT_FILE, 'w', encoding='utf-8') as f:
        f.write(f"last_run: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"status: running\n")
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, 'r', encoding='utf-8') as df:
                scripts = json.load(df)
            f.write(f"total_scripts: {len(scripts)}\n")


def run():
    """主运行函数"""
    # 确保目录存在
    os.makedirs(ROOT_DIR, exist_ok=True)
    
    # 更新心跳
    update_heartbeat()
    
    # 检查并更新
    added = check_and_update()
    
    # 检查每日更新
    if check_daily_update():
        # 每日额外添加一些话术
        daily_scripts = [
            {"id": f"DAILY_{datetime.now().strftime('%Y%m%d')}_{i}", "scenario": "日常聊天", "type": "关心", 
             "content": f"今日话术示例{i+1}", "usage": "日常关心", "source": "自动更新", 
             "emotion_level": 2, "gender": "通用", "tags": ["日常", "关心", "自动"]}
            for i in range(3)
        ]
        scripts = load_scripts()
        existing_ids = set(s['id'] for s in scripts)
        for ds in daily_scripts:
            if ds['id'] not in existing_ids:
                scripts.append(ds)
                added.append(ds['id'])
        save_scripts(scripts)
        log_update(added)
    
    # 更新心跳（包含最新数据）
    update_heartbeat()
    
    # 输出统计
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            scripts = json.load(f)
        print(f"[{datetime.now().strftime('%H:%M:%S')}] 话术库运行正常 | 总话术: {len(scripts)} | 今日新增: {len(added)}")
    else:
        print(f"[{datetime.now().strftime('%H:%M:%S')}] 话术库运行正常 | 今日新增: {len(added)}")
    
    return len(added)


if __name__ == '__main__':
    # 配置参数
    MINUTES_BETWEEN_RUNS = 6  # 每6小时运行一次
    
    print("="*60)
    print("  Z.Talk · 全自动话术库系统")
    print("="*60)
    print(f"  数据目录: {ROOT_DIR}")
    print(f"  运行间隔: 每{MINUTES_BETWEEN_RUNS}小时")
    print(f"  启动时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("="*60)
    
    # 首次运行
    added = run()
    if added:
        print(f"\n✅ 首次运行成功，新增 {len(added)} 条话术")
    else:
        print("\n✅ 首次运行成功，无新增话术")
    
    print(f"\n💡 系统将每{MINUTES_BETWEEN_RUNS}小时自动检查并更新")
    print("💡 后台静默运行，无需人工干预")
    print("="*60)
    
    # 持续运行
    try:
        while True:
            time.sleep(MINUTES_BETWEEN_RUNS * 60)
            added = run()
            if added:
                print(f"\n[{datetime.now().strftime('%H:%M:%S')}] 自动更新: 新增 {len(added)} 条话术")
    except KeyboardInterrupt:
        print("\n\n程序已停止")
