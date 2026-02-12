@echo off
echo ============================================
echo   BACKEND TEST
echo ============================================
echo.

cd backend

echo Python kontrol...
python --version
if %errorlevel% neq 0 (
    echo HATA: Python bulunamadi!
    pause
    exit /b 1
)

echo.
echo Bagimliliklari yukle...
pip install -r requirements.txt

echo.
echo Backend baslatiliyor...
echo Port: 5000
echo.
echo TARAYICIDA AC: http://127.0.0.1:5000
echo CTRL+C ile durdurun
echo.

python app.py

pause
