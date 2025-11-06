# 🏛️ AlgoGov: Algorithmic Governance Simulator

**Algoritmik yönetişim ve dijital demokrasiyi simüle eden açık kaynak oyun platformu**


## 🎯 Proje Hakkında

AlgoGov, 1000 kişilik bir uzay kolonisinde farklı yönetim modellerini test etmek için tasarlanmış interaktif bir simülasyondur. Proje, dijital demokrasi, algoritmik karar alma ve katılımcı yönetişim konularında deneysel araştırma yapmayı hedefler.

### Ana Özellikler

- 🧑‍🤝‍🧑 **1000 Karakterli Dinamik Toplum**: Her biri Ethos-Pathos-Logos dengesiyle karakterize edilmiş bireyler
- 🏛️ **9 Yönetim Modülü**: Adalet, Güvenlik, Sağlık, Eğitim, Ekonomi, İçişleri, Dışişleri, Çevre, Teknoloji
- 🎮 **3 Aşamalı Deney**: İnsan → Algoritma → Hibrit yönetim modelleri
- 📊 **Gerçek Zamanlı Metrikler**: Mutluluk, ekonomi, çevre, suç, gelişme
- 🔬 **Bilimsel Metodoloji**: Tekrarlanabilir, veri odaklı araştırma

## 🚀 Hızlı Başlangıç

### Gereksinimler

- Python 3.9 veya üzeri
- Hiçbir ek paket gerekmez! (Sadece standard library)

### Kurulum

```bash
# Repo'yu klonla
git clone https://github.com/[your-username]/algogov-simulator.git
cd algogov-simulator

# Doğrudan çalıştır (sanal ortam opsiyonel)
python main.py
```

### İlk Oyununuz

```bash
$ python main.py

============================================================
  ALGOGOV: Algorithmic Governance Simulator v0.1
============================================================

🏗️  Koloni başlatılıyor...
✅ Alpha Colony hazır! Nüfus: 1000

📋 Karar veritabanı yüklendi: 20 karar

Simülasyona başlamak için Enter'a basın...
```

## 📁 Proje Yapısı

```
algogov-simulator/
│
├── main.py                    # Ana giriş noktası
├── requirements.txt           # Python bağımlılıkları (şimdilik boş)
├── README.md                  # Bu dosya
│
├── src/
│   ├── core/                  # Temel sınıflar
│   │   ├── character.py       # Karakter sistemi
│   │   ├── colony.py          # Koloni yönetimi
│   │   ├── module.py          # Yönetim modülleri
│   │   └── decision_manager.py# Karar yöneticisi
│   │
│   ├── decisions/             # Karar veritabanı
│   │   └── decision_database.py # 20 karar (9 modül × 2-3 karar)
│   │
│   ├── simulation/            # Simülasyon motoru
│   │   └── game_loop.py       # Oyun döngüsü
│   │
│   ├── algorithms/            # Yönetim algoritmaları (Faz 2)
│   │   └── (gelecekte eklenecek)
│   │
│   └── utils/                 # Yardımcı araçlar
│       └── display.py         # Konsol görüntüleme
│
├── tests/                     # Birim testler
│   └── (gelecekte eklenecek)
│
├── data/                      # Simülasyon sonuçları
│   └── (otomatik oluşturulur)
│
└── docs/                      # Dokümantasyon
    ├── game_design.md         # Oyun tasarım dokümanı
    ├── algorithm_specs.md     # Algoritma detayları
    └── research_questions.md  # Araştırma soruları
```

## 🎮 Nasıl Oynanır?

### Faz 1: Manuel Yönetim (Mevcut Versiyon)

Siz koloni yöneticisisiniz! Her turda 9 farklı modül için kararlar alacaksınız.

#### Karar Alma Süreci

1. **Karar Sunulur**: Her modül için bir sorun ve 2-4 seçenek gösterilir
2. **Seçenekleri İnceleyin**: Her seçeneğin özellikleri:
   - **Ethos/Pathos/Logos Ağırlıkları**: İdeolojik karakteristik
   - **Etkiler**: Para, enerji, çevre, suç oranına etkisi
   - **Destek Oranı**: Nüfusun ne kadarının destekleyeceği
3. **Seçim Yapın**: Numarasını yazıp Enter'a basın
4. **Sonuçları İzleyin**: Seçiminiz koloninizi nasıl etkiledi?

#### Örnek Karar

```
────────────────────────────────────────────────────────────
🏛️  MODÜL: Sağlık
📋 KARAR: Sağlık Sisteminin Yapısı
❓ Koloninin sağlık hizmetleri nasıl organize edilmeli?

1. Ücretsiz Evrensel Sağlık: Herkes için tam kapsamlı
   💭 Ethos: 0.4 | Pathos: 0.9 | Logos: 0.5
   📊 Etkiler: money -1200, energy 100
   👥 Tahmini Destek: 67.3%

2. Özel + Kamu Karma: Temel hizmetler ücretsiz
   💭 Ethos: 0.5 | Pathos: 0.5 | Logos: 0.7
   📊 Etkiler: money -600, energy 60, crime 0.01
   👥 Tahmini Destek: 58.2%

3. Sigortaya Dayalı: Herkes kendi sigortasını alır
   💭 Ethos: 0.7 | Pathos: 0.2 | Logos: 0.8
   📊 Etkiler: money -200, energy 30, crime 0.02
   👥 Tahmini Destek: 42.1%

Seçiminiz (1-3): 
```

### Metrikler

Kararlarınız 5 ana metriği etkiler:

- 😊 **Mutluluk** (0-100%): Nüfusun genel ruh hali
- 💰 **Para**: Koloni bütçesi (başlangıç: 10,000)
- 📈 **Gelişme**: Çevre kalitesi × Enerji tüketimi
- 🌱 **Çevre** (0-100%): Çevresel sürdürülebilirlik
- 🚨 **Suç Oranı** (0-100%): Düşük olması iyidir

## 🧠 Ethos-Pathos-Logos Sistemi

Her karakter ve karar seçeneği üç ideolojik boyutta ağırlıklandırılır:

### Ethos (Ahlak/Otorite) 
- Geleneksel değerler
- Hiyerarşi ve otorite
- Toplumsal düzen

### Pathos (Duygu/Empati)
- Duygusal bağ
- Sosyal adalet
- Toplumsal refah

### Logos (Mantık/Akıl)
- Rasyonel analiz
- Verimlilik
- Pragmatik çözümler

**Destek Hesaplama**: Bir karakterin bir kararı destekleme olasılığı, karakter ve karar ağırlıklarının benzerliğine (cosine similarity) bağlıdır.

## 🔬 Araştırma Amaçları

Bu simülasyon şu soruları yanıtlamayı hedefler:

1. **Yönetim Modelleri**: Hangi karar stratejisi (insan, algoritma, hibrit) en başarılı?
2. **Toplumsal Tercihler**: Farklı karakter kompozisyonları nasıl sonuçlar üretir?
3. **Kısa vs Uzun Vade**: Popülist kararlar mı yoksa uzun vadeli planlama mı daha etkili?
4. **Demokratik Meşruiyet**: Destek oranı yüksek kararlar her zaman en iyisi mi?
5. **Çok Boyutlu Optimizasyon**: Tüm metrikleri dengelemek mümkün mü?

## 🗺️ Yol Haritası

### ✅ v0.1 - İlk MVP (Mevcut)
- [x] Temel koloni simülasyonu
- [x] 9 modül × 2 karar = 20 karar veritabanı
- [x] Manuel karar alma arayüzü
- [x] 5 temel metrik takibi
- [x] Konsol tabanlı görselleştirme

### 🔄 v0.2 - Algoritma Yarışması (Gelecek)
- [ ] 7 farklı algoritma implementasyonu
- [ ] Otomatik simülasyon modu
- [ ] Algoritma performans karşılaştırması
- [ ] CSV/JSON veri export

### 🚧 v0.3 - Web Arayüzü
- [ ] FastAPI backend
- [ ] React frontend
- [ ] Gerçek zamanlı grafikler
- [ ] Karar geçmişi görselleştirme

### 🌟 v1.0 - Multiplayer
- [ ] Kullanıcı hesap sistemi
- [ ] Gerçek oyuncular ile hibrit mod
- [ ] Her 7 turda algoritma seçimi
- [ ] Liderboard ve karşılaştırma

## 🤝 Katkıda Bulunma

Katkılarınızı bekliyoruz! İşte yapabilecekleriniz:

### Kolay Katkılar
- 📝 Yeni karar senaryoları yazma
- 🐛 Bug raporları
- 📚 Dokümantasyon iyileştirme
- 🌐 Çeviri (İngilizce/diğer diller)

### Orta Seviye
- 🎨 Görselleştirme iyileştirmeleri
- 🔢 Yeni metrik önerileri
- ⚙️ Performans optimizasyonları
- 🧪 Test yazma

### İleri Seviye
- 🤖 Yeni algoritma stratejileri
- 🌐 Web arayüzü geliştirme
- 📊 Veri analiz araçları
- 🎮 Oyun mekaniği eklentileri

### Katkı Süreci

1. Fork yapın
2. Feature branch oluşturun (`git checkout -b feature/amazing-feature`)
3. Commit yapın (`git commit -m 'Add some amazing feature'`)
4. Push edin (`git push origin feature/amazing-feature`)
5. Pull Request açın

## 📄 Lisans

Bu proje MIT lisansı altında açık kaynak olarak sunulmaktadır. Detaylar için [LICENSE](LICENSE) dosyasına bakın.

## 🙏 İlham Kaynakları

- [Pol.is](https://pol.is) - Konsensüs bulma algoritması
- [Decidim](https://decidim.org) - Katılımcı demokrasi platformu
- [vTaiwan](https://info.vtaiwan.tw) - Dijital yönetişim deneyi
- Democracy 3 & 4 - Yönetim simülasyon oyunları

## 📬 İletişim

- **GitHub Issues**: Bug raporu ve özellik önerileri
- **GitHub Discussions**: Genel tartışmalar ve sorular
- **Email**: [your-email]

## 🌟 Yıldızlayın!

Bu projeyi beğendiyseniz, GitHub'da ⭐ vermeyi unutmayın!

---

**Not**: Bu proje aktif geliştirme aşamasındadır. İlk kararlı sürüm olan v1.0 için yol haritasını takip edin.
