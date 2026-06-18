@echo off
REM ============================================
REM Z.Talk 智言 - 设置每日定时采集任务
REM 以管理员身份运行此脚本
REM ============================================

echo 正在创建 Windows 定时任务...
echo.

REM 每天早上9点自动运行采集
schtasks /create /tn "ZTalk智言_每日采集" /tr "python \"%~dp0多渠道采集.py\"" /sc daily /st 09:00 /f

REM 同时设置开机自启动（复制到启动文件夹）
copy "%~dp0开机自动采集.bat" "%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup\ZTalk采集.bat" /Y

echo.
echo ============================================
echo 设置完成!
echo.
echo 1. 每天 09:00 自动采集话术
echo 2. 开机时自动采集话术
echo.
echo 查看任务: schtasks /query /tn "ZTalk智言_每日采集"
echo 删除任务: schtasks /delete /tn "ZTalk智言_每日采集" /f
echo ============================================
pause
