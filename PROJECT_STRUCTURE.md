# 📁 PROJE YAPISI

```
cafe-pos/
│
├── 📄 README.md                    # Detaylı proje dokümantasyonu
├── 📄 QUICKSTART.md               # Hızlı başlangıç kılavuzu
├── 📄 .gitignore                  # Git ignore kuralları
├── 🔨 build.bat                   # Otomatik build scripti (WINDOWS)
├── 🔨 run-dev.bat                 # Geliştirme modu başlatıcı
│
├── 📂 backend/                    # Python Flask Backend
│   ├── 📄 app.py                  # Ana Flask uygulaması
│   ├── 📄 database.py             # Veritabanı yönetimi
│   ├── 📄 models.py               # İş mantığı katmanı
│   ├── 📄 requirements.txt        # Python bağımlılıkları
│   ├── 📄 build_backend.spec      # PyInstaller yapılandırması
│   │
│   ├── 📂 routes/                 # API Endpoint'leri
│   │   ├── __init__.py            # Route kaydedici
│   │   ├── tables.py              # Masa API'leri
│   │   ├── menu.py                # Menü API'leri
│   │   ├── orders.py              # Sipariş API'leri
│   │   └── reports.py             # Rapor API'leri
│   │
│   └── 📂 data/                   # Veritabanı klasörü (otomatik oluşur)
│       └── cafe.db                # SQLite veritabanı
│
└── 📂 frontend/                   # Electron Frontend
    ├── 📄 package.json            # Node.js yapılandırması
    │
    ├── 📂 src/
    │   ├── 📄 main.js             # Electron ana process
    │   ├── 📄 preload.js          # Güvenli IPC köprüsü
    │   │
    │   └── 📂 pages/              # HTML Sayfaları
    │       ├── index.html         # Ana ekran (40 masa)
    │       ├── table.html         # Masa detay & sipariş
    │       ├── menu-management.html  # Menü yönetimi
    │       └── reports.html       # Satış raporları
    │
    └── 📂 assets/                 # Görseller, ikonlar
        └── icon.png

```

## 🔄 Veri Akışı

```
[Kullanıcı Arayüzü]
         ↓
   [Electron UI]
         ↓
    HTTP Request
         ↓
   [Flask API]
         ↓
   [Model Layer]
         ↓
  [SQLite Database]
```

## 📊 API Endpoint'leri

### Masalar
- `GET    /api/tables/` - Tüm masalar
- `GET    /api/tables/:id` - Tek masa
- `POST   /api/tables/:id/open` - Masa aç
- `POST   /api/tables/:id/close` - Masa kapat

### Menü
- `GET    /api/menu/categories` - Kategoriler
- `POST   /api/menu/categories` - Kategori ekle
- `GET    /api/menu/products` - Ürünler
- `POST   /api/menu/products` - Ürün ekle
- `PUT    /api/menu/products/:id` - Ürün güncelle
- `DELETE /api/menu/products/:id` - Ürün sil

### Siparişler
- `GET    /api/orders/table/:id` - Masa siparişleri
- `POST   /api/orders/add` - Sipariş ekle
- `PUT    /api/orders/:id/quantity` - Adet güncelle
- `DELETE /api/orders/:id` - Sipariş sil

### Raporlar
- `GET    /api/reports/daily?date=YYYY-MM-DD` - Günlük rapor
- `GET    /api/reports/range?start_date=...&end_date=...` - Aralık raporu

## 🗂️ Veritabanı Tabloları

1. **tables** - 40 masa bilgisi
2. **categories** - Ürün kategorileri
3. **products** - Menü ürünleri
4. **active_orders** - Masalardaki aktif siparişler
5. **completed_sales** - Tamamlanmış satışlar
6. **sale_details** - Satış detayları

## 🎨 UI Ekranları

### 1. Ana Ekran (index.html)
- 40 masanın grid görünümü
- Renk kodlu durum gösterimi
- Menü yönetimi linki
- Raporlar linki

### 2. Masa Detay (table.html)
- Sol panel: Kategori filtreli menü
- Sağ panel: Adisyon listesi
- Adet kontrolü (+/-)
- Ürün silme
- Nakit/Kart ödeme

### 3. Menü Yönetimi (menu-management.html)
- Ürün ekleme formu
- Ürün listesi tablosu
- Düzenleme/Silme işlemleri

### 4. Raporlar (reports.html)
- Tarih seçici
- Özet kartları (satış, ciro, nakit, kart)
- Ürün bazlı tablo
- Kategori bazlı tablo

## 🔐 Güvenlik

- ✅ Context isolation aktif
- ✅ Node integration kapalı
- ✅ Preload script ile güvenli IPC
- ✅ SQL injection koruması (parameterized queries)
- ✅ Local-only backend (127.0.0.1)
- ✅ CORS sadece local origin

## 🚀 Build Süreci

1. **Backend Build:**
   ```
   PyInstaller → cafe_backend.exe
   ```

2. **Frontend Build:**
   ```
   electron-builder → Kafe POS Setup.exe
   (Backend exe'yi içine gömer)
   ```

3. **Final Package:**
   ```
   Setup.exe → Install → Desktop Shortcut
   ```

## 📦 Deployment Checklist

- [x] Backend exe test edildi
- [x] Frontend standalone çalışıyor
- [x] Veritabanı otomatik oluşuyor
- [x] Port çakışması kontrolü var
- [x] Hata yönetimi implementasyonu
- [x] Kullanıcı dokümantasyonu hazır
- [x] Build script'leri çalışıyor
