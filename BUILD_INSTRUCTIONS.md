# 🚀 ADIM ADIM KURULUM REHBERİ

## ÖNEMLİ NOTLAR

Bu dosya, projeyi sıfırdan build etmek için gerekli **tüm adımları** içerir.

---

## 📋 GEREKSİNİMLER

### 1. Python 3.8+ Kurulumu

**İndirme:** https://www.python.org/downloads/

**Kurulum sırasında:**
- ✅ "Add Python to PATH" seçeneğini işaretleyin
- ✅ "Install for all users" önerilir

**Kontrol:**
```bash
python --version
# Çıktı: Python 3.8.x veya üzeri olmalı
```

### 2. Node.js 16+ Kurulumu

**İndirme:** https://nodejs.org/

**Kurulum sırasında:**
- ✅ "Add to PATH" otomatik yapılır
- ✅ "Tools for Native Modules" seçeneğini işaretleyin

**Kontrol:**
```bash
node --version
npm --version
```

---

## 🔧 ADIM ADIM BUILD SÜRECİ

### Otomatik Build (Önerilen)

1. Proje klasörünü açın
2. `build.bat` dosyasına **çift tıklayın**
3. 5-10 dakika bekleyin
4. `frontend/dist/Kafe POS Setup.exe` oluşur

---

### Manuel Build (Detaylı)

#### ADIM 1: Backend Build

```bash
# 1.1 Backend klasörüne gidin
cd backend

# 1.2 Sanal ortam oluşturun (opsiyonel)
python -m venv venv
venv\Scripts\activate

# 1.3 Bağımlılıkları yükleyin
pip install -r requirements.txt

# 1.4 Backend exe'yi oluşturun
pyinstaller build_backend.spec

# 1.5 Çıktı kontrolü
dir dist\cafe_backend.exe
```

**Beklenen çıktı:** `backend/dist/cafe_backend.exe` (~15-20 MB)

---

#### ADIM 2: Backend'i Frontend'e Kopyalama

**ÇOK ÖNEMLİ!** Bu adımı atlamayın:

```bash
# Proje ana klasöründe:
mkdir frontend\backend\dist
copy backend\dist\cafe_backend.exe frontend\backend\dist\
```

**Kontrol:**
```bash
dir frontend\backend\dist\cafe_backend.exe
```

---

#### ADIM 3: Frontend Build

```bash
# 3.1 Frontend klasörüne gidin
cd frontend

# 3.2 Node paketlerini yükleyin
npm install

# 3.3 Windows installer'ı oluşturun
npm run build:win
```

**Süre:** 3-5 dakika

**Beklenen çıktı:**
- `frontend/dist/Kafe POS Setup.exe` (~100-150 MB)
- `frontend/dist/win-unpacked/` (unpacked dosyalar)

---

## ✅ BUILD SONRASI KONTROL

### Test: Geliştirme Modunda Çalıştırma

```bash
# Ana klasörde
run-dev.bat
```

**Beklenen davranış:**
1. Backend console açılır
2. "Flask sunucusu başlatılıyor - Port: 5000" görürsünüz
3. 3 saniye sonra Electron penceresi açılır
4. Masalar yüklenir

### Test: Production EXE

```bash
# Setup'ı çalıştırın
frontend\dist\Kafe POS Setup.exe
```

**Beklenen davranış:**
1. Installer açılır
2. Kurulum konumu seçilir
3. Desktop shortcut oluşturulur
4. Program başlatılır

---

## 🐛 SORUN GİDERME

### "Python bulunamadı"
**Çözüm:**
1. Python'u yeniden kurun
2. "Add to PATH" seçeneğini işaretleyin
3. Bilgisayarı yeniden başlatın

### "npm tanınmıyor"
**Çözüm:**
1. Node.js'i yeniden kurun
2. Bilgisayarı yeniden başlatın

### "PyInstaller bulunamadı"
**Çözüm:**
```bash
pip install pyinstaller
```

### "Backend exe oluşmadı"
**Kontrol edin:**
```bash
cd backend
dir dist
```

**Yoksa:**
```bash
pip install --upgrade pyinstaller
pyinstaller build_backend.spec
```

### "Frontend build hatası"
**Çözüm:**
```bash
cd frontend
rmdir /s /q node_modules
npm cache clean --force
npm install
npm run build:win
```

### "Backend başlamıyor"
**Kontrol:**
1. Port 5000 meşgul mü?
2. Firewall backend.exe'yi engelliyor mu?

**Test:**
```bash
cd backend
python app.py
# Tarayıcıda: http://127.0.0.1:5000
```

---

## 📂 DOSYA YAPISI (Build Sonrası)

```
cafe-pos/
├── backend/
│   ├── dist/
│   │   └── cafe_backend.exe  ✅ Backend exe
│   └── data/
│       └── cafe.db            (runtime'da oluşur)
│
└── frontend/
    ├── backend/dist/
    │   └── cafe_backend.exe   ✅ Kopyalanmış backend
    └── dist/
        └── Kafe POS Setup.exe ✅ Final installer
```

---

## 🎯 DAĞITIM

### Son Kullanıcıya Teslim

**Tek dosya göndermeniz yeterli:**
```
frontend/dist/Kafe POS Setup.exe
```

Kullanıcı:
1. Setup'ı çalıştırır
2. Kurulum konumu seçer
3. Desktop icon'a tıklar
4. Program çalışır!

**Gereksinimler (kullanıcı için):**
- Windows 10/11
- Yönetici yetkisi (kurulum için)
- 500 MB boş disk alanı

---

## 🔄 GÜNCELLEMELERİ DAĞITMA

1. Kodda değişiklik yapın
2. `build.bat` çalıştırın
3. Yeni `Kafe POS Setup.exe` oluşur
4. Bunu kullanıcılara gönderin
5. Eski sürüm üzerine kurabilirler

**Veritabanı korunur** - `backend/data/cafe.db` kurulumlar arasında saklanır

---

## 📊 BUILD SÜRELERİ

- Backend exe: **2-3 dakika**
- Frontend install: **1-2 dakika**
- Frontend build: **3-5 dakika**
- **Toplam: 6-10 dakika**

---

## 💡 İLERİ SEVİYE

### Sadece Backend Güncelleme

```bash
cd backend
pyinstaller build_backend.spec
copy dist\cafe_backend.exe ..\frontend\backend\dist\
cd ..\frontend
npm run build:win
```

### Sadece Frontend Güncelleme

```bash
cd frontend
# UI değişiklikleri yap
npm run build:win
```

### Versiyonlama

`package.json` içinde:
```json
"version": "1.0.0"  // Her release'de artırın
```

---

## 🆘 HATA LOGLARI

### Backend Logları
Development:
```bash
cd backend
python app.py
# Console'da loglar görünür
```

Production:
- Kullanıcı AppData klasöründe loglar olabilir

### Frontend Logları
Development:
- Electron console (Ctrl+Shift+I)
- Terminal output

---

## ✅ BAŞARI KRİTERLERİ

Build başarılı sayılır eğer:

1. ✅ `backend/dist/cafe_backend.exe` var
2. ✅ `frontend/backend/dist/cafe_backend.exe` var
3. ✅ `frontend/dist/Kafe POS Setup.exe` var
4. ✅ Setup çalıştırılıp program açılıyor
5. ✅ Masalar yükleniyor
6. ✅ Backend otomatik başlıyor/kapanıyor

---

**Başarılar!** 🎉
