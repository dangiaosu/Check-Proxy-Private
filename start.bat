@echo off
chcp 65001 >nul

:: Tiêu đề
echo ============================================
echo   Kiểm tra và chạy Proxy Checker
echo   by Đan Giáo Sư vs ChatGPT
echo ============================================

:: Kiểm tra Python đã cài đặt chưa
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python chưa được cài đặt. Vui lòng tải và cài đặt Python từ https://www.python.org/downloads/
    pause
    exit /b
)

:: Kiểm tra kết nối mạng
echo Kiểm tra kết nối mạng...
ping 8.8.8.8 -n 1 >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Không có kết nối mạng. Vui lòng kiểm tra lại.
    pause
    exit /b
)

:: Danh sách các thư viện cần thiết
set LIBS=aiohttp asyncio pandas colorama openpyxl

:: Kiểm tra và cài đặt từng thư viện
echo Kiểm tra và cài đặt các thư viện cần thiết...
for %%L in (%LIBS%) do (
    python -c "import %%L" >nul 2>&1
    if errorlevel 1 (
        echo [INFO] Thiếu thư viện %%L. Tiến hành cài đặt...
        pip install %%L
        if errorlevel 1 (
            echo [ERROR] Lỗi khi cài đặt thư viện %%L. Vui lòng kiểm tra lại pip hoặc kết nối mạng.
            pause
            exit /b
        )
    )
)

:: Chạy script Python
echo [INFO] Tất cả điều kiện đã sẵn sàng. Chạy chương trình...
python check.py
if errorlevel 1 (
    echo [ERROR] Lỗi khi chạy chương trình. Vui lòng kiểm tra lại code Python.
    pause
    exit /b
)

:: Kết thúc
echo [INFO] Chương trình đã hoàn tất. Nhấn phím bất kỳ để thoát...
pause
exit /b
