@echo off
echo ============================================
echo   KAFE POS - EXE BUILDER
echo ============================================
echo.

echo [1/5] Gerekli klasorleri olusturuluyor...
if not exist "backend\dist" mkdir backend\dist
if not exist "frontend\assets" mkdir frontend\assets
if not exist "frontend\backend\dist" mkdir frontend\backend\dist
echo   Klasorler hazir!

echo.
echo [2/5] Backend bagimliliklari kontrol ediliyor...
cd backend
pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo HATA: Backend bagimliliklari yuklenemedi!
    pause
    exit /b 1
)

echo.
echo [3/5] Backend exe olusturuluyor...
pyinstaller build_backend.spec
if %errorlevel% neq 0 (
    echo HATA: Backend exe olusturulamadi!
    pause
    exit /b 1
)

echo.
echo [4/5] Backend exe frontend'e kopyalaniyor...
copy dist\cafe_backend.exe ..\frontend\backend\dist\cafe_backend.exe
if %errorlevel% neq 0 (
    echo UYARI: Backend exe kopyalanamadi, manuel kopyalayiniz!
)

echo.
echo [5/5] Frontend exe olusturuluyor...
cd ..\frontend
call npm install
if %errorlevel% neq 0 (
    echo HATA: Frontend bagimliliklari yuklenemedi!
    pause
    exit /b 1
)

call npm run build:win
if %errorlevel% neq 0 (
    echo HATA: Frontend exe olusturulamadi!
    pause
    exit /b 1
)

echo.
echo ============================================
echo   BUILD TAMAMLANDI!
echo ============================================
echo.
echo Installer konumu: frontend\dist\Kafe POS Setup.exe
echo.
pause
