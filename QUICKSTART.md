# 🚀 HIZLI BAŞLANGIÇ KILAVUZU

## Windows için Tek Tıkla EXE Oluşturma

### Gereksinimler
1. Python 3.8+ kurulu olmalı
2. Node.js 16+ kurulu olmalı
3. Git kurulu olmalı (opsiyonel)

---

## ADIM 1: Projeyi İndirin

```bash
# Git ile (önerilir)
git clone <repository-url>
cd cafe-pos

# VEYA ZIP indir ve çıkar
```

---

## ADIM 2: Tek Komutla Build

**build.bat dosyasına çift tıklayın!**

Bu dosya otomatik olarak:
✅ Backend bağımlılıklarını yükler
✅ Backend exe'yi oluşturur
✅ Frontend bağımlılıklarını yükler
✅ Frontend installer'ı oluşturur

**Süre:** ~5-10 dakika

---

## ADIM 3: Uygulamayı Çalıştırın

Build tamamlandıktan sonra:

1. `frontend/dist/Kafe POS Setup.exe` dosyasını çalıştırın
2. Kurulum sihirbazını takip edin
3. Masaüstü kısayolu oluşturulur
4. Programı başlatın!

---

## Geliştirme Modu

Test ve geliştirme için:

**run-dev.bat dosyasına çift tıklayın!**

Bu mod:
- Backend'i Python ile çalıştırır
- Frontend'i development modda açar
- DevTools açık gelir
- Hot reload aktif

---

## Manuel Build (İleri Seviye)

### Backend EXE

```bash
cd backend
pip install -r requirements.txt
pyinstaller build_backend.spec
```

Çıktı: `backend/dist/cafe_backend.exe`

### Frontend Installer

```bash
cd frontend
npm install
npm run build:win
```

Çıktı: `frontend/dist/Kafe POS Setup.exe`

---

## Sorun Giderme

### "Python bulunamadı" hatası
- Python'u PATH'e ekleyin
- VEYA komut satırında: `python --version`

### "npm tanınmıyor" hatası
- Node.js'i yeniden kurun
- "Add to PATH" seçeneğini işaretleyin

### Build başarısız
1. Tüm terminalleri kapatın
2. `backend/dist` ve `frontend/dist` klasörlerini silin
3. `build.bat`'ı yeniden çalıştırın

---

## Kullanım Akışı

1. **İlk Açılış**
   - Program otomatik veritabanı oluşturur
   - 40 masa ve örnek menü hazır gelir

2. **Masa Açma**
   - Yeşil (boş) masaya tıklayın
   - Masa otomatik "dolu" olur

3. **Sipariş Verme**
   - Sol panelden ürünlere tıklayın
   - Sağ panelde sipariş görünür
   - +/- ile adet değiştirin

4. **Ödeme Alma**
   - "Nakit" veya "Kart" butonuna tıklayın
   - Masa otomatik kapanır
   - Satış kaydedilir

5. **Raporlama**
   - Ana ekrandan "Raporlar"a gidin
   - Tarih seçin
   - Detaylı rapor görün

---

## İlk Kullanım İpuçları

✅ Menü Yönetimi'nden kendi ürünlerinizi ekleyin
✅ Kategori bazlı organize edin
✅ Fiyatları düzenli güncelleyin
✅ Her gün sonunda rapor alın
✅ Veritabanını düzenli yedekleyin (`backend/data/cafe.db`)

---

## Destek

📧 E-posta: support@cafepos.com
📚 Dokümantasyon: README.md
🐛 Hata bildirimi: GitHub Issues

---

**Başarılar!** ☕
