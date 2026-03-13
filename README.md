# Formrack 3D Model Viewer

Profesyonel B2B websitesi için WebGL tabanlı 3D ürün önizleme sistemi.

## 📁 Proje Yapısı

```
FORMRACK-WEB-ONIZLEME/
├── index.html              # Ana sayfa
├── models.json             # Model metadata (yedek)
├── server.py               # Python sunucu (otomatik tarama)
├── start-server.bat        # Windows başlatıcı
├── start-server.sh         # Linux/Mac başlatıcı
└── models/                 # 3D model klasörü
    ├── model1.glb
    ├── model2.glb
    └── ...
```

## 🚀 Başlangıç

### Windows
1. **Çift tıkla**: `start-server.bat`
2. Browser'da aç: `http://localhost:8000`

### macOS / Linux
```bash
chmod +x start-server.sh
./start-server.sh
```

Veya direkt Python:
```bash
python3 server.py
```

## 📦 Model Ekleme

1. `.glb` veya `.gltf` dosyasını **`models/`** klasörüne koy
2. Sayfayı yenile
3. Dropdown menüde model otomatik görünecek
4. Seç ve 3D önizlemesini gör

**Örnek:**
```
models/
├── urun-1.glb
├── urun-2.glb
└── ozel-tasarim.glb
```

## ✨ Özellikler

✅ **Otomatik Model Taraması** - `models/` klasöründeki dosyaları dinamik olarak yükler  
✅ **Upload & Select** - Dosya yükle veya dropdown'dan seç  
✅ **360° Interaktif** - Drag (döndür), Scroll (zoom), Right-click (pan)  
✅ **Auto-Rotate** - Otomatik dönerken inceleme imkanı  
✅ **Mobil Uyumlu** - Responsive tasarım  
✅ **Dark Premium** - Profesyonel görünüm  
✅ **WebGL Rendering** - Fiziksel olarak doğru aydınlatma  

## 🔧 Teknik Detaylar

- **Framework**: Google Model Viewer
- **Format**: GLB/GLTF
- **Sunucu**: Python HTTP Server
- **API Endpoint**: `/api/models`
- **Port**: 8000
- **Tarayıcı**: Tüm modern tarayıcılar (Chrome, Firefox, Safari, Edge)

## 📋 API Endpoint

Model listesini programatik olarak almak:

```bash
curl http://localhost:8000/api/models
```

Yanıt:
```json
{
  "models": [
    {
      "id": 1,
      "name": "Ürün 1",
      "filename": "urun-1.glb",
      "description": "3D Model - urun-1.glb"
    }
  ]
}
```

## 🌐 Deployment

### Canlı Sunucu
Production için profesyonel sunucu kullan:
- Nginx
- Apache
- Node.js Express
- Python Flask/Gunicorn

Sayfaları ve modelleri aynı sunucuya yükle:
```
/var/www/formrack/
├── index.html
├── models/
│   ├── model1.glb
│   └── model2.glb
└── ...
```

## ⚙️ Python Gereksinimleri

Python 3.7+ (ek paket yok)

## 📝 Not

- `.glb` dosyaları SolidWorks → Blender → GLB formatında olmalı
- Dosya isimleri UTF-8 uyumlu olmalı
- Max dosya boyutu: Sunucuya bağlı (genelde 1GB)

## 📧 Destek

Sorularınız için iletişime geçin.

---

**Formrack** - Premium Industrial Solutions
