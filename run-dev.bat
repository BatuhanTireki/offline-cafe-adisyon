@echo off
echo ============================================
echo   KAFE POS - GELISTIRME MODU
echo ============================================
echo.

echo Python kontrol ediliyor...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo HATA: Python bulunamadi! Lutfen Python yukleyin.
    pause
    exit /b 1
)

echo Node.js kontrol ediliyor...
node --version >nul 2>&1
if %errorlevel% neq 0 (
    echo HATA: Node.js bulunamadi! Lutfen Node.js yukleyin.
    pause
    exit /b 1
)

echo.
echo Backend baslatiiliyor...
start "Backend Server" cmd /k "cd backend && python app.py"

timeout /t 5 /nobreak > nul

echo.
echo Frontend baslatiiliyor...
cd frontend
call npm start

pause
