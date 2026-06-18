@echo off
REM ============================================
REM Z.Talk 智言 - 开机自动采集话术
REM 将此文件放入 Windows 启动文件夹即可开机自运行
REM 启动文件夹路径: shell:startup
REM ============================================

cd /d "%~dp0"
echo [%date% %time%] 开机自动采集开始... >> 采集日志.log

REM 延迟30秒等待网络连接
timeout /t 30 /nobreak > nul

REM 运行采集脚本
python 多渠道采集.py >> 采集日志.log 2>&1

echo [%date% %time%] 采集完成 >> 采集日志.log
