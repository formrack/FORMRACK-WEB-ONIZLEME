# Formrack 3D Model Viewer - Quick Start Guide

## 🚀 BAŞLAMA (Turkish / English)

### Windows
1. **`RUN-SERVER.bat` dosyasına çift tıkla**
2. Browser'da aç: **http://localhost:8000**

### macOS / Linux
```bash
chmod +x start-server.sh
./start-server.sh
```

---

## 📂 MODEL EKLEME

**3D modellerini `models/` klasörüne koy:**

```
FORMRACK-WEB-ONIZLEME/
└── models/
    ├── Hazır Sahne.glb          ← (zaten var)
    ├── yeni-model.glb           ← Buraya ekle
    ├── urun-1.glb               ← Buraya ekle
    └── tasarim-v2.glb           ← Buraya ekle
```

**Sayfayı yenile → Dropdown'da otomatik görünecek!**

---

## ✨ NASIL KULLANILIR

### Dropdown Seçme
- Sağ alttaki **Seç** dropdown'undan model seç
- Model otomatik yüklenecek

### Upload Butonu
- Sağ üstteki **⬆** butonuna tıkla
- Bilgisayardan `.glb` veya `.gltf` dosya seç
- Yükleme ve önizleme başlayacak

### 3D Kontroller
- **Drag (Sürükle)** = Döndür (Rotate)
- **Scroll** = Yaklaştır/Uzaklaştır (Zoom)
- **Sağ Tıkla + Drag** = Pan (Hareket)

---

## 📋 DESTEKLENEN FORMAT

✅ `.glb` - Binary GLTF (Önerilen)
✅ `.gltf` - Text GLTF

---

## 🔍 SOL BAŞTAKI AYARLAR

**Sağ üstte:**
- Model seçici dropdown
- Dosya yükleme butonu

**Sol altta:**
- Formrack başlığı
- Ürün bilgileri

---

## 🐛 SORUN GIDERİP

### Models görünmüyor
- Sayfayı yenile: `F5` veya `Ctrl+R`
- Browser console'u açı: `F12` → Console
- Hataları oku ve rapor et

### Upload çalışmıyor
- Dosya `.glb` veya `.gltf` formatında olmalı
- Dosya boyutu çok büyük değilse kontrol et

### Server başlamıyor
- Python kurulu mu? `python --version`
- Başka bir programın port 8000'ü kullanıyor mu?

---

## 📦 API ENDPOINT

Modelleri programatik olarak almak:
```
http://localhost:8000/api/models
```

Sonuç:
```json
{
  "models": [
    {
      "id": 1,
      "name": "Hazır Sahne",
      "filename": "Hazır Sahne.glb",
      "description": "3D Ürün Modeli",
      "size": 2048576
    }
  ],
  "total": 1
}
```

---

## 🌐 CANLIYA ALMAK

Sunucuya yüklendikten sonra production web server kullan:
- Nginx
- Apache
- Node.js
- Python Gunicorn

---

## 📞 DESTEK

Sorularınız için: **support@formrack.com**

---

**Made with ❤️ for Formrack**
