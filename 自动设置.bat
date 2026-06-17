@echo off
REM 话搭子 · 自动设置脚本
REM 双击此文件即可设置每日自动运行

echo ============================================================
echo   话搭子 · 自动话术库设置
echo ============================================================
echo.

REM 检查Python是否可用
where python >nul 2>&1
if %errorlevel% neq 0 (
    echo [错误] 未找到Python，请先安装Python
    pause
    exit /b 1
)

echo [1/3] 正在创建每日自动更新任务...
schtasks /create /tn "话搭子_每日更新" /tr "python C:\Users\W\话搭子话术库\每日自动更新.py" /sc daily /st 09:00 /ru SYSTEM /f

if %errorlevel% equ 0 (
    echo [成功] 已创建每日早上9:00自动更新任务
) else (
    echo [失败] 创建任务失败，请以管理员身份运行此脚本
)

echo.
echo [2/3] 正在创建启动时自动运行任务...
schtasks /create /tn "话搭子_启动运行" /tr "python C:\Users\W\话搭子话术库\每日自动更新.py" /sc onlogon /ru %USERNAME% /f

if %errorlevel% equ 0 (
    echo [成功] 已创建用户登录时自动运行任务
) else (
    echo [失败] 创建登录任务失败
)

echo.
echo [3/3] 正在测试运行...
cd /d "C:\Users\W\话搭子话术库"
python 每日自动更新.py

echo.
echo ============================================================
echo   设置完成！
echo   - 每天 09:00 自动更新话术
echo   - 登录时自动运行一次
echo   - 所有更新记录保存在日志文件中
echo ============================================================
echo.
pause
