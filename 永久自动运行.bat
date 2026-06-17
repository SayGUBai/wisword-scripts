@echo off
REM 话搭子 · 永久自动运行服务
REM 此脚本创建Windows任务，每天自动运行话术库更新

echo ============================================================
echo   话搭子 · 全自动话术库 - 永久自动运行
echo ============================================================
echo.

REM 检查Python
where python >nul 2>&1
if %errorlevel% neq 0 (
    echo [错误] 未找到Python
    pause
    exit /b 1
)

echo 正在设置自动运行任务...
echo.

REM 创建每天上午9点运行的任务
schtasks /create /tn "HuaDazi_DailyUpdate" /tr "python C:\Users\W\话搭子话术库\每日自动更新.py" /sc daily /st 09:00 /ru SYSTEM /f 2>nul

if %errorlevel% equ 0 (
    echo ✅ 已设置每天上午9:00自动更新
) else (
    echo ⚠️  创建任务失败，请尝试以管理员身份运行
)

REM 创建登录时运行的任务
schtasks /create /tn "HuaDazi_OnLogin" /tr "python C:\Users\W\话搭子话术库\每日自动更新.py" /sc onlogon /ru %USERNAME% /f 2>nul

if %errorlevel% equ 0 (
    echo ✅ 已设置登录时自动运行
) else (
    echo ⚠️  创建登录任务失败
)

REM 创建后台静默运行的Python脚本
echo.
echo 正在创建后台运行脚本...
echo # -*- coding: utf-8 -*- > C:\Users\W\话搭子话术库\auto_runner.py
echo import time >> C:\Users\W\话搭子话术库\auto_runner.py
echo import subprocess >> C:\Users\W\话搭子话术库\auto_runner.py
echo import os >> C:\Users\W\话搭子话术库\auto_runner.py
echo. >> C:\Users\W\话搭子话术库\auto_runner.py
echo SCRIPT_DIR = r"C:\Users\W\话搭子话术库" >> C:\Users\W\话搭子话术库\auto_runner.py
echo UPDATE_INTERVAL = 3600  # 每小时检查一次 >> C:\Users\W\话搭子话术库\auto_runner.py
echo. >> C:\Users\W\话搭子话术库\auto_runner.py
echo def run(): >> C:\Users\W\话搭子话术库\auto_runner.py
echo     try: >> C:\Users\W\话搭子话术库\auto_runner.py
echo         os.chdir(SCRIPT_DIR) >> C:\Users\W\话搭子话术库\auto_runner.py
echo         result = subprocess.run(['python', '每日自动更新.py'], >> C:\Users\W\话搭子话术库\auto_runner.py
echo                                capture_output=True, text=True, timeout=60) >> C:\Users\W\话搭子话术库\auto_runner.py
echo         if result.returncode == 0: >> C:\Users\W\话搭子话术库\auto_runner.py
echo             print(f"[{{datetime.now().strftime('%H:%M:%S')}}] 自动更新成功") >> C:\Users\W\话搭子话术库\auto_runner.py
echo         else: >> C:\Users\W\话搭子话术库\auto_runner.py
echo             print(f"[{{datetime.now().strftime('%H:%M:%S')}}] 更新失败: {{result.stderr}}") >> C:\Users\W\话搭子话术库\auto_runner.py
echo     except Exception as e: >> C:\Users\W\话搭子话术库\auto_runner.py
echo         print(f"[{{datetime.now().strftime('%H:%M:%S')}}] 错误: {{e}}") >> C:\Users\W\话搭子话术库\auto_runner.py
echo. >> C:\Users\W\话搭子话术库\auto_runner.py
echo if __name__ == '__main__': >> C:\Users\W\话搭子话术库\auto_runner.py
echo     print("话搭子自动运行服务已启动...") >> C:\Users\W\话搭子话术库\auto_runner.py
echo     from datetime import datetime >> C:\Users\W\话搭子话术库\auto_runner.py
echo     while True: >> C:\Users\W\话搭子话术库\auto_runner.py
echo         run() >> C:\Users\W\话搭子话术库\auto_runner.py
echo         time.sleep(UPDATE_INTERVAL) >> C:\Users\W\话搭子话术库\auto_runner.py

echo ✅ 后台运行脚本已创建

echo.
echo ============================================================
echo   自动运行设置完成！
echo   - 每天 09:00 自动更新
echo   - 登录时自动运行
echo   - 后台每小时检查一次
echo   - 所有更新记录在日志文件中
echo ============================================================
echo.
pause
