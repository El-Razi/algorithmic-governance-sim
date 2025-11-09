# Not: YZ analizörü her karar için seçenekler oluşturmuş gibi kurgusal yaklaşım
# ...existing code...
DECISION_DATABASE = {
    "⚖️ Adalet": [
        # === KURULUM FAZLARI (İlk 3 tur için) ===
        {
            "id": "justice_001",
            "phase": "setup",
            "title": "Yasal Çerçeve Oluşturma",
            "description": "YZ Analiz: Kolonide hukuk sistemi acilen tanımlanmalı. 3 olası model tespit edildi.",
            "options": [
                {
                    "id": "A",
                    "text": "Anayasal Demokrasi: Yazılı anayasa ve bağımsız yargı",
                    "ethos": 0.6,
                    "pathos": 0.5,
                    "logos": 0.7,
                    "effects": {
                        "money": -800,
                        "energy": 40,
                        "crime": -0.03
                    }
                },
                {
                    "id": "B",
                    "text": "Konsensüs Hukuku: Topluluk kararları ve arabuluculuk",
                    "ethos": 0.4,
                    "pathos": 0.8,
                    "logos": 0.5,
                    "effects": {
                        "money": -400,
                        "energy": 30,
                        "crime": -0.02
                    }
                },
                {
                    "id": "C",
                    "text":"Teknokratik Sistem: YZ destekli algoritmik hukuk",
                    "ethos": 0.3,
                    "pathos": 0.3,
                    "logos": 0.9,
                    "effects": {
                        "money": -600,
                        "energy": 50,
                        "crime": -0.04
                     }
                }
            ]
        },
        {
            "id": "justice_002",
            "phase": "setup",
            "title": "Ceza Sistemi Protokolü",
            "description": "YZ Analiz: Suç işleyenlere yaptırım mekanizması kurulmalı. Hayatta kalma şartları dikkate alınmalı.",
            "options": [
                {
                    "id": "A",
                    "text": "İzolasyon Hücreleri: Ayrı bölmelerde karantina",
                    "ethos": 0.7,
                    "pathos": 0.2,
                    "logos": 0.6,
                    "effects": {
                        "money": -500,
                        "energy": 30,
                        "crime": -0.05
                    }
                },
                {
                    "id": "B",
                    "text": "Rehabilitasyon Programı: Psikolojik destek ve yeniden entegrasyon",
                    "ethos": 0.3,
                    "pathos": 0.8,
                    "logos": 0.6,
                    "effects": {
                        "money": -700,
                        "energy": 40,
                        "crime": -0.04
                    }
                },
                {
                    "id": "C",
                    "text": "Toplum Hizmeti: Zorlu görevlerde çalıştırma",
                    "ethos": 0.5,
                    "pathos": 0.5,
                    "logos": 0.7,
                    "effects": {
                        "money": -200,
                        "energy": 35,
                        "crime": -0.03,
                        "environment": 0.01
                    }
                }
            ]
        },
        {
            "id": "justice_003",
            "phase": "setup",
            "title": "Yargı Organı Yapılanması",
            "description": "YZ Analiz: Hâkim ve jüri seçimi için 3 farklı model simüle edildi.",
            "options": [
                {
                    "id": "A",
                    "text": "Uzman Hâkimler: Dünya'dan getirilen hukukçular",
                    "ethos": 0.6,
                    "pathos": 0.3,
                    "logos": 0.8,
                    "effects": {
                        "money": -900,
                        "energy": 30,
                        "crime": -0.06
                    }
                },
                {
                    "id": "B",
                    "text": "Rotatif Jüri: Rastgele seçilen kolonistler",
                    "ethos": 0.4,
                    "pathos": 0.7,
                    "logos": 0.5,
                    "effects": {
                        "money": -300,
                        "energy": 25,
                        "crime": -0.02
                    }
                },
                {
                    "id": "C",
                    "text": "YZ Yargıç: Tarafsız algoritma kararları",
                    "ethos": 0.3,
                    "pathos": 0.2,
                    "logos": 0.9,
                    "effects": {
                        "money": -600,
                        "energy": 45,
                        "crime": -0.05
                    }
                }
            ]
        },
        {
            "id": "justice_004",
            "phase": "setup",
            "title": "Temel Haklar Bildirisi",
            "description": "YZ Analiz: Kolonistlerin hak ve özgürlüklerini tanımlayan belge gerekli.",
            "options": [
                {
                    "id": "A",
                    "text": "Geniş Haklar: İfade, toplantı, mahremiyet özgürlükleri",
                    "ethos": 0.3,
                    "pathos": 0.7,
                    "logos": 0.6,
                    "effects": {
                        "money": -200,
                        "energy": 20,
                        "crime": 0.01
                    }
                },
                {
                    "id": "B",
                    "text": "Sınırlı Haklar: Hayatta kalma öncelikli, bazı kısıtlamalar",
                    "ethos": 0.7,
                    "pathos": 0.3,
                    "logos": 0.7,
                    "effects": {
                        "money": -100,
                        "energy": 15,
                        "crime": -0.02
                    }
                },
                {
                    "id": "C",
                    "text": "Dinamik Haklar: Durumlara göre ayarlanabilen sistem",
                    "ethos": 0.5,
                    "pathos": 0.5,
                    "logos": 0.8,
                    "effects": {
                        "money": -300,
                        "energy": 25,
                        "crime": 0.0
                    }
                }
            ]
        },
        
        # === SORUN VE TALEPLER (4-12. kararlar) ===
        {
            "id": "justice_005",
            "phase": "crisis",
            "title": "İlk Cinayet Vakası",
            "description": "ACIL - YZ Analiz: Bir kolonist diğerini öldürdü. Oksijen kıtlığı tartışması. Toplum şokta. Ceza kararı bekleniyor.",
            "options": [
                {
                    "id": "A",
                    "text": "Hava Kilidinden Dışarı Atma: Caydırıcı maksimum ceza",
                    "ethos": 0.8,
                    "pathos": 0.1,
                    "logos": 0.4,
                    "effects": {
                        "money": 0,
                        "energy": 10,
                        "crime": -0.08
                    }
                },
                {
                    "id": "B",
                    "text": "Ömür Boyu İzolasyon: Yaşam hakkı korunur, tecrit edilir",
                    "ethos": 0.6,
                    "pathos": 0.5,
                    "logos": 0.6,
                    "effects": {
                        "money": -400,
                        "energy": 25,
                        "crime": -0.04
                    }
                },
                {
                    "id": "C",
                    "text": "Psikolojik Tedavi: Uzay psikozu teşhisi, tedavi protokolü",
                    "ethos": 0.3,
                    "pathos": 0.8,
                    "logos": 0.7,
                    "effects": {
                        "money": -600,
                        "energy": 35,
                        "crime": -0.02
                    }
                }
            ]
        },
        {
            "id": "justice_006",
            "phase": "crisis",
            "title": "Kaynak Hırsızlığı Salgını",
            "description": "YZ Analiz: Su ve gıda stoklarından sistematik çalma tespit edildi. %15 kolonist karışmış. Sert önlem talebi var.",
            "options": [
                {
                    "id": "A",
                    "text": "Toplu Ceza: Herkese rasyon kesintisi, kolektif sorumluluk",
                    "ethos": 0.7,
                    "pathos": 0.2,
                    "logos": 0.5,
                    "effects": {
                        "money": 200,
                        "energy": 15,
                        "crime": -0.06
                    }
                },
                {
                    "id": "B",
                    "text": "Bireysel Soruşturma: Her vaka ayrı değerlendirilsin",
                    "ethos": 0.5,
                    "pathos": 0.6,
                    "logos": 0.7,
                    "effects": {
                        "money": -500,
                        "energy": 40,
                        "crime": -0.03
                    }
                },
                {
                    "id": "C",
                    "text": "Af ve Yeniden Dağıtım: Kökeni anlamak, sistemi düzeltmek",
                    "ethos": 0.3,
                    "pathos": 0.8,
                    "logos": 0.6,
                    "effects": {
                        "money": -300,
                        "energy": 30,
                        "crime": 0.01
                    }
                }
            ]
        },
        {
            "id": "justice_007",
            "phase": "crisis",
            "title": "İsyan Girişimi İddiası",
            "description": "YZ Analiz: Güvenlik, bir grubun yönetimi ele geçirme planı yaptığını bildiriyor. Kanıt belirsiz. Hızlı karar gerek.",
            "options": [
                {
                    "id": "A",
                    "text": "Önleyici Tutuklama: Şüpheliler derhal izole edilsin",
                    "ethos": 0.8,
                    "pathos": 0.2,
                    "logos": 0.5,
                    "effects": {
                        "money": -200,
                        "energy": 20,
                        "crime": -0.05
                    }
                },
                {
                    "id": "B",
                    "text": "Şeffaf Soruşturma: Açık duruşma, toplum izlesin",
                    "ethos": 0.4,
                    "pathos": 0.6,
                    "logos": 0.8,
                    "effects": {
                        "money": -400,
                        "energy": 35,
                        "crime": -0.02
                    }
                },
                {
                    "id": "C",
                    "text": "Diyalog Girişimi: Temsilcilerle müzakere, talepleri dinle",
                    "ethos": 0.3,
                    "pathos": 0.8,
                    "logos": 0.6,
                    "effects": {
                        "money": -300,
                        "energy": 25,
                        "crime": 0.02
                    }
                }
            ]
        },
        {
            "id": "justice_008",
            "phase": "crisis",
            "title": "Sabotaj Suçlaması",
            "description": "YZ Analiz: Yaşam destek sisteminde manipülasyon bulundu. Suçlu tespit edilemedi. Paranoya yayılıyor.",
            "options": [
                {
                    "id": "A",
                    "text": "Kapsamlı Sorgu: Herkesten ifade al, suçluyu bul",
                    "ethos": 0.7,
                    "pathos": 0.3,
                    "logos": 0.7,
                    "effects": {
                        "money": -600,
                        "energy": 45,
                        "crime": -0.04
                    }
                },
                {
                    "id": "B",
                    "text": "YZ İzleme: Sistematik gözetim başlat",
                    "ethos": 0.6,
                    "pathos": 0.2,
                    "logos": 0.9,
                    "effects": {
                        "money": -800,
                        "energy": 60,
                        "crime": -0.06
                    }
                },
                {
                    "id": "C",
                    "text": "Af İlanı: Suçlu kendini açıklarsa ceza indirimi",
                    "ethos": 0.4,
                    "pathos": 0.7,
                    "logos": 0.6,
                    "effects": {
                        "money": -200,
                        "energy": 20,
                        "crime": -0.01
                    }
                }
            ]
        },
        {
            "id": "justice_009",
            "phase": "crisis",
            "title": "Karaborsaya Talebi",
            "description": "YZ Analiz: Yeraltı ticaret ağı tespit edildi. İlaç, gıda, malzeme. Bazıları 'gerekli' diyor.",
            "options": [
                {
                    "id": "A",
                    "text": "Sıfır Tolerans: Tüm karaborsayı kapat, katılanları cezalandır",
                    "ethos": 0.8,
                    "pathos": 0.2,
                    "logos": 0.6,
                    "effects": {
                        "money": -300,
                        "energy": 30,
                        "crime": -0.05
                    }
                },
                {
                    "id": "B",
                    "text": "Düzenle ve Vergilendir: Yasal karaborsa, kontrollü ticaret",
                    "ethos": 0.4,
                    "pathos": 0.5,
                    "logos": 0.8,
                    "effects": {
                        "money": 400,
                        "energy": 40,
                        "crime": 0.02
                    }
                },
                {
                    "id": "C",
                    "text": "Alternatif Sağla: Resmi dağıtım ağını iyileştir",
                    "ethos": 0.5,
                    "pathos": 0.7,
                    "logos": 0.7,
                    "effects": {
                        "money": -600,
                        "energy": 50,
                        "crime": -0.03
                    }
                }
            ]
        },
        {
            "id": "justice_010",
            "phase": "crisis",
            "title": "Aile İçi Şiddet Vakası",
            "description": "YZ Analiz: Kapalı yaşam alanlarında şiddet artıyor. Mağdurlar sessiz kalıyor. Müdahale protokolü tanımsız.",
            "options": [
                {
                    "id": "A",
                    "text": "Zorunlu Ayrılık: Şiddet uygulayan derhalayrı bölmeye",
                    "ethos": 0.7,
                    "pathos": 0.5,
                    "logos": 0.6,
                    "effects": {
                        "money": -400,
                        "energy": 30,
                        "crime": -0.03
                    }
                },
                {
                    "id": "B",
                    "text": "Aile Terapisi: Çift danışmanlığı ve psikolojik destek",
                    "ethos": 0.4,
                    "pathos": 0.8,
                    "logos": 0.7,
                    "effects": {
                        "money": -600,
                        "energy": 40,
                        "crime": -0.02
                    }
                },
                {
                    "id": "C",
                    "text": "Toplumsal Arabuluculuk: Komşu müdahalesi sistemi",
                    "ethos": 0.5,
                    "pathos": 0.7,
                    "logos": 0.5,
                    "effects": {
                        "money": -200,
                        "energy": 25,
                        "crime": -0.01
                    }
                }
            ]
        },
        {
            "id": "justice_011",
            "phase": "crisis",
            "title": "Çocuk Suçu Meselesi",
            "description": "YZ Analiz: Uzayda doğan ilk nesil ergenliğe girdi. Vandalizm ve isyan arttı. Yetişkin mahkemeleri uygun değil.",
            "options": [
                {
                    "id": "A",
                    "text": "Yetişkin Gibi Yargıla: Suç suçtur, yaş önemli değil",
                    "ethos": 0.8,
                    "pathos": 0.2,
                    "logos": 0.5,
                    "effects": {
                        "money": -200,
                        "energy": 20,
                        "crime": -0.04
                    }
                },
                {
                    "id": "B",
                    "text": "Gençlik Mahkemesi: Özel rehabilitasyon programı",
                    "ethos": 0.4,
                    "pathos": 0.8,
                    "logos": 0.7,
                    "effects": {
                        "money": -700,
                        "energy": 45,
                        "crime": -0.02
                    }
                },
                {
                    "id": "C",
                    "text": "Toplumsal Mentörlük: Yaşlılar gençlere rehberlik etsin",
                    "ethos": 0.6,
                    "pathos": 0.7,
                    "logos": 0.6,
                    "effects": {
                        "money": -400,
                        "energy": 35,
                        "crime": -0.03
                    }
                }
            ]
        },
        {
            "id": "justice_012",
            "phase": "crisis",
            "title": "Ötanazi Talebi",
            "description": "YZ Analiz: Terminal hasta bir kolonist ölme hakkı talep ediyor. Tıbbi kaynaklar kısıtlı. Etik tartışma başladı.",
            "options": [
                {
                    "id": "A",
                    "text": "Yasakla: Yaşam kutsaldır, ötanazi kabul edilemez",
                    "ethos": 0.8,
                    "pathos": 0.3,
                    "logos": 0.4,
                    "effects": {
                        "money": -300,
                        "energy": 25,
                        "crime": 0.0
                    }
                },
                {
                    "id": "B",
                    "text": "Düzenlenmiş İzin: Sıkı prosedür ile tıbbi ötanazi",
                    "ethos": 0.4,
                    "pathos": 0.7,
                    "logos": 0.8,
                    "effects": {
                        "money": -100,
                        "energy": 15,
                        "crime": 0.01
                    }
                },
                {
                    "id": "C",
                    "text": "Bireysel Özgürlük: Herkes kendi kararını verir",
                    "ethos": 0.2,
                    "pathos": 0.6,
                    "logos": 0.7,
                    "effects": {
                        "money": -50,
                        "energy": 10,
                        "crime": 0.02
                    }
                }
            ]
        }
    ],
    "🛡️ Güvenlik": [
        # === KURULUM FAZLARI ===
        {
            "id": "security_001",
            "phase": "setup",
            "title": "Güvenlik Gücü Organizasyonu",
            "description": "YZ Analiz: Kolonide düzeni sağlayacak güvenlik yapısı kurulmalı. 3 model öneriliyor.",
            "options": [
                {
                    "id": "A",
                    "text": "Profesyonel Güvenlik: Eğitimli tam zamanlı ekip",
                    "ethos": 0.7,
                    "pathos": 0.3,
                    "logos": 0.7,
                    "effects": {
                        "money": -1000,
                        "energy": 60,
                        "crime": -0.08
                    }
                },
                {
                    "id": "B",
                    "text": "Rotatif Nöbet: Tüm kolonistler sırayla görev alır",
                    "ethos": 0.5,
                    "pathos": 0.7,
                    "logos": 0.5,
                    "effects": {
                        "money": -300,
                        "energy": 40,
                        "crime": -0.03
                    }
                },
                {
                    "id": "C",
                    "text": "YZ Gözetim: Otonom sensörler ve robotlar",
                    "ethos": 0.4,
                    "pathos": 0.2,
                    "logos": 0.9,
                    "effects": {
                        "money": -1200,
                        "energy": 80,
                        "crime": -0.10
                    }
                }
            ]
        },
         {
            "id": "security_002",
            "phase": "setup",
            "title": "Silahlanma Politikası",
            "description": "YZ Analiz: Tehlikelere karşı silah bulundurma konusu netleştirilmeli. Risk analizi tamamlandı.",
            "options": [
                {
                    "id": "A",
                    "text": "Sadece Güvenlik Gücünde: Merkezi kontrol",
                    "ethos": 0.7,
                    "pathos": 0.4,
                    "logos": 0.7,
                    "effects": {
                        "money": -400,
                        "energy": 30,
                        "crime": -0.04
                    }
                },
                {
                    "id": "B",
                    "text": "Lisanslı Bireysel: Eğitim alanlar taşıyabilir",
                    "ethos": 0.6,
                    "pathos": 0.4,
                    "logos": 0.6,
                    "effects": {
                        "money": -200,
                        "energy": 25,
                        "crime": 0.02
                    }
                },
                {
                    "id": "C",
                    "text": "Silahsız Koloni: Sadece sersemletici ekipman",
                    "ethos": 0.3,
                    "pathos": 0.8,
                    "logos": 0.5,
                    "effects": {
                        "money": -100,
                        "energy": 15,
                        "crime": 0.01
                    }
                }
            ]
        },
        {
            "id": "security_003",
            "phase": "setup",
            "title": "Acil Durum Protokolleri",
            "description": "YZ Analiz: Hava sızıntısı, yangın, dekompresyon gibi krizler için hazırlık şart. Simülasyonlar çalıştırıldı.",
            "options": [
                {
                    "id": "A",
                    "text": "Askeri Tarzda: Sık tatbikat ve katı disiplin",
                    "ethos": 0.8,
                    "pathos": 0.3,
                    "logos": 0.7,
                    "effects": {
                        "money": -700,
                        "energy": 50,
                        "crime": -0.02
                    }
                },
                {
                    "id": "B",
                    "text": "Sivil Hazırlık: Temel eğitim ve bilgilendirme",
                    "ethos": 0.5,
                    "pathos": 0.7,
                    "logos": 0.7,
                    "effects": {
                        "money": -400,
                        "energy": 30,
                        "crime": 0.0
                    }
                },
                {
                    "id": "C",
                    "text": "YZ Koordinasyon: Sistem otomatik yönlendirir",
                    "ethos": 0.4,
                    "pathos": 0.4,
                    "logos": 0.9,
                    "effects": {
                        "money": -900,
                        "energy": 70,
                        "crime": 0.0
                    }
                }
            ]
        },
        
        # === SORUN VE TALEPLER ===
        {
            "id": "security_004",
            "phase": "crisis",
            "title": "Meteor Yağmuru Uyarısı",
            "description": "ACIL - YZ Analiz: 48 saat içinde meteor yağmuru olasılığı %78. Koruyucu kalkanlar yetersiz. Tahliye mi, siper mi?",
            "options": [
                {
                    "id": "A",
                    "text": "Derin Sığınaklara Tahliye: Herkes güvenli bölmelere",
                    "ethos": 0.6,
                    "pathos": 0.7,
                    "logos": 0.8,
                    "effects": {
                        "money": -600,
                        "energy": 80,
                        "crime": 0.0,
                        "environment": 0.0
                    }
                },
                {
                    "id": "B",
                    "text": "Aktif Savunma: Lazer sistemlerle meteorları parçala",
                    "ethos": 0.7,
                    "pathos": 0.4,
                    "logos": 0.8,
                    "effects": {
                        "money": -1200,
                        "energy": 150,
                        "crime": 0.0,
                        "environment": -0.02
                    }
                },
                {
                    "id": "C",
                    "text": "Risk Al: Minimal önlem, normal yaşama devam",
                    "ethos": 0.5,
                    "pathos": 0.3,
                    "logos": 0.4,
                    "effects": {
                        "money": -200,
                        "energy": 30,
                        "crime": 0.03,
                        "environment": 0.0
                    }
                }
            ]
        },
        {
            "id": "security_005",
            "phase": "crisis",
            "title": "Bilinmeyen Sinyal Tespiti",
            "description": "YZ Analiz: 20km mesafeden düzenli radyo sinyali alınıyor. Kaynak belirsiz. Düşman kolonisi mi, yardım çağrısı mı?",
            "options": [
                {
                    "id": "A",
                    "text": "Keşif Ekibi Gönder: Silahlı araştırma gezisi",
                    "ethos": 0.6,
                    "pathos": 0.5,
                    "logos": 0.7,
                    "effects": {
                        "money": -800,
                        "energy": 100,
                        "crime": 0.0
                    }
                },
                {
                    "id": "B",
                    "text": "Savunma Pozisyonu: Bekle ve hazırlan",
                    "ethos": 0.7,
                    "pathos": 0.3,
                    "logos": 0.7,
                    "effects": {
                        "money": -500,
                        "energy": 60,
                        "crime": -0.01
                    }
                },
                {
                    "id": "C",
                    "text": "Pasif Dinleme: Sinyali kaydet ve analiz et, hemen müdahale etme",
                    "ethos": 0.4,
                    "pathos": 0.5,
                    "logos": 0.8,
                    "effects": {
                        "money": -200,
                        "energy": 30,
                        "crime": 0.0
                    }
                }
            ]
        },
        {
            "id": "security_006",
            "phase": "crisis",
            "title": "Oksijen Üretim Sabotajı",
            "description": "YZ Analiz: Yaşam destek sisteminde kasıtlı müdahale tespit edildi. 72 saat sonra oksijen kritik seviyede. Suçlu bulunamadı.",
            "options": [
                {
                    "id": "A",
                    "text": "Sıkıyönetim İlan Et: Tüm bölgelere askeri kontrol",
                    "ethos": 0.9,
                    "pathos": 0.2,
                    "logos": 0.6,
                    "effects": {
                        "money": -800,
                        "energy": 100,
                        "crime": -0.10
                    }
                },
                {
                    "id": "B",
                    "text": "Acil Onarım: Tüm kaynakları sisteme yönlendir",
                    "ethos": 0.5,
                    "pathos": 0.6,
                    "logos": 0.9,
                    "effects": {
                        "money": -1500,
                        "energy": 150,
                        "crime": 0.0,
                        "environment": 0.02
                    }
                },
                {
                    "id": "C",
                    "text": "Gönüllü İtiraf: Ödül karşılığı bilgi toplama",
                    "ethos": 0.4,
                    "pathos": 0.6,
                    "logos": 0.7,
                    "effects": {
                        "money": -500,
                        "energy": 50,
                        "crime": -0.03
                    }
                }
            ]
        },
        {
            "id": "security_007",
            "phase": "crisis",
            "title": "Çeteleşme Problemi",
            "description": "YZ Analiz: Farklı bölmelerde yaşayan gruplar arası gerginlik artıyor. Çete benzeri yapılar oluştu. Çatışma riski yüksek.",
            "options": [
                {
                    "id": "A",
                    "text": "Zorla Yeniden Yerleştirme: Grupları dağıt",
                    "ethos": 0.8,
                    "pathos": 0.3,
                    "logos": 0.6,
                    "effects": {
                        "money": -600,
                        "energy": 70,
                        "crime": -0.05
                    }
                },
                {
                    "id": "B",
                    "text": "Arabuluculuk Programı: Liderleri masaya oturtur",
                    "ethos": 0.4,
                    "pathos": 0.8,
                    "logos": 0.7,
                    "effects": {
                        "money": -400,
                        "energy": 40,
                        "crime": -0.02
                    }
                },
                {
                    "id": "C",
                    "text": "Ortak Düşman: Dış tehdit vurgula, birliği sağla",
                    "ethos": 0.7,
                    "pathos": 0.5,
                    "logos": 0.6,
                    "effects": {
                        "money": -300,
                        "energy": 35,
                        "crime": -0.04
                    }
                }
            ]
        },
        {
            "id": "security_008",
            "phase": "crisis",
            "title": "Güvenlik Gücü İsyanı",
            "description": "YZ Analiz: Güvenlik ekibinin %30'u maaş ve çalışma koşullarından şikayetçi. İş bırakma tehdidi var.",
            "options": [
                {
                    "id": "A",
                    "text": "Talepler Kabul Edilsin: Maaş artışı ve iyileştirmeler",
                    "ethos": 0.5,
                    "pathos": 0.7,
                    "logos": 0.6,
                    "effects": {
                        "money": -1000,
                        "energy": 50,
                        "crime": -0.03
                    }
                },
                {
                    "id": "B",
                    "text": "Değiştir: İsyancıları görevden al, yenilerini ata",
                    "ethos": 0.8,
                    "pathos": 0.2,
                    "logos": 0.5,
                    "effects": {
                        "money": -600,
                        "energy": 60,
                        "crime": 0.05
                    }
                },
                {
                    "id": "C",
                    "text": "Müzakere: Kısmi talepler, uzun vadeli iyileştirme",
                    "ethos": 0.6,
                    "pathos": 0.6,
                    "logos": 0.8,
                    "effects": {
                        "money": -500,
                        "energy": 45,
                        "crime": 0.0
                    }
                }
            ]
        },
        {
            "id": "security_009",
            "phase": "crisis",
            "title": "Kaçak Yapı Tespit Edildi",
            "description": "YZ Analiz: İzinsiz bölmelerde gizli odalar inşa edilmiş. Güvenlik riski oluşturuyor. Amaçları belirsiz.",
            "options": [
                {
                    "id": "A",
                    "text": "Derhal Yık: Yasadışı yapıları kaldır",
                    "ethos": 0.8,
                    "pathos": 0.2,
                    "logos": 0.6,
                    "effects": {
                        "money": -300,
                        "energy": 40,
                        "crime": -0.04
                    }
                },
                {
                    "id": "B",
                    "text": "Kayıt Altına Al: Yasallaştır ve denetle",
                    "ethos": 0.4,
                    "pathos": 0.6,
                    "logos": 0.7,
                    "effects": {
                        "money": -200,
                        "energy": 25,
                        "crime": 0.01
                    }
                },
                {
                    "id": "C",
                    "text": "Görmezden Gel: Mahremiyet hakkı tanı",
                    "ethos": 0.3,
                    "pathos": 0.7,
                    "logos": 0.4,
                    "effects": {
                        "money": 0,
                        "energy": 10,
                        "crime": 0.03
                    }
                }
            ]
        },
        {
            "id": "security_010",
            "phase": "crisis",
            "title": "Panik Atağı Salgını",
            "description": "YZ Analiz: Kolonistlerin %25'i klaustrofobi ve panik atak yaşıyor. Güvenlik olaylarına yanlış tepkiler artıyor.",
            "options": [
                {
                    "id": "A",
                    "text": "Sakinleştirici Dağıt: Kimyasal müdahale",
                    "ethos": 0.6,
                    "pathos": 0.4,
                    "logos": 0.7,
                    "effects": {
                        "money": -400,
                        "energy": 30,
                        "crime": -0.02
                    }
                },
                {
                    "id": "B",
                    "text": "Grup Terapisi: Psikolojik destek grupları kur",
                    "ethos": 0.4,
                    "pathos": 0.8,
                    "logos": 0.7,
                    "effects": {
                        "money": -600,
                        "energy": 40,
                        "crime": -0.01
                    }
                },
                {
                    "id": "C",
                    "text": "Sanal Gerçeklik: VR ile Dünya simülasyonu",
                    "ethos": 0.3,
                    "pathos": 0.6,
                    "logos": 0.8,
                    "effects": {
                        "money": -800,
                        "energy": 60,
                        "crime": 0.0
                    }
                }
            ]
        },
        {
            "id": "security_011",
            "phase": "crisis",
            "title": "Radyasyon Sızıntısı",
            "description": "ACIL - YZ Analiz: C Sektöründe radyasyon seviyeleri normalin 3 katı. 150 kişi risk altında. Tahliye vs onarım?",
            "options": [
                {
                    "id": "A",
                    "text": "Acil Tahliye: Sektörü boşalt, karantinaya al",
                    "ethos": 0.6,
                    "pathos": 0.7,
                    "logos": 0.8,
                    "effects": {
                        "money": -1000,
                        "energy": 120,
                        "crime": 0.02
                    }
                },
                {
                    "id": "B",
                    "text": "Robot Onarımı: İnsansız müdahale ekibi",
                    "ethos": 0.5,
                    "pathos": 0.5,
                    "logos": 0.9,
                    "effects": {
                        "money": -1500,
                        "energy": 150,
                        "crime": 0.0
                    }
                },
                {
                    "id": "C",
                    "text": "Gönüllü Kahramanlar: Fazla ödeme karşılığı insan ekibi",
                    "ethos": 0.7,
                    "pathos": 0.4,
                    "logos": 0.6,
                    "effects": {
                        "money": -800,
                        "energy": 80,
                        "crime": -0.01
                    }
                }
            ]
        },
        {
            "id": "security_012",
            "phase": "crisis",
            "title": "Uydu Kaybı",
            "description": "YZ Analiz: İletişim ve gözetim uydusu çalışmayı durdurdu. Dış dünyayla bağlantı koptu. Onarım ekibi göndermek riskli.",
            "options": [
                {
                    "id": "A",
                    "text": "Uzay Yürüyüşü: En iyi teknisyenler onarıma gitsin",
                    "ethos": 0.7,
                    "pathos": 0.5,
                    "logos": 0.7,
                    "effects": {
                        "money": -1000,
                        "energy": 150,
                        "crime": 0.0
                    }
                },
                {
                    "id": "B",
                    "text": "Yeni Uydu Fırlat: Yedek uyduyu devreye al",
                    "ethos": 0.5,
                    "pathos": 0.4,
                    "logos": 0.9,
                    "effects": {
                        "money": -2000,
                        "energy": 200,
                        "crime": 0.0
                    }
                },
                {
                    "id": "C",
                    "text": "İzolasyonu Kabul Et: İçe dönük yaşama alış",
                    "ethos": 0.6,
                    "pathos": 0.6,
                    "logos": 0.4,
                    "effects": {
                        "money": 0,
                        "energy": 20,
                        "crime": 0.04
                    }
                }
            ]
        }
    ],
    
    "🏥 Sağlık": [
        # === KURULUM FAZLARI ===
        {
            "id": "health_001",
            "phase": "setup",
            "title": "Sağlık Sistemi Altyapısı",
            "description": "YZ Analiz: Tıbbi bakım organizasyonu kurulmalı. Sınırlı kaynaklarla maksimum kapsam hedefleniyor.",
            "options": [
                {
                    "id": "A",
                    "text": "Merkezi Hastane: Tam donanımlı tek büyük tesis",
                    "ethos": 0.6,
                    "pathos": 0.5,
                    "logos": 0.8,
                    "effects": {
                        "money": -1500,
                        "energy": 100,
                        "crime": 0.0
                    }
                },
                {
                    "id": "B",
                    "text": "Dağıtık Klinikler: Her sektörde küçük revir",
                    "ethos": 0.5,
                    "pathos": 0.7,
                    "logos": 0.6,
                    "effects": {
                        "money": -1000,
                        "energy": 80,
                        "crime": 0.0
                    }
                },
                {
                    "id": "C",
                    "text": "Tele-Tıp: YZ teşhis, uzaktan tedavi",
                    "ethos": 0.3,
                    "pathos": 0.4,
                    "logos": 0.9,
                    "effects": {
                        "money": -800,
                        "energy": 60,
                        "crime": 0.0
                    }
                }
            ]
        },
        {
            "id": "health_002",
            "phase": "setup",
            "title": "Tıbbi Önceliklendirme",
            "description": "YZ Analiz: Kaynaklar sınırlı. Acil durumlarda kim önce tedavi edilecek? Etik protokol gerekli.",
            "options": [
                {
                    "id": "A",
                    "text": "İlk Gelen: Sıra sistemi, adil dağılım",
                    "ethos": 0.5,
                    "pathos": 0.8,
                    "logos": 0.6,
                    "effects": {
                        "money": -300,
                        "energy": 25,
                        "crime": 0.0
                    }
                },
                {
                    "id": "B",
                    "text": "Hayatta Kalma Şansı: En yüksek kurtarma ihtimali",
                    "ethos": 0.6,
                    "pathos": 0.4,
                    "logos": 0.9,
                    "effects": {
                        "money": -200,
                        "energy": 20,
                        "crime": 0.01
                    }
                },
                {
                    "id": "C",
                    "text": "Toplumsal Değer: Koloniye katkısı yüksek olanlar",
                    "ethos": 0.7,
                    "pathos": 0.2,
                    "logos": 0.7,
                    "effects": {
                        "money": -250,
                        "energy": 22,
                        "crime": 0.03
                    }
                }
            ]
        },
        {
            "id": "health_003",
            "phase": "setup",
            "title": "İlaç Üretim Stratejisi",
            "description": "YZ Analiz: Dünya'dan getirilen ilaç stoku tükeniyor. Kendi üretimimizi başlatmalıyız.",
            "options": [
                {
                    "id": "A",
                    "text": "Biyosentez Laboratuvarı: Mikrobiyal üretim",
                    "ethos": 0.5,
                    "pathos": 0.6,
                    "logos": 0.9,
                    "effects": {
                        "money": -2000,
                        "energy": 150,
                        "crime": 0.0,
                        "environment": 0.02
                    }
                },
                {
                    "id": "B",
                    "text": "Bitkisel İlaçlar: Sera tarımında tıbbi bitkiler",
                    "ethos": 0.4,
                    "pathos": 0.7,
                    "logos": 0.6,
                    "effects": {
                        "money": -1000,
                        "energy": 80,
                        "crime": 0.0,
                        "environment": 0.04
                    }
                },
                {
                    "id": "C",
                    "text": "Rasyon ve Öncelik: Mevcut stoğu dikkatli kullan",
                    "ethos": 0.7,
                    "pathos": 0.3,
                    "logos": 0.7,
                    "effects": {
                        "money": -200,
                        "energy": 30,
                        "crime": 0.02
                    }
                }
            ]
        },
        {
            "id": "health_004",
            "phase": "setup",
            "title": "Ruh Sağlığı Programı",
            "description": "YZ Analiz: Kapalı ortam psikolojik sorunlara yol açıyor. Proaktif destek sistemi öneriliyor.",
            "options": [
                {
                    "id": "A",
                    "text": "Zorunlu Terapi: Herkes ayda bir görüşme",
                    "ethos": 0.7,
                    "pathos": 0.6,
                    "logos": 0.7,
                    "effects": {
                        "money": -1200,
                        "energy": 70,
                        "crime": -0.03
                    }
                },
                {
                    "id": "B",
                    "text": "Gönüllü Destek: İsteyen başvursun",
                    "ethos": 0.4,
                    "pathos": 0.7,
                    "logos": 0.6,
                    "effects": {
                        "money": -600,
                        "energy": 40,
                        "crime": 0.0
                    }
                },
                {
                    "id": "C",
                    "text": "Akran Desteği: Kolonistler birbirini dinlesin",
                    "ethos": 0.5,
                    "pathos": 0.8,
                    "logos": 0.5,
                    "effects": {
                        "money": -200,
                        "energy": 25,
                        "crime": 0.0
                    }
                }
            ]
        },
        
        # === SORUN VE TALEPLER ===
        {
            "id": "health_005",
            "phase": "crisis",
            "title": "Bilinmeyen Hastalık Salgını",
            "description": "ACIL - YZ Analiz: 47 kolonist benzer semptomlar gösteriyor. Uzay mikrobu olabilir. Karantina kararı şart.",
            "options": [
                {
                    "id": "A",
                    "text": "Tam Karantina: Hasta sektörü tamamen izole et",
                    "ethos": 0.8,
                    "pathos": 0.4,
                    "logos": 0.8,
                    "effects": {
                        "money": -800,
                        "energy": 100,
                        "crime": 0.02
                    }
                },
                {
                    "id": "B",
                    "text": "Deneysel Tedavi: Yeni ilaç kombinasyonları dene",
                    "ethos": 0.5,
                    "pathos": 0.6,
                    "logos": 0.8,
                    "effects": {
                        "money": -1200,
                        "energy": 120,
                        "crime": 0.0
                    }
                },
                {
                    "id": "C",
                    "text": "Doğal Bağışıklık: Minimal müdahale, vücut savaşsın",
                    "ethos": 0.6,
                    "pathos": 0.3,
                    "logos": 0.5,
                    "effects": {
                        "money": -200,
                        "energy": 40,
                        "crime": 0.04
                    }
                }
            ]
        },
        {
            "id": "health_006",
            "phase": "crisis",
            "title": "Doktor İntiharı",
            "description": "YZ Analiz: Baş cerrahımız intihar etti. Not: 'Tükendim, kimseyi kurtaramıyorum.' Moral çöktü. Acil liderlik gerek.",
            "options": [
                {
                    "id": "A",
                    "text": "Yeni Başhekim Ata: Hızlı terfi ve sorumluluk",
                    "ethos": 0.7,
                    "pathos": 0.5,
                    "logos": 0.7,
                    "effects": {
                        "money": -400,
                        "energy": 35,
                        "crime": 0.0
                    }
                },
                {
                    "id": "B",
                    "text": "Ekip Terapisi: Tüm sağlık çalışanları psikolojik destek",
                    "ethos": 0.4,
                    "pathos": 0.9,
                    "logos": 0.6,
                    "effects": {
                        "money": -800,
                        "energy": 50,
                        "crime": 0.0
                    }
                },
                {
                    "id": "C",
                    "text": "YZ Doktor Devrede: Algoritmik tıp ana sistem olsun",
                    "ethos": 0.5,
                    "pathos": 0.3,
                    "logos": 0.9,
                    "effects": {
                        "money": -1000,
                        "energy": 80,
                        "crime": 0.01
                    }
                }
            ]
        },
        {
            "id": "health_007",
            "phase": "crisis",
            "title": "Yaşlı Nüfus Krizi",
            "description": "YZ Analiz: 65 yaş üstü kolonistler kronik hastalıklarla boğuşuyor. Kaynak %40'ını tüketiyorlar. Tartışma başladı.",
            "options": [
                {
                    "id": "A",
                    "text": "Yaş Limiti Koy: 70 yaş üstü palyatif bakıma geçsin",
                    "ethos": 0.7,
                    "pathos": 0.2,
                    "logos": 0.8,
                    "effects": {
                        "money": 600,
                        "energy": -30,
                        "crime": 0.05
                    }
                },
                {
                    "id": "B",
                    "text": "Eşit Hak: Yaş ayırımı yapma, herkes eşit tedavi",
                    "ethos": 0.4,
                    "pathos": 0.9,
                    "logos": 0.5,
                    "effects": {
                        "money": -1500,
                        "energy": 100,
                        "crime": 0.0
                    }
                },
                {
                    "id": "C",
                    "text": "Gönüllü Feragat: Yaşlılar kendi kararıyla vazgeçsin",
                    "ethos": 0.6,
                    "pathos": 0.5,
                    "logos": 0.6,
                    "effects": {
                        "money": 300,
                        "energy": -15,
                        "crime": 0.02
                    }
                }
            ]
        },
        {
            "id": "health_008",
            "phase": "crisis",
            "title": "Doğum Kontrol Tartışması",
            "description": "YZ Analiz: Hamilelik oranı artıyor. Kaynak hesapları yeni bebeklere hazır değil. Kontrol mi, özgürlük mü?",
            "options": [
                {
                    "id": "A",
                    "text": "Doğum İzni Sistemi: Başvuru ve onay gerekli",
                    "ethos": 0.8,
                    "pathos": 0.3,
                    "logos": 0.8,
                    "effects": {
                        "money": -300,
                        "energy": 30,
                        "crime": 0.03
                    }
                },
                {
                    "id": "B",
                    "text": "Serbest Ama Desteksiz: Doğur ama ekstra kaynak yok",
                    "ethos": 0.6,
                    "pathos": 0.4,
                    "logos": 0.7,
                    "effects": {
                        "money": 0,
                        "energy": 20,
                        "crime": 0.02
                    }
                },
                {
                    "id": "C",
                    "text": "Teşvik: Nüfus artışı uzun vadede avantaj",
                    "ethos": 0.5,
                    "pathos": 0.7,
                    "logos": 0.6,
                    "effects": {
                        "money": -800,
                        "energy": 80,
                        "crime": 0.0
                    }
                }
            ]
        },
        {
            "id": "health_009",
            "phase": "crisis",
            "title": "Organ Nakli Krizi",
            "description": "YZ Analiz: Bir çocuğa böbrek gerek. 2 uyumlu yetişkin var ama ikisi de reddediyor. Zorla mı alsın?",
            "options": [
                {
                    "id": "A",
                    "text": "Zorla Bağış: Toplum yararı bireyin üstünde",
                    "ethos": 0.8,
                    "pathos": 0.5,
                    "logos": 0.6,
                    "effects": {
                        "money": -500,
                        "energy": 60,
                        "crime": 0.04
                    }
                },
                {
                    "id": "B",
                    "text": "Gönüllülük: Zorlanamaz, ikna edilmeye çalışılsın",
                    "ethos": 0.4,
                    "pathos": 0.7,
                    "logos": 0.7,
                    "effects": {
                        "money": -300,
                        "energy": 40,
                        "crime": 0.0
                    }
                },
                {
                    "id": "C",
                    "text": "Yapay Organ: Biyoteknoloji araştırması başlat",
                    "ethos": 0.5,
                    "pathos": 0.6,
                    "logos": 0.9,
                    "effects": {
                        "money": -2000,
                        "energy": 150,
                        "crime": 0.0
                    }
                }
            ]
        },
        {
            "id": "health_010",
            "phase": "crisis",
            "title": "Uyku Bozukluğu Epidemisi",
            "description": "YZ Analiz: %60 kolonist uykusuzluk çekiyor. Performans düştü, kazalar arttı. 24 saatlik yapay gün/gece problemi.",
            "options": [
                {
                    "id": "A",
                    "text": "Uyku İlaçları: Kimyasal müdahale ile düzenli uyku",
                    "ethos": 0.6,
                    "pathos": 0.4,
                    "logos": 0.7,
                    "effects": {
                        "money": -700,
                        "energy": 50,
                        "crime": 0.0
                    }
                },
                {
                    "id": "B",
                    "text": "Işık Terapisi: Gelişmiş yapay gün döngüsü",
                    "ethos": 0.4,
                    "pathos": 0.6,
                    "logos": 0.8,
                    "effects": {
                        "money": -1000,
                        "energy": 80,
                        "crime": 0.0,
                        "environment": 0.01
                    }
                },
                {
                    "id": "C",
                    "text": "Meditasyon Programı: Doğal uyku teknikleri",
                    "ethos": 0.5,
                    "pathos": 0.7,
                    "logos": 0.6,
                    "effects": {
                        "money": -300,
                        "energy": 35,
                        "crime": 0.0
                    }
                }
            ]
        },
        {
            "id": "health_011",
            "phase": "crisis",
            "title": "Gen Tedavisi Talebi",
            "description": "YZ Analiz: Genetik hastalıklı bebekler için CRISPR tedavisi talep ediliyor. Teknoloji mevcut ama etik tartışmalı.",
            "options": [
                {
                    "id": "A",
                    "text": "Sınırlı İzin: Sadece ölümcül hastalıklar için",
                    "ethos": 0.6,
                    "pathos": 0.6,
                    "logos": 0.8,
                    "effects": {
                        "money": -1500,
                        "energy": 120,
                        "crime": 0.01
                    }
                },
                {
                    "id": "B",
                    "text": "Tam Serbestlik: Ebeveyn isterse yapılsın",
                    "ethos": 0.3,
                    "pathos": 0.7,
                    "logos": 0.8,
                    "effects": {
                        "money": -2000,
                        "energy": 150,
                        "crime": 0.02
                    }
                },
                {
                    "id": "C",
                    "text": "Yasak: Doğaya müdahale etik değil",
                    "ethos": 0.8,
                    "pathos": 0.4,
                    "logos": 0.4,
                    "effects": {
                        "money": 0,
                        "energy": 10,
                        "crime": 0.03
                    }
                }
            ]
        },
        {
            "id": "health_012",
            "phase": "crisis",
            "title": "Tıbbi Veriler Sızdırıldı",
            "description": "YZ Analiz: Herkesin sağlık kayıtları hacklendi ve yayınlandı. Mahremiyet ihlali. Damgalanma başladı.",
            "options": [
                {
                    "id": "A",
                    "text": "Suçluyu Bul ve Cezalandır: Ağır yaptırım",
                    "ethos": 0.8,
                    "pathos": 0.4,
                    "logos": 0.7,
                    "effects": {
                        "money": -600,
                        "energy": 50,
                        "crime": -0.04
                    }
                },
                {
                    "id": "B",
                    "text": "Şeffaflık Kültürü: Tüm verileri zaten açık yap",
                    "ethos": 0.3,
                    "pathos": 0.5,
                    "logos": 0.8,
                    "effects": {
                        "money": -200,
                        "energy": 25,
                        "crime": 0.02
                    }
                },
                {
                    "id": "C",
                    "text": "Psikolojik Destek: Mağdurlara terapi sağla",
                    "ethos": 0.5,
                    "pathos": 0.8,
                    "logos": 0.6,
                    "effects": {
                        "money": -500,
                        "energy": 40,
                        "crime": 0.0
                    }
                }
            ]
        }
    ],
    
    "🎓 Eğitim": [
        # === KURULUM FAZLARI ===
        {
            "id": "education_001",
            "phase": "setup",
            "title": "Eğitim Sistemi Modeli",
            "description": "YZ Analiz: Koloni çocukları için eğitim programı kurulmalı. 3 farklı pedagojik yaklaşım değerlendirildi.",
            "options": [
                {
                    "id": "A",
                    "text": "Klasik Sınıf: Öğretmen merkezli, müfredat tabanlı",
                    "ethos": 0.7,
                    "pathos": 0.4,
                    "logos": 0.6,
                    "effects": {
                        "money": -800,
                        "energy": 50,
                        "crime": -0.02
                    }
                },
                {
                    "id": "B",
                    "text": "Montessori: Çocuk merkezli, keşfederek öğrenme",
                    "ethos": 0.3,
                    "pathos": 0.8,
                    "logos": 0.6,
                    "effects": {
                        "money": -1000,
                        "energy": 60,
                        "crime": 0.0
                    }
                },
                {
                    "id": "C",
                    "text": "YZ Öğretmen: Kişiselleştirilmiş dijital eğitim",
                    "ethos": 0.4,
                    "pathos": 0.4,
                    "logos": 0.9,
                    "effects": {
                        "money": -1200,
                        "energy": 80,
                        "crime": 0.0
                    }
                }
            ]
        },
        {
            "id": "education_002",
            "phase": "setup",
            "title": "Müfredat İçeriği",
            "description": "YZ Analiz: Ne öğretilmeli? Dünya bilgisi mi, koloni becerileri mi, yoksa her ikisi mi?",
            "options": [
                {
                    "id": "A",
                    "text": "Dünya Kültürü: Tarih, sanat, edebiyat ağırlıklı",
                    "ethos": 0.6,
                    "pathos": 0.7,
                    "logos": 0.5,
                    "effects": {
                        "money": -500,
                        "energy": 40,
                        "crime": 0.0
                    }
                },
                {
                    "id": "B",
                    "text": "Hayatta Kalma: Mühendislik, tıp, pratik beceriler",
                    "ethos": 0.7,
                    "pathos": 0.3,
                    "logos": 0.9,
                    "effects": {
                        "money": -800,
                        "energy": 60,
                        "crime": 0.0
                    }
                },
                {
                    "id": "C",
                    "text": "Hibrit: %50 klasik eğitim, %50 koloni becerileri",
                    "ethos": 0.5,
                    "pathos": 0.6,
                    "logos": 0.8,
                    "effects": {
                        "money": -700,
                        "energy": 55,
                        "crime": 0.0
                    }
                }
            ]
        },
        {
            "id": "education_003",
            "phase": "setup",
            "title": "Öğretmen Kaynağı",
            "description": "YZ Analiz: Kalifiye öğretmen sayısı yetersiz. Alternatif çözümler değerlendiriliyor.",
            "options": [
                {
                    "id": "A",
                    "text": "Meslek Değişimi: Diğer sektörlerden öğretmen yetiştir",
                    "ethos": 0.6,
                    "pathos": 0.6,
                    "logos": 0.7,
                    "effects": {
                        "money": -600,
                        "energy": 50,
                        "crime": 0.0
                    }
                },
                {
                    "id": "B",
                    "text": "Yaşlı Mentörler: Emekliler öğretmen olsun",
                    "ethos": 0.7,
                    "pathos": 0.7,
                    "logos": 0.6,
                    "effects": {
                        "money": -300,
                        "energy": 30,
                        "crime": 0.0
                    }
                },
                {
                    "id": "C",
                    "text": "Tamamen Dijital: YZ ve video dersler",
                    "ethos": 0.3,
                    "pathos": 0.3,
                    "logos": 0.9,
                    "effects": {
                        "money": -400,
                        "energy": 60,
                        "crime": 0.01
                    }
                }
            ]
        },
        
        # === SORUN VE TALEPLER ===
        {
            "id": "education_004",
            "phase": "crisis",
            "title": "Öğrenci İsyanı",
            "description": "YZ Analiz: Gençler eğitimin anlamsız olduğunu söylüyor. 'Dünya'ya dönmeyeceğiz, neden öğreniyoruz?' diyorlar.",
            "options": [
                {
                    "id": "A",
                    "text": "Zorunlu Devam: Disiplin artır, katılım zorunlu tut",
                    "ethos": 0.8,
                    "pathos": 0.3,
                    "logos": 0.6,
                    "effects": {
                        "money": -400,
                        "energy": 35,
                        "crime": 0.03
                    }
                },
                {
                    "id": "B",
                    "text": "Müfredat Revizyonu: Koloni odaklı içerik geliştir",
                    "ethos": 0.5,
                    "pathos": 0.7,
                    "logos": 0.8,
                    "effects": {
                        "money": -800,
                        "energy": 60,
                        "crime": 0.0
                    }
                },
                {
                    "id": "C",
                    "text": "Öğrenci Konseyine Yetki Ver: Kendi müfredatlarını tasarlasınlar",
                    "ethos": 0.3,
                    "pathos": 0.8,
                    "logos": 0.6,
                    "effects": {
                        "money": -300,
                        "energy": 40,
                        "crime": 0.01
                    }
                }
            ]
        },
        {
            "id": "education_005",
            "phase": "crisis",
            "title": "Öğretmen Tükenmişliği",
            "description": "YZ Analiz: Öğretmenlerin %70'i burn-out yaşıyor. İstifa talepleri geliyor. Eğitim çökme noktasında.",
            "options": [
                {
                    "id": "A",
                    "text": "Maaş ve İzin Artışı: Maddi motivasyon sağla",
                    "ethos": 0.6,
                    "pathos": 0.7,
                    "logos": 0.7,
                    "effects": {
                        "money": -1000,
                        "energy": 50,
                        "crime": 0.0
                    }
                },
                {
                    "id": "B",
                    "text": "Sınıf Mevcudunu Azalt: Daha fazla öğretmen ata",
                    "ethos": 0.5,
                    "pathos": 0.8,
                    "logos": 0.7,
                    "effects": {
                        "money": -800,
                        "energy": 60,
                        "crime": 0.0
                    }
                },
                {
                    "id": "C",
                    "text": "YZ Asistan: Öğretmenlere teknolojik destek",
                    "ethos": 0.4,
                    "pathos": 0.5,
                    "logos": 0.9,
                    "effects": {
                        "money": -1200,
                        "energy": 80,
                        "crime": 0.0
                    }
                }
            ]
        },
        {
            "id": "education_006",
            "phase": "crisis",
            "title": "Eğitim Eşitsizliği",
            "description": "YZ Analiz: Bazı sektörlerdeki çocuklar daha iyi eğitim alıyor. Sosyo-ekonomik bölünme başladı.",
            "options": [
                {
                    "id": "A",
                    "text": "Tek Tip Okul: Herkese eşit kaynak",
                    "ethos": 0.5,
                    "pathos": 0.8,
                    "logos": 0.7,
                    "effects": {
                        "money": -1000,
                        "energy": 70,
                        "crime": -0.02
                    }
                },
                {
                    "id": "B",
                    "text": "Performansa Göre: İyi öğrencilere daha fazla kaynak",
                    "ethos": 0.7,
                    "pathos": 0.3,
                    "logos": 0.8,
                    "effects": {
                        "money": -600,
                        "energy": 50,
                        "crime": 0.03
                    }
                },
                {
                    "id": "C",
                    "text": "Pozitif Ayrımcılık: Geri kalan bölgelere fazla yatırım",
                    "ethos": 0.4,
                    "pathos": 0.9,
                    "logos": 0.6,
                    "effects": {
                        "money": -1200,
                        "energy": 80,
                        "crime": -0.01
                    }
                }
            ]
        },
        {
            "id": "education_007",
            "phase": "crisis",
            "title": "Dünya Tarihi Tartışması",
            "description": "YZ Analiz: Veliler Dünya tarihinin öğretilmesini tartışıyor. 'Eski savaşlar burada anlamsız' diyen grup var.",
            "options": [
                {
                    "id": "A",
                    "text": "Tarih Zorunlu: Geçmişi bilmeden gelecek olmaz",
                    "ethos": 0.7,
                    "pathos": 0.6,
                    "logos": 0.6,
                    "effects": {
                        "money": -300,
                        "energy": 30,
                        "crime": 0.0
                    }
                },
                {
                    "id": "B",
                    "text": "Seçmeli Yap: İsteyen alsın",
                    "ethos": 0.4,
                    "pathos": 0.5,
                    "logos": 0.7,
                    "effects": {
                        "money": -200,
                        "energy": 25,
                        "crime": 0.01
                    }
                },
                {
                    "id": "C",
                    "text": "Kaldır: Sadece koloni tarihi öğretilsin",
                    "ethos": 0.6,
                    "pathos": 0.4,
                    "logos": 0.6,
                    "effects": {
                        "money": -100,
                        "energy": 20,
                        "crime": 0.02
                    }
                }
            ]
        },
        {
            "id": "education_008",
            "phase": "crisis",
            "title": "Özel Yetenek Programı Talebi",
            "description": "YZ Analiz: Üstün zeka gösteren çocuklar sıkılıyor. Aileler özel program istiyor. Kaynakları nereden ayıracağız?",
            "options": [
                {
                    "id": "A",
                    "text": "Hızlandırılmış Program: Ayrı sınıf ve ileri müfredat",
                    "ethos": 0.6,
                    "pathos": 0.5,
                    "logos": 0.8,
                    "effects": {
                        "money": -1000,
                        "energy": 70,
                        "crime": 0.01
                    }
                },
                {
                    "id": "B",
                    "text": "Mentörlük: Yetenekliler yetişkinlerle çalışsın",
                    "ethos": 0.5,
                    "pathos": 0.6,
                    "logos": 0.7,
                    "effects": {
                        "money": -500,
                        "energy": 45,
                        "crime": 0.0
                    }
                },
                {
                    "id": "C",
                    "text": "Herkes Eşit: Özel program elitizm yaratır",
                    "ethos": 0.7,
                    "pathos": 0.7,
                    "logos": 0.5,
                    "effects": {
                        "money": -200,
                        "energy": 25,
                        "crime": 0.02
                    }
                }
            ]
        },
        {
            "id": "education_009",
            "phase": "crisis",
            "title": "Sanal Gerçeklik Bağımlılığı",
            "description": "YZ Analiz: Eğitim VR'ı çocuklar oyun için kullanıyor. Gözlük takılı 12 saat kalıyorlar. Sosyal beceriler kayboluyor.",
            "options": [
                {
                    "id": "A",
                    "text": "VR Yasakla: Sadece fiziksel dersler",
                    "ethos": 0.8,
                    "pathos": 0.5,
                    "logos": 0.5,
                    "effects": {
                        "money": -200,
                        "energy": 20,
                        "crime": 0.02
                    }
                },
                {
                    "id": "B",
                    "text": "Sınırlı Kullanım: Günde maksimum 2 saat",
                    "ethos": 0.6,
                    "pathos": 0.6,
                    "logos": 0.7,
                    "effects": {
                        "money": -400,
                        "energy": 40,
                        "crime": 0.0
                    }
                },
                {
                    "id": "C",
                    "text": "Ebeveyn Kontrolü: Aileler karar versin",
                    "ethos": 0.5,
                    "pathos": 0.7,
                    "logos": 0.6,
                    "effects": {
                        "money": -300,
                        "energy": 30,
                        "crime": 0.01
                    }
                }
            ]
        },
        {
            "id": "education_010",
            "phase": "crisis",
            "title": "Din ve İnanç Eğitimi",
            "description": "YZ Analiz: Farklı dinlere mensup aileler kendi inançlarının öğretilmesini talep ediyor. Laik eğitim mi, çoğulcu mu?",
            "options": [
                {
                    "id": "A",
                    "text": "Laik Eğitim: Hiçbir din okulda öğretilmez",
                    "ethos": 0.5,
                    "pathos": 0.4,
                    "logos": 0.8,
                    "effects": {
                        "money": -200,
                        "energy": 25,
                        "crime": 0.02
                    }
                },
                {
                    "id": "B",
                    "text": "Dinler Tarihi: Objektif bilgi, tüm dinler anlatılır",
                    "ethos": 0.6,
                    "pathos": 0.7,
                    "logos": 0.8,
                    "effects": {
                        "money": -500,
                        "energy": 40,
                        "crime": 0.0
                    }
                },
                {
                    "id": "C",
                    "text": "Ailede Öğretilsin: Okul karışmaz",
                    "ethos": 0.7,
                    "pathos": 0.6,
                    "logos": 0.6,
                    "effects": {
                        "money": -100,
                        "energy": 15,
                        "crime": 0.01
                    }
                }
            ]
        },
        {
            "id": "education_011",
            "phase": "crisis",
            "title": "Fiziksel Eğitim Krizi",
            "description": "YZ Analiz: Çocuklar düşük yerçekiminde büyüdüğü için kas ve kemik gelişimi zayıf. Fiziksel eğitim şart.",
            "options": [
                {
                    "id": "A",
                    "text": "Zorunlu Spor: Günde 2 saat egzersiz",
                    "ethos": 0.7,
                    "pathos": 0.5,
                    "logos": 0.8,
                    "effects": {
                        "money": -800,
                        "energy": 80,
                        "crime": -0.01
                    }
                },
                {
                    "id": "B",
                    "text": "Yapay Yerçekimi Odası: Pahalı ama etkili",
                    "ethos": 0.5,
                    "pathos": 0.6,
                    "logos": 0.9,
                    "effects": {
                        "money": -2000,
                        "energy": 150,
                        "crime": 0.0
                    }
                },
                {
                    "id": "C",
                    "text": "Doğal Uyum: Uzay vücudu evolüsyonu kabul edilsin",
                    "ethos": 0.4,
                    "pathos": 0.5,
                    "logos": 0.6,
                    "effects": {
                        "money": -200,
                        "energy": 25,
                        "crime": 0.02
                    }
                }
            ]
        },
        {
            "id": "education_012",
            "phase": "crisis",
            "title": "Üniversite Alternatifi",
            "description": "YZ Analiz: İlk mezun nesil yetişkin oldu. Yükseköğretim talebi var ama fiziksel kampüs imkansız. Ne yapacağız?",
            "options": [
                {
                    "id": "A",
                    "text": "Çıraklık Sistemi: Pratik beceri öğrenme",
                    "ethos": 0.7,
                    "pathos": 0.6,
                    "logos": 0.7,
                    "effects": {
                        "money": -400,
                        "energy": 40,
                        "crime": 0.0
                    }
                },
                {
                    "id": "B",
                    "text": "Online Üniversite: Dünya'dan uzaktan eğitim",
                    "ethos": 0.4,
                    "pathos": 0.5,
                    "logos": 0.9,
                    "effects": {
                        "money": -1000,
                        "energy": 80,
                        "crime": 0.0
                    }
                },
                {
                    "id": "C",
                    "text": "Koloni Akademisi: Kendi üniversitemizi kur",
                    "ethos": 0.6,
                    "pathos": 0.7,
                    "logos": 0.8,
                    "effects": {
                        "money": -2500,
                        "energy": 150,
                        "crime": 0.0
                    }
                }
            ]
        }
    ],
    
    "💰 Ekonomi": [
        # === KURULUM FAZLARI ===
        {
            "id": "economy_001",
            "phase": "setup",
            "title": "Para Birimi ve Sistem",
            "description": "YZ Analiz: Kolonide ekonomik değişim için sistem kurulmalı. Hangi model uygun?",
            "options": [
                {
                    "id": "A",
                    "text": "Dijital Para: Blockchain tabanlı koloni kredisi",
                    "ethos": 0.4,
                    "pathos": 0.5,
                    "logos": 0.9,
                    "effects": {
                        "money": -800,
                        "energy": 60,
                        "crime": -0.01
                    }
                },
                {
                    "id": "B",
                    "text": "Takas Ekonomisi: Para yok, mal-hizmet değişimi",
                    "ethos": 0.5,
                    "pathos": 0.8,
                    "logos": 0.5,
                    "effects": {
                        "money": -200,
                        "energy": 30,
                        "crime": 0.01
                    }
                },
                {
                    "id": "C",
                    "text": "Çalışma Puanı: Emek saati bazlı sistem",
                    "ethos": 0.6,
                    "pathos": 0.7,
                    "logos": 0.7,
                    "effects": {
                        "money": -400,
                        "energy": 40,
                        "crime": 0.0
                    }
                }
            ]
        },
        {
            "id": "economy_002",
            "phase": "setup",
            "title": "Kaynak Dağıtım Modeli",
            "description": "YZ Analiz: Gıda, su, enerji nasıl dağıtılacak? 3 ekonomik model simüle edildi.",
            "options": [
                {
                    "id": "A",
                    "text": "Eşit Rasyon: Herkese aynı miktar",
                    "ethos": 0.5,
                    "pathos": 0.9,
                    "logos": 0.6,
                    "effects": {
                        "money": -500,
                        "energy": 50,
                        "crime": -0.01
                    }
                },
                {
                    "id": "B",
                    "text": "Performansa Göre: Katkı oranında kaynak",
                    "ethos": 0.7,
                    "pathos": 0.3,
                    "logos": 0.8,
                    "effects": {
                        "money": -300,
                        "energy": 40,
                        "crime": 0.03
                    }
                },
                {
                    "id": "C",
                    "text": "Serbest Piyasa: Arz-talep belirlesin",
                    "ethos": 0.6,
                    "pathos": 0.2,
                    "logos": 0.9,
                    "effects": {
                        "money": 200,
                        "energy": 60,
                        "crime": 0.04
                    }
                }
            ]
        },
        {
            "id": "economy_003",
            "phase": "setup",
            "title": "Üretim Organizasyonu",
            "description": "YZ Analiz: Sera tarımı, madencilik, üretim işlerini kim yönetecek?",
            "options": [
                {
                    "id": "A",
                    "text": "Devlet İşletmeleri: Merkezi planlama",
                    "ethos": 0.7,
                    "pathos": 0.6,
                    "logos": 0.7,
                    "effects": {
                        "money": -600,
                        "energy": 70,
                        "crime": -0.01
                    }
                },
                {
                    "id": "B",
                    "text": "Kooperatifler: İşçi sahipliği ve yönetimi",
                    "ethos": 0.4,
                    "pathos": 0.8,
                    "logos": 0.7,
                    "effects": {
                        "money": -400,
                        "energy": 60,
                        "crime": 0.0
                    }
                },
                {
                    "id": "C",
                    "text": "Özel Girişim: Bireysel şirketler rekabeti",
                    "ethos": 0.6,
                    "pathos": 0.3,
                    "logos": 0.9,
                    "effects": {
                        "money": 300,
                        "energy": 80,
                        "crime": 0.02
                    }
                }
            ]
        },
        
        # === SORUN VE TALEPLER ===
        {
            "id": "economy_004",
            "phase": "crisis",
            "title": "Enflasyon Krizi",
            "description": "YZ Analiz: Fiyatlar %300 arttı. Koloni kredisi değer kaybediyor. Panik alım başladı. Acil müdahale gerek.",
            "options": [
                {
                    "id": "A",
                    "text": "Fiyat Kontrolü: Üst limit koy, zorla uygula",
                    "ethos": 0.8,
                    "pathos": 0.5,
                    "logos": 0.6,
                    "effects": {
                        "money": -500,
                        "energy": 40,
                        "crime": 0.03
                    }
                },
                {
                    "id": "B",
                    "text": "Para Basımı Durdur: Arz azalt, değer koru",
                    "ethos": 0.6,
                    "pathos": 0.4,
                    "logos": 0.9,
                    "effects": {
                        "money": 300,
                        "energy": 30,
                        "crime": 0.04
                    }
                },
                {
                    "id": "C",
                    "text": "Yeni Para Birimi: Sıfırdan başla",
                    "ethos": 0.5,
                    "pathos": 0.5,
                    "logos": 0.8,
                    "effects": {
                        "money": -1000,
                        "energy": 80,
                        "crime": 0.02
                    }
                }
            ]
        },
        {
            "id": "economy_005",
            "phase": "crisis",
            "title": "İşsizlik Artışı",
            "description": "YZ Analiz: Otomasyon nedeniyle %25 kolonist işsiz kaldı. Sosyal gerilim yükseliyor. İş yaratma zorunlu.",
            "options": [
                {
                    "id": "A",
                    "text": "Kamu İstihdamı: Devlet işlerde çalıştır",
                    "ethos": 0.6,
                    "pathos": 0.8,
                    "logos": 0.6,
                    "effects": {
                        "money": -1500,
                        "energy": 100,
                        "crime": -0.03
                    }
                },
                {
                    "id": "B",
                    "text": "Temel Gelir: Çalışmadan maaş ver",
                    "ethos": 0.4,
                    "pathos": 0.9,
                    "logos": 0.7,
                    "effects": {
                        "money": -2000,
                        "energy": 80,
                        "crime": -0.01
                    }
                },
                {
                    "id": "C",
                    "text": "Yeniden Eğitim: Yeni beceriler öğret",
                    "ethos": 0.5,
                    "pathos": 0.6,
                    "logos": 0.9,
                    "effects": {
                        "money": -1000,
                        "energy": 90,
                        "crime": 0.0
                    }
                }
            ]
        },
        {
            "id": "economy_006",
            "phase": "crisis",
            "title": "Servet Uçurumu",
            "description": "YZ Analiz: En zengin %10 koloninin %80'ine sahip. Eşitsizlik rekor seviyede. Sosyal huzursuzluk artıyor.",
            "options": [
                {
                    "id": "A",
                    "text": "Servet Vergisi: Zenginlerden %50 al",
                    "ethos": 0.5,
                    "pathos": 0.8,
                    "logos": 0.7,
                    "effects": {
                        "money": 1500,
                        "energy": 50,
                        "crime": 0.03
                    }
                },
                {
                    "id": "B",
                    "text": "Maksimum Gelir: Kimse belirli miktarın üstünü kazanamaz",
                    "ethos": 0.6,
                    "pathos": 0.7,
                    "logos": 0.6,
                    "effects": {
                        "money": 800,
                        "energy": 40,
                        "crime": 0.04
                    }
                },
                {
                    "id": "C",
                    "text": "Gönüllü Bağış: Zenginleri ikna et",
                    "ethos": 0.7,
                    "pathos": 0.5,
                    "logos": 0.5,
                    "effects": {
                        "money": 300,
                        "energy": 30,
                        "crime": 0.02
                    }
                }
            ]
        },
        {
            "id": "economy_007",
            "phase": "crisis",
            "title": "Enerji Kıtlığı Ekonomisi",
            "description": "YZ Analiz: Enerji üretimi düştü, fiyatlar uçtu. Fabrikalar durdu. Ekonomik çöküş riski var.",
            "options": [
                {
                    "id": "A",
                    "text": "Zorunlu Kesinti: Herkesin enerjisi %50 azalt",
                    "ethos": 0.8,
                    "pathos": 0.5,
                    "logos": 0.7,
                    "effects": {
                        "money": 400,
                        "energy": -100,
                        "crime": 0.05
                    }
                },
                {
                    "id": "B",
                    "text": "Piyasa Fiyatı: En çok ödeyenler kullansın",
                    "ethos": 0.6,
                    "pathos": 0.2,
                    "logos": 0.9,
                    "effects": {
                        "money": 800,
                        "energy": -50,
                        "crime": 0.06
                    }
                },
                {
                    "id": "C",
                    "text": "Acil Yatırım: Tüm kaynağı yeni jeneratöre",
                    "ethos": 0.5,
                    "pathos": 0.6,
                    "logos": 0.9,
                    "effects": {
                        "money": -2500,
                        "energy": 200,
                        "crime": 0.02
                    }
                }
            ]
        },
        {
            "id": "economy_008",
            "phase": "crisis",
            "title": "Borç Sarmalı",
            "description": "YZ Analiz: Koloni başlangıçta alınan kredilerle boğuşuyor. Ödemeler kaynak tüketiyor. Yeniden yapılandırma şart.",
            "options": [
                {
                    "id": "A",
                    "text": "Borcu Öde: Kemer sık, her şeyi geri ver",
                    "ethos": 0.8,
                    "pathos": 0.3,
                    "logos": 0.7,
                    "effects": {
                        "money": -3000,
                        "energy": 100,
                        "crime": 0.04
                    }
                },
                {
                    "id": "B",
                    "text": "Yeniden Müzakere: Vade ve faiz indirim talep et",
                    "ethos": 0.5,
                    "pathos": 0.6,
                    "logos": 0.8,
                    "effects": {
                        "money": -1000,
                        "energy": 50,
                        "crime": 0.01
                    }
                },
                {
                    "id": "C",
                    "text": "İflas İlan Et: Bağımsızlık, borç tanımıyoruz",
                    "ethos": 0.7,
                    "pathos": 0.5,
                    "logos": 0.5,
                    "effects": {
                        "money": 2000,
                        "energy": 60,
                        "crime": 0.06
                    }
                }
            ]
        },
        {
            "id": "economy_009",
            "phase": "crisis",
            "title": "Gıda Spekülatörü",
            "description": "YZ Analiz: Birkaç kişi gıda stoku biriktirip fiyat artırıyor. Açlık tehdidi var. Piyasa manipülasyonu.",
            "options": [
                {
                    "id": "A",
                    "text": "El Koy: Stokları kamulaştır",
                    "ethos": 0.8,
                    "pathos": 0.7,
                    "logos": 0.6,
                    "effects": {
                        "money": 600,
                        "energy": 40,
                        "crime": 0.04
                    }
                },
                {
                    "id": "B",
                    "text": "Ağır Vergi: Spekülasyonu cezalandır",
                    "ethos": 0.6,
                    "pathos": 0.6,
                    "logos": 0.8,
                    "effects": {
                        "money": 800,
                        "energy": 35,
                        "crime": 0.02
                    }
                },
                {
                    "id": "C",
                    "text": "Devlet Üretimi Artır: Piyasaya müdahale etme",
                    "ethos": 0.5,
                    "pathos": 0.5,
                    "logos": 0.9,
                    "effects": {
                        "money": -1200,
                        "energy": 100,
                        "crime": 0.0,
                        "environment": -0.02
                    }
                }
            ]
        },
        {
            "id": "economy_010",
            "phase": "crisis",
            "title": "Kripto Para Dolandırıcılığı",
            "description": "YZ Analiz: Bir grup 'KoloniCoin' adlı sahte kripto sattı. 200 kolonist birikimlerini kaybetti. Düzenleme gerekli.",
            "options": [
                {
                    "id": "A",
                    "text": "Kripto Yasağı: Tüm alternatif paralar illegal",
                    "ethos": 0.8,
                    "pathos": 0.5,
                    "logos": 0.6,
                    "effects": {
                        "money": -300,
                        "energy": 30,
                        "crime": -0.03
                    }
                },
                {
                    "id": "B",
                    "text": "Lisanslama: Sadece onaylı kriptolar",
                    "ethos": 0.6,
                    "pathos": 0.5,
                    "logos": 0.8,
                    "effects": {
                        "money": -500,
                        "energy": 40,
                        "crime": -0.01
                    }
                },
                {
                    "id": "C",
                    "text": "Eğitim: Finansal okuryazarlık programı",
                    "ethos": 0.4,
                    "pathos": 0.7,
                    "logos": 0.8,
                    "effects": {
                        "money": -700,
                        "energy": 50,
                        "crime": 0.0
                    }
                }
            ]
        },
        {
            "id": "economy_011",
            "phase": "crisis",
            "title": "Robot İşgücü Vergisi",
            "description": "YZ Analiz: İşsiz kalan işçiler robot sahiplerinin vergilendirilmesini talep ediyor. Teknoloji mi, insan mı?",
            "options": [
                {
                    "id": "A",
                    "text": "Robot Vergisi: Otomasyon maliyeti artsın",
                    "ethos": 0.5,
                    "pathos": 0.8,
                    "logos": 0.6,
                    "effects": {
                        "money": 1000,
                        "energy": 40,
                        "crime": 0.01
                    }
                },
                {
                    "id": "B",
                    "text": "Teknoloji Teşviki: Vergi muafiyeti, daha fazla otomasyon",
                    "ethos": 0.6,
                    "pathos": 0.3,
                    "logos": 0.9,
                    "effects": {
                        "money": -500,
                        "energy": 100,
                        "crime": 0.04
                    }
                },
                {
                    "id": "C",
                    "text": "İnsan-Robot Dengesi: %50 insan, %50 otomasyon zorunlu",
                    "ethos": 0.6,
                    "pathos": 0.6,
                    "logos": 0.7,
                    "effects": {
                        "money": -300,
                        "energy": 70,
                        "crime": 0.0
                    }
                }
            ]
        },
        {
            "id": "economy_012",
            "phase": "crisis",
            "title": "Dünya ile Ticaret Teklifi",
            "description": "YZ Analiz: Dünya nadir mineraller için cömert teklif sunuyor. Ama kaynaklarımız tükenir. Kabul mü, ret mi?",
            "options": [
                {
                    "id": "A",
                    "text": "Kabul Et: Para gerekli, sat gitsin",
                    "ethos": 0.6,
                    "pathos": 0.4,
                    "logos": 0.7,
                    "effects": {
                        "money": 5000,
                        "energy": 150,
                        "crime": 0.0,
                        "environment": -0.08
                    }
                },
                {
                    "id": "B",
                    "text": "Sınırlı Ticaret: Sadece yenilenebilir kaynaklar",
                    "ethos": 0.5,
                    "pathos": 0.6,
                    "logos": 0.8,
                    "effects": {
                        "money": 2000,
                        "energy": 80,
                        "crime": 0.0,
                        "environment": -0.03
                    }
                },
                {
                    "id": "C",
                    "text": "Reddet: Kendi kendine yeterlilik öncelik",
                    "ethos": 0.7,
                    "pathos": 0.5,
                    "logos": 0.6,
                    "effects": {
                        "money": -500,
                        "energy": 50,
                        "crime": 0.02,
                        "environment": 0.02
                    }
                }
            ]
        }
    ],
    
    "🏛️ İçişleri": [
        # === KURULUM FAZLARI ===
        {
            "id": "internal_001",
            "phase": "setup",
            "title": "Vatandaşlık Tanımı",
            "description": "YZ Analiz: Kolonide 'vatandaş' kim? Hak ve sorumluluklar nasıl belirlenmeli?",
            "options": [
                {
                    "id": "A",
                    "text": "Doğuştan Hak: Kolonide doğan herkes vatandaş",
                    "ethos": 0.5,
                    "pathos": 0.8,
                    "logos": 0.7,
                    "effects": {
                        "money": -300,
                        "energy": 30,
                        "crime": 0.0
                    }
                },
                {
                    "id": "B",
                    "text": "Kazanılmış Hak: Koloniye katkı sonrası vatandaşlık",
                    "ethos": 0.7,
                    "pathos": 0.4,
                    "logos": 0.7,
                    "effects": {
                        "money": -200,
                        "energy": 25,
                        "crime": 0.02
                    }
                },
                {
                    "id": "C",
                    "text": "Evrensel: Tüm insanlar eşit haklara sahip",
                    "ethos": 0.3,
                    "pathos": 0.9,
                    "logos": 0.6,
                    "effects": {
                        "money": -400,
                        "energy": 35,
                        "crime": 0.0
                    }
                }
            ]
        },
        {
            "id": "internal_002",
            "phase": "setup",
            "title": "Medya ve İfade Özgürlüğü",
            "description": "YZ Analiz: Koloni içi haberleşme ve yayın sistemi kurulacak. Kontrol seviyesi belirlenmeli.",
            "options": [
                {
                    "id": "A",
                    "text": "Serbest Basın: Sansür yok, herkes yayın yapabilir",
                    "ethos": 0.3,
                    "pathos": 0.7,
                    "logos": 0.8,
                    "effects": {
                        "money": -400,
                        "energy": 40,
                        "crime": 0.02
                    }
                },
                {
                    "id": "B",
                    "text": "Devlet Kontrolü: Resmi yayın organı, onaylı içerik",
                    "ethos": 0.8,
                    "pathos": 0.3,
                    "logos": 0.6,
                    "effects": {
                        "money": -600,
                        "energy": 50,
                        "crime": -0.03
                    }
                },
                {
                    "id": "C",
                    "text": "Öz-Düzenleme: Yayıncılar kendi etik kurallarını koyar",
                    "ethos": 0.5,
                    "pathos": 0.6,
                    "logos": 0.7,
                    "effects": {
                        "money": -300,
                        "energy": 35,
                        "crime": 0.01
                    }
                }
            ]
        },
        {
            "id": "internal_003",
            "phase": "setup",
            "title": "Nüfus Kayıt Sistemi",
            "description": "YZ Analiz: Her kolonistin kimlik ve aktivite kaydı tutulmalı mı? Mahremiyet vs güvenlik dengesi.",
            "options": [
                {
                    "id": "A",
                    "text": "Tam Kayıt: Tüm hareketler izlenir",
                    "ethos": 0.8,
                    "pathos": 0.3,
                    "logos": 0.8,
                    "effects": {
                        "money": -1000,
                        "energy": 80,
                        "crime": -0.06
                    }
                },
                {
                    "id": "B",
                    "text": "Temel Bilgiler: Sadece kimlik ve iletişim",
                    "ethos": 0.5,
                    "pathos": 0.6,
                    "logos": 0.7,
                    "effects": {
                        "money": -400,
                        "energy": 40,
                        "crime": -0.02
                    }
                },
                {
                    "id": "C",
                    "text": "Gönüllü: İsteyen kayıt olur",
                    "ethos": 0.3,
                    "pathos": 0.8,
                    "logos": 0.5,
                    "effects": {
                        "money": -200,
                        "energy": 25,
                        "crime": 0.03
                    }
                }
            ]
        },
        
        # === SORUN VE TALEPLER ===
        {
            "id": "internal_004",
            "phase": "crisis",
            "title": "Yabancı Dil Meselesi",
            "description": "YZ Analiz: Farklı dillerden kolonistler kendi dillerinde eğitim istiyor. Birlik mi, çeşitlilik mi?",
            "options": [
                {
                    "id": "A",
                    "text": "Tek Dil Politikası: Sadece ortak dil konuşulsun",
                    "ethos": 0.8,
                    "pathos": 0.3,
                    "logos": 0.7,
                    "effects": {
                        "money": -500,
                        "energy": 40,
                        "crime": 0.03
                    }
                },
                {
                    "id": "B",
                    "text": "Çok Dilli: Tüm dillerde hizmet",
                    "ethos": 0.3,
                    "pathos": 0.9,
                    "logos": 0.6,
                    "effects": {
                        "money": -1200,
                        "energy": 80,
                        "crime": 0.0
                    }
                },
                {
                    "id": "C",
                    "text": "Ortak Dil + Ev Dili: İkili sistem",
                    "ethos": 0.5,
                    "pathos": 0.7,
                    "logos": 0.8,
                    "effects": {
                        "money": -700,
                        "energy": 60,
                        "crime": 0.01
                    }
                }
            ]
        },
        {
            "id": "internal_005",
            "phase": "crisis",
            "title": "İsim Değiştirme Talebi",
            "description": "YZ Analiz: Uzayda doğan nesil 'koloni isimleri' istiyor. Dünya isimleri eski diyorlar. Kimlik krizi başladı.",
            "options": [
                {
                    "id": "A",
                    "text": "Serbest Bırak: Herkes istediği ismi seçsin",
                    "ethos": 0.3,
                    "pathos": 0.8,
                    "logos": 0.7,
                    "effects": {
                        "money": -300,
                        "energy": 30,
                        "crime": 0.01
                    }
                },
                {
                    "id": "B",
                    "text": "Geleneklere Bağlı Kal: Değiştirme yasak",
                    "ethos": 0.8,
                    "pathos": 0.3,
                    "logos": 0.5,
                    "effects": {
                        "money": -100,
                        "energy": 20,
                        "crime": 0.03
                    }
                },
                {
                    "id": "C",
                    "text": "18 Yaş Sonrası: Reşit olunca karar verilsin",
                    "ethos": 0.6,
                    "pathos": 0.6,
                    "logos": 0.7,
                    "effects": {
                        "money": -200,
                        "energy": 25,
                        "crime": 0.01
                    }
                }
            ]
        },
        {
            "id": "internal_006",
            "phase": "crisis",
            "title": "Propaganda Suçlaması",
            "description": "YZ Analiz: Resmi yayın organı hükümeti övüyor, eleştirileri görmezden geliyor. Propaganda mı, bilgilendirme mi?",
            "options": [
                {
                    "id": "A",
                    "text": "Bağımsız Denetim: Medya kurulu oluştur",
                    "ethos": 0.4,
                    "pathos": 0.7,
                    "logos": 0.8,
                    "effects": {
                        "money": -600,
                        "energy": 45,
                        "crime": 0.0
                    }
                },
                {
                    "id": "B",
                    "text": "Muhalefete Yer Ver: Zorunlu dengeli yayın",
                    "ethos": 0.5,
                    "pathos": 0.8,
                    "logos": 0.7,
                    "effects": {
                        "money": -400,
                        "energy": 40,
                        "crime": 0.01
                    }
                },
                {
                    "id": "C",
                    "text": "Devam Et: Moral için olumlu haber gerekli",
                    "ethos": 0.7,
                    "pathos": 0.4,
                    "logos": 0.5,
                    "effects": {
                        "money": -200,
                        "energy": 30,
                        "crime": 0.03
                    }
                }
            ]
        },
        {
            "id": "internal_007",
            "phase": "crisis",
            "title": "Cinsiyet Kimliği Tartışması",
            "description": "YZ Analiz: Bazı kolonistler resmi kayıtlarda cinsiyet tanımlarının genişletilmesini talep ediyor. Kabul mü, ret mi?",
            "options": [
                {
                    "id": "A",
                    "text": "Geniş Tanım: Bireysel kimlik tercihleri kabul",
                    "ethos": 0.3,
                    "pathos": 0.9,
                    "logos": 0.7,
                    "effects": {
                        "money": -400,
                        "energy": 35,
                        "crime": 0.0
                    }
                },
                {
                    "id": "B",
                    "text": "Biyolojik Cinsiyet: Sadece iki kategori",
                    "ethos": 0.8,
                    "pathos": 0.3,
                    "logos": 0.6,
                    "effects": {
                        "money": -100,
                        "energy": 20,
                        "crime": 0.03
                    }
                },
                {
                    "id": "C",
                    "text": "Cinsiyet Kaydı Kaldır: Kimlikte belirtilmesin",
                    "ethos": 0.4,
                    "pathos": 0.7,
                    "logos": 0.8,
                    "effects": {
                        "money": -300,
                        "energy": 30,
                        "crime": 0.01
                    }
                }
            ]
        },
        {
            "id": "internal_008",
            "phase": "crisis",
            "title": "Mahremiyet İhlali Skandalı",
            "description": "YZ Analiz: Yöneticilerin özel yaşam alanlarını gözetlediği ortaya çıktı. Kamuoyu öfkeli. İstifa talepleri var.",
            "options": [
                {
                    "id": "A",
                    "text": "Toplu İstifa: Sorumlular görevden alınsın",
                    "ethos": 0.5,
                    "pathos": 0.8,
                    "logos": 0.7,
                    "effects": {
                        "money": -800,
                        "energy": 60,
                        "crime": -0.02
                    }
                },
                {
                    "id": "B",
                    "text": "Özür ve Reform: Gözetim yasaları değişsin",
                    "ethos": 0.6,
                    "pathos": 0.7,
                    "logos": 0.8,
                    "effects": {
                        "money": -600,
                        "energy": 50,
                        "crime": 0.0
                    }
                },
                {
                    "id": "C",
                    "text": "Güvenlik Gerekçesi: Gözetim şarttı, devam",
                    "ethos": 0.8,
                    "pathos": 0.3,
                    "logos": 0.7,
                    "effects": {
                        "money": -300,
                        "energy": 35,
                        "crime": -0.04
                    }
                }
            ]
        },
        {
            "id": "internal_009",
            "phase": "crisis",
            "title": "Dini Ayrımcılık İddiası",
            "description": "YZ Analiz: Belirli dini grubun işe alımlarda dışlandığı iddia ediliyor. Ayrımcılık mı, tesadüf mü?",
            "options": [
                {
                    "id": "A",
                    "text": "Bağımsız Soruşturma: Tam inceleme yap",
                    "ethos": 0.5,
                    "pathos": 0.8,
                    "logos": 0.8,
                    "effects": {
                        "money": -700,
                        "energy": 50,
                        "crime": 0.0
                    }
                },
                {
                    "id": "B",
                    "text": "Kota Sistemi: Her gruba orantılı istihdam",
                    "ethos": 0.6,
                    "pathos": 0.7,
                    "logos": 0.6,
                    "effects": {
                        "money": -500,
                        "energy": 45,
                        "crime": 0.02
                    }
                },
                {
                    "id": "C",
                    "text": "Liyakat Odaklı: Din kayıtları silinsin",
                    "ethos": 0.7,
                    "pathos": 0.5,
                    "logos": 0.9,
                    "effects": {
                        "money": -300,
                        "energy": 35,
                        "crime": 0.01
                    }
                }
            ]
        },
        {
            "id": "internal_010",
            "phase": "crisis",
            "title": "Yaşlıların Oy Hakkı",
            "description": "YZ Analiz: Gençler 'geleceği görmeyecekler neden karar veriyorlar' diyor. Yaşlıların oy hakkı tartışılıyor.",
            "options": [
                {
                    "id": "A",
                    "text": "Üst Yaş Sınırı: 75 yaş üstü oy kullanamaz",
                    "ethos": 0.6,
                    "pathos": 0.2,
                    "logos": 0.7,
                    "effects": {
                        "money": -200,
                        "energy": 25,
                        "crime": 0.05
                    }
                },
                {
                    "id": "B",
                    "text": "Eşit Haklar: Yaş ayırımı yapılamaz",
                    "ethos": 0.5,
                    "pathos": 0.9,
                    "logos": 0.6,
                    "effects": {
                        "money": -100,
                        "energy": 20,
                        "crime": 0.0
                    }
                },
                {
                    "id": "C",
                    "text": "Ağırlıklı Oy: Gençlerin oyu daha değerli",
                    "ethos": 0.5,
                    "pathos": 0.4,
                    "logos": 0.8,
                    "effects": {
                        "money": -400,
                        "energy": 35,
                        "crime": 0.04
                    }
                }
            ]
        },
        {
            "id": "internal_011",
            "phase": "crisis",
            "title": "Yeni Bayrak Tasarımı",
            "description": "YZ Analiz: Dünya bayraklarından bağımsız, koloni bayrağı talebi var. Kimlik inşası mı, bölünme mi?",
            "options": [
                {
                    "id": "A",
                    "text": "Yeni Bayrak: Koloni kimliği oluştur",
                    "ethos": 0.6,
                    "pathos": 0.7,
                    "logos": 0.6,
                    "effects": {
                        "money": -300,
                        "energy": 30,
                        "crime": 0.01
                    }
                },
                {
                    "id": "B",
                    "text": "Dünya Bayrağı: Birliği simgele",
                    "ethos": 0.7,
                    "pathos": 0.6,
                    "logos": 0.6,
                    "effects": {
                        "money": -100,
                        "energy": 20,
                        "crime": 0.0
                    }
                },
                {
                    "id": "C",
                    "text": "Hibrit Tasarım: İkisini birleştir",
                    "ethos": 0.5,
                    "pathos": 0.8,
                    "logos": 0.7,
                    "effects": {
                        "money": -200,
                        "energy": 25,
                        "crime": 0.0
                    }
                }
            ]
        },
        {
            "id": "internal_012",
            "phase": "crisis",
            "title": "Koloni Anayasası Revizyonu",
            "description": "YZ Analiz: İlk anayasa 10 yıl önce yazıldı. Şartlar değişti. Yeniden yazma talebi güçleniyor.",
            "options": [
                {
                    "id": "A",
                    "text": "Kurucu Meclis: Seçilmiş delegeler yeniden yazsın",
                    "ethos": 0.5,
                    "pathos": 0.8,
                    "logos": 0.7,
                    "effects": {
                        "money": -1000,
                        "energy": 80,
                        "crime": 0.0
                    }
                },
                {
                    "id": "B",
                    "text": "Referandum: Madde madde halk oylasın",
                    "ethos": 0.4,
                    "pathos": 0.9,
                    "logos": 0.6,
                    "effects": {
                        "money": -1200,
                        "energy": 100,
                        "crime": 0.01
                    }
                },
                {
                    "id": "C",
                    "text": "Mevcut Koruma: İstikrar için değişim yapma",
                    "ethos": 0.8,
                    "pathos": 0.4,
                    "logos": 0.6,
                    "effects": {
                        "money": -200,
                        "energy": 25,
                        "crime": 0.03
                    }
                }
            ]
        }
    ],
    "🌍 Dışişleri": [
        # === KURULUM FAZLARI ===
        {
            "id": "foreign_001",
            "phase": "setup",
            "title": "Diplomatik Duruş",
            "description": "YZ Analiz: Diğer uzay kolonileri ve Dünya ile ilişkilerimizi tanımlama zamanı. Temel politika ne olmalı?",
            "options": [
                {
                    "id": "A",
                    "text": "İzolasyonist: Minimum temas, kendi kendine yeterlik",
                    "ethos": 0.8,
                    "pathos": 0.4,
                    "logos": 0.6,
                    "effects": {
                        "money": -300,
                        "energy": 40,
                        "crime": 0.0
                    }
                },
                {
                    "id": "B",
                    "text": "Aktif Diplomasi: İşbirliği ve ittifak arayışı",
                    "ethos": 0.4,
                    "pathos": 0.7,
                    "logos": 0.8,
                    "effects": {
                        "money": -800,
                        "energy": 60,
                        "crime": 0.0
                    }
                },
                {
                    "id": "C",
                    "text": "Seçici İlişkiler: Sadece faydalı ortaklarla",
                    "ethos": 0.6,
                    "pathos": 0.5,
                    "logos": 0.9,
                    "effects": {
                        "money": -500,
                        "energy": 50,
                        "crime": 0.0
                    }
                }
            ]
        },
        {
            "id": "foreign_002",
            "phase": "setup",
            "title": "Ticaret Politikası",
            "description": "YZ Analiz: Dış ticaret kuralları belirlenmeli. Ne kadar açık, ne kadar korumacı olmalıyız?",
            "options": [
                {
                    "id": "A",
                    "text": "Serbest Ticaret: Sınırsız ithalat-ihracat",
                    "ethos": 0.5,
                    "pathos": 0.4,
                    "logos": 0.9,
                    "effects": {
                        "money": 800,
                        "energy": 80,
                        "crime": 0.01,
                        "environment": -0.02
                    }
                },
                {
                    "id": "B",
                    "text": "Korunan Ekonomi: Yüksek gümrük, yerli üretim",
                    "ethos": 0.7,
                    "pathos": 0.6,
                    "logos": 0.6,
                    "effects": {
                        "money": -400,
                        "energy": 50,
                        "crime": 0.0
                    }
                },
                {
                    "id": "C",
                    "text": "Stratejik Ticaret: Sadece kritik olmayan mallar",
                    "ethos": 0.6,
                    "pathos": 0.5,
                    "logos": 0.8,
                    "effects": {
                        "money": 200,
                        "energy": 60,
                        "crime": 0.0
                    }
                }
            ]
        },
        {
            "id": "foreign_003",
            "phase": "setup",
            "title": "Göç Politikası",
            "description": "YZ Analiz: Diğer kolonilerden göç talebi var. Kapılarımızı açmalı mıyız?",
            "options": [
                {
                    "id": "A",
                    "text": "Açık Kapı: Herkes hoş gelsin",
                    "ethos": 0.3,
                    "pathos": 0.9,
                    "logos": 0.5,
                    "effects": {
                        "money": -600,
                        "energy": 100,
                        "crime": 0.04
                    }
                },
                {
                    "id": "B",
                    "text": "Kalifiye Göç: Sadece yetenekli profesyoneller",
                    "ethos": 0.7,
                    "pathos": 0.4,
                    "logos": 0.9,
                    "effects": {
                        "money": 400,
                        "energy": 60,
                        "crime": 0.01
                    }
                },
                {
                    "id": "C",
                    "text": "Kapalı Sınır: Göç kabul etmiyoruz",
                    "ethos": 0.8,
                    "pathos": 0.2,
                    "logos": 0.6,
                    "effects": {
                        "money": 200,
                        "energy": 30,
                        "crime": 0.0
                    }
                }
            ]
        },
        
        # === SORUN VE TALEPLER ===
        {
            "id": "foreign_004",
            "phase": "crisis",
            "title": "Komşu Koloni Çöküşü",
            "description": "ACIL - YZ Analiz: 100km uzaktaki koloni yaşam desteği kaybetti. 500 kişi yardım bekliyor. Kaynaklarımız kısıtlı.",
            "options": [
                {
                    "id": "A",
                    "text": "Tam Kurtarma: Herkesi al, paylaş",
                    "ethos": 0.4,
                    "pathos": 0.9,
                    "logos": 0.5,
                    "effects": {
                        "money": -2000,
                        "energy": 200,
                        "crime": 0.05
                    }
                },
                {
                    "id": "B",
                    "text": "Seçici Yardım: Sadece kritik yetenekler",
                    "ethos": 0.7,
                    "pathos": 0.3,
                    "logos": 0.8,
                    "effects": {
                        "money": -800,
                        "energy": 80,
                        "crime": 0.02
                    }
                },
                {
                    "id": "C",
                    "text": "Sadece İlaç Gönder: Kendimizi riske atmayalım",
                    "ethos": 0.8,
                    "pathos": 0.4,
                    "logos": 0.7,
                    "effects": {
                        "money": -300,
                        "energy": 40,
                        "crime": 0.06
                    }
                }
            ]
        },
        {
            "id": "foreign_005",
            "phase": "crisis",
            "title": "Dünya Yeni Vergi İstiyor",
            "description": "YZ Analiz: Dünya hükümetleri kolonilere 'uzay vergisi' getirmeyi planlıyor. Ödeme mi, isyan mı?",
            "options": [
                {
                    "id": "A",
                    "text": "Öde ve Devam: İlişkileri bozma",
                    "ethos": 0.7,
                    "pathos": 0.5,
                    "logos": 0.6,
                    "effects": {
                        "money": -1500,
                        "energy": 50,
                        "crime": 0.02
                    }
                },
                {
                    "id": "B",
                    "text": "Müzakere: İndirim talep et",
                    "ethos": 0.6,
                    "pathos": 0.6,
                    "logos": 0.8,
                    "effects": {
                        "money": -800,
                        "energy": 60,
                        "crime": 0.01
                    }
                },
                {
                    "id": "C",
                    "text": "Bağımsızlık İlan Et: Artık Dünya'ya bağlı değiliz",
                    "ethos": 0.8,
                    "pathos": 0.6,
                    "logos": 0.6,
                    "effects": {
                        "money": 0,
                        "energy": 80,
                        "crime": 0.07
                    }
                }
            ]
        },
        {
            "id": "foreign_006",
            "phase": "crisis",
            "title": "Ticaret Ambargos Tehdidi",
            "description": "YZ Analiz: Büyük bir Dünya bloğu insan hakları ihlali gerekçesiyle ambargo tehdidi savuruyor. Teslim mi, direniş mi?",
            "options": [
                {
                    "id": "A",
                    "text": "Reform Yap: Talepleri kabul et",
                    "ethos": 0.5,
                    "pathos": 0.7,
                    "logos": 0.7,
                    "effects": {
                        "money": -600,
                        "energy": 50,
                        "crime": 0.0
                    }
                },
                {
                    "id": "B",
                    "text": "Alternatif Ortaklar Bul: Başka ülkelerle anlaş",
                    "ethos": 0.6,
                    "pathos": 0.5,
                    "logos": 0.9,
                    "effects": {
                        "money": -1000,
                        "energy": 80,
                        "crime": 0.01
                    }
                },
                {
                    "id": "C",
                    "text": "Karşı Ambargo: Biz de onları boykot et",
                    "ethos": 0.8,
                    "pathos": 0.4,
                    "logos": 0.5,
                    "effects": {
                        "money": -1500,
                        "energy": 100,
                        "crime": 0.05
                    }
                }
            ]
        },
        {
            "id": "foreign_007",
            "phase": "crisis",
            "title": "Casusuk İddiası",
            "description": "YZ Analiz: Bir kolonist rakip koloniye bilgi sızdırmakla suçlanıyor. Diplomatik kriz doğabilir.",
            "options": [
                {
                    "id": "A",
                    "text": "Gizli Yargılama: Sessizce halledelim",
                    "ethos": 0.7,
                    "pathos": 0.4,
                    "logos": 0.7,
                    "effects": {
                        "money": -400,
                        "energy": 40,
                        "crime": -0.02
                    }
                },
                {
                    "id": "B",
                    "text": "Açık Duruşma: Şeffaflık gösterelim",
                    "ethos": 0.5,
                    "pathos": 0.7,
                    "logos": 0.8,
                    "effects": {
                        "money": -600,
                        "energy": 50,
                        "crime": 0.01
                    }
                },
                {
                    "id": "C",
                    "text": "Sınır Dışı Et: Sorunu dışarıya at",
                    "ethos": 0.8,
                    "pathos": 0.3,
                    "logos": 0.6,
                    "effects": {
                        "money": -200,
                        "energy": 30,
                        "crime": 0.0
                    }
                }
            ]
        },
        {
            "id": "foreign_008",
            "phase": "crisis",
            "title": "Mülteci Dalgası",
            "description": "YZ Analiz: Savaştan kaçan 200 mülteci sınırlarımıza geldi. İnsani yardım mı, sınır güvenliği mi?",
            "options": [
                {
                    "id": "A",
                    "text": "Hepsini Kabul Et: İnsani görev",
                    "ethos": 0.4,
                    "pathos": 0.9,
                    "logos": 0.5,
                    "effects": {
                        "money": -1200,
                        "energy": 120,
                        "crime": 0.03
                    }
                },
                {
                    "id": "B",
                    "text": "Geçici Kamp: Durum düzelene kadar barındır",
                    "ethos": 0.6,
                    "pathos": 0.7,
                    "logos": 0.7,
                    "effects": {
                        "money": -800,
                        "energy": 80,
                        "crime": 0.02
                    }
                },
                {
                    "id": "C",
                    "text": "Geri Gönder: Kapasitemiz yok",
                    "ethos": 0.8,
                    "pathos": 0.2,
                    "logos": 0.6,
                    "effects": {
                        "money": -200,
                        "energy": 30,
                        "crime": 0.05
                    }
                }
            ]
        },
        {
            "id": "foreign_009",
            "phase": "crisis",
            "title": "Uzay Anlaşması Teklifi",
            "description": "YZ Analiz: Diğer koloniler 'Uzay Barış Paktı' imzalıyor. Bize de katılma teklifi geldi. Bağlayıcı kurallar var.",
            "options": [
                {
                    "id": "A",
                    "text": "İmzala: Uluslararası topluma katıl",
                    "ethos": 0.5,
                    "pathos": 0.7,
                    "logos": 0.8,
                    "effects": {
                        "money": -600,
                        "energy": 50,
                        "crime": -0.02
                    }
                },
                {
                    "id": "B",
                    "text": "Şartlı İmza: Bazı maddeler için istisna talep et",
                    "ethos": 0.6,
                    "pathos": 0.6,
                    "logos": 0.8,
                    "effects": {
                        "money": -800,
                        "energy": 60,
                        "crime": 0.0
                    }
                },
                {
                    "id": "C",
                    "text": "İmzalama: Egemenliğimizi koruyalım",
                    "ethos": 0.8,
                    "pathos": 0.4,
                    "logos": 0.6,
                    "effects": {
                        "money": -200,
                        "energy": 30,
                        "crime": 0.03
                    }
                }
            ]
        },
        {
            "id": "foreign_010",
            "phase": "crisis",
            "title": "Teknoloji Transferi Talebi",
            "description": "YZ Analiz: Gelişmekte olan bir koloni bizden yaşam destek teknolojisi istiyor. Paylaşmak rekabet avantajını kaybettirir.",
            "options": [
                {
                    "id": "A",
                    "text": "Ücretsiz Paylaş: Dayanışma göster",
                    "ethos": 0.4,
                    "pathos": 0.9,
                    "logos": 0.6,
                    "effects": {
                        "money": -400,
                        "energy": 40,
                        "crime": 0.0
                    }
                },
                {
                    "id": "B",
                    "text": "Ücretli Sat: Ticari anlaşma yap",
                    "ethos": 0.6,
                    "pathos": 0.4,
                    "logos": 0.9,
                    "effects": {
                        "money": 1200,
                        "energy": 60,
                        "crime": 0.0
                    }
                },
                {
                    "id": "C",
                    "text": "Reddet: Stratejik üstünlüğü koru",
                    "ethos": 0.8,
                    "pathos": 0.3,
                    "logos": 0.7,
                    "effects": {
                        "money": 0,
                        "energy": 20,
                        "crime": 0.02
                    }
                }
            ]
        },
        {
            "id": "foreign_011",
            "phase": "crisis",
            "title": "Dünya Medya İlgisi",
            "description": "YZ Analiz: Dünya medyası kolonimizi 'distopya' olarak gösteriyor. İmajımızı düzeltmeli miyiz?",
            "options": [
                {
                    "id": "A",
                    "text": "Halkla İlişkiler Kampanyası: Profesyonel imaj yönetimi",
                    "ethos": 0.6,
                    "pathos": 0.6,
                    "logos": 0.8,
                    "effects": {
                        "money": -1000,
                        "energy": 70,
                        "crime": 0.0
                    }
                },
                {
                    "id": "B",
                    "text": "Gazeteci Davet Et: Şeffaflık göster",
                    "ethos": 0.5,
                    "pathos": 0.7,
                    "logos": 0.7,
                    "effects": {
                        "money": -600,
                        "energy": 50,
                        "crime": 0.01
                    }
                },
                {
                    "id": "C",
                    "text": "Görmezden Gel: Dünya fikri önemli değil",
                    "ethos": 0.8,
                    "pathos": 0.4,
                    "logos": 0.6,
                    "effects": {
                        "money": -100,
                        "energy": 20,
                        "crime": 0.02
                    }
                }
            ]
        },
        {
            "id": "foreign_012",
            "phase": "crisis",
            "title": "Koloni Federasyonu Teklifi",
            "description": "YZ Analiz: 5 koloni birleşip konfederasyon kurmayı teklif ediyor. Ortak savunma, ticaret. Ama kısmi egemenlik kaybı.",
            "options": [
                {
                    "id": "A",
                    "text": "Tam Üyelik: Federasyona katıl",
                    "ethos": 0.5,
                    "pathos": 0.7,
                    "logos": 0.8,
                    "effects": {
                        "money": -1000,
                        "energy": 80,
                        "crime": -0.03
                    }
                },
                {
                    "id": "B",
                    "text": "Gözlemci Statü: Kararlar bağlamaz",
                    "ethos": 0.6,
                    "pathos": 0.6,
                    "logos": 0.7,
                    "effects": {
                        "money": -400,
                        "energy": 40,
                        "crime": 0.0
                    }
                },
                {
                    "id": "C",
                    "text": "Tek Başına Dur: Bağımsızlık şart",
                    "ethos": 0.8,
                    "pathos": 0.4,
                    "logos": 0.6,
                    "effects": {
                        "money": -200,
                        "energy": 30,
                        "crime": 0.03
                    }
                }
            ]
        }
    ],
    
    "🌱 Çevre": [
        # === KURULUM FAZLARI ===
        {
            "id": "environment_001",
            "phase": "setup",
            "title": "Enerji Kaynak Seçimi",
            "description": "YZ Analiz: Koloninin enerji ihtiyacı için uzun vadeli çözüm şart. 3 ana seçenek var.",
            "options": [
                {
                    "id": "A",
                    "text": "Güneş Panelleri: Temiz ama düşük verim",
                    "ethos": 0.5,
                    "pathos": 0.7,
                    "logos": 0.7,
                    "effects": {
                        "money": -1500,
                        "energy": 100,
                        "environment": 0.05
                    }
                },
                {
                    "id": "B",
                    "text": "Nükleer Füzyon: Yüksek verim, yüksek risk",
                    "ethos": 0.6,
                    "pathos": 0.4,
                    "logos": 0.9,
                    "effects": {
                        "money": -3000,
                        "energy": 300,
                        "environment": 0.02
                    }
                },
                {
                    "id": "C",
                    "text": "Hibrit Sistem: Her ikisini birleştir",
                    "ethos": 0.5,
                    "pathos": 0.6,
                    "logos": 0.8,
                    "effects": {
                        "money": -2000,
                        "energy": 180,
                        "environment": 0.04
                    }
                }
            ]
        },
        {
            "id": "environment_002",
            "phase": "setup",
            "title": "Su Geri Dönüşüm Sistemi",
            "description": "YZ Analiz: Su kaynakları sınırlı. %99 geri dönüşüm hedefleniyor. Teknoloji seviyesi?",
            "options": [
                {
                    "id": "A",
                    "text": "Temel Filtrasyon: Ucuz ama %85 verim",
                    "ethos": 0.7,
                    "pathos": 0.5,
                    "logos": 0.6,
                    "effects": {
                        "money": -800,
                        "energy": 60,
                        "environment": 0.03
                    }
                },
                {
                    "id": "B",
                    "text": "İleri Teknoloji: Pahalı ama %98 verim",
                    "ethos": 0.5,
                    "pathos": 0.6,
                    "logos": 0.9,
                    "effects": {
                        "money": -2000,
                        "energy": 120,
                        "environment": 0.06
                    }
                },
                {
                    "id": "C",
                    "text": "Biyolojik Sistem: Bitkiler ve bakterilerle doğal temizlik",
                    "ethos": 0.4,
                    "pathos": 0.8,
                    "logos": 0.7,
                    "effects": {
                        "money": -1200,
                        "energy": 80,
                        "environment": 0.08
                    }
                }
            ]
        },
        {
            "id": "environment_003",
            "phase": "setup",
            "title": "Atık Yönetim Stratejisi",
            "description": "YZ Analiz: Günlük atık miktarı artıyor. Uzay'da çöp sahamız yok. Çözüm?",
            "options": [
                {
                    "id": "A",
                    "text": "Geri Dönüşüm Merkezi: Her şey ayrıştırılıp yeniden kullanılır",
                    "ethos": 0.5,
                    "pathos": 0.7,
                    "logos": 0.8,
                    "effects": {
                        "money": -1500,
                        "energy": 100,
                        "environment": 0.08
                    }
                },
                {
                    "id": "B",
                    "text": "Plazma Yakma: Atıklar enerjiye dönüştürülür",
                    "ethos": 0.6,
                    "pathos": 0.5,
                    "logos": 0.9,
                    "effects": {
                        "money": -2000,
                        "energy": 150,
                        "environment": 0.03
                    }
                },
                {
                    "id": "C",
                    "text": "Uzaya Fırlatma: Güneş'e doğru yolla",
                    "ethos": 0.7,
                    "pathos": 0.3,
                    "logos": 0.6,
                    "effects": {
                        "money": -1000,
                        "energy": 120,
                        "environment": -0.02
                    }
                }
            ]
        },
        
        # === SORUN VE TALEPLER ===
        {
            "id": "environment_004",
            "phase": "crisis",
            "title": "Hava Kalitesi Krizi",
            "description": "ACIL - YZ Analiz: CO2 seviyeleri %30 arttı. İnsanlar baş ağrısı ve yorgunluk yaşıyor. Oksijen üretimi yetersiz.",
            "options": [
                {
                    "id": "A",
                    "text": "Acil Sera İnşaatı: 10 kat fazla bitki",
                    "ethos": 0.6,
                    "pathos": 0.7,
                    "logos": 0.8,
                    "effects": {
                        "money": -2500,
                        "energy": 200,
                        "environment": 0.10
                    }
                },
                {
                    "id": "B",
                    "text": "Kimyasal Temizleyiciler: Hızlı ama pahalı",
                    "ethos": 0.7,
                    "pathos": 0.5,
                    "logos": 0.8,
                    "effects": {
                        "money": -3000,
                        "energy": 250,
                        "environment": 0.06
                    }
                },
                {
                    "id": "C",
                    "text": "Nüfus Rasyonlaması: Kişi başı oksijen limiti",
                    "ethos": 0.8,
                    "pathos": 0.3,
                    "logos": 0.7,
                    "effects": {
                        "money": -500,
                        "energy": 60,
                        "crime": 0.06,
                        "environment": 0.03
                    }
                }
            ]
        },
        {
            "id": "environment_005",
            "phase": "crisis",
            "title": "Su Sızıntısı Felaketi",
            "description": "YZ Analiz: Ana su tankında sızıntı. %40 rezerv kaybedildi. Kritik durum. Su rasyonu şart.",
            "options": [
                {
                    "id": "A",
                    "text": "Sıkı Rasyon: Kişi başı 2 litre/gün",
                    "ethos": 0.8,
                    "pathos": 0.5,
                    "logos": 0.7,
                    "effects": {
                        "money": -400,
                        "energy": 50,
                        "crime": 0.05,
                        "environment": 0.0
                    }
                },
                {
                    "id": "B",
                    "text": "Acil Madencilik: Buzullardan su çıkar",
                    "ethos": 0.6,
                    "pathos": 0.6,
                    "logos": 0.9,
                    "effects": {
                        "money": -2000,
                        "energy": 180,
                        "crime": 0.0,
                        "environment": -0.05
                    }
                },
                {
                    "id": "C",
                    "text": "Dünya'dan İthalat: Acil su takviyesi iste",
                    "ethos": 0.7,
                    "pathos": 0.6,
                    "logos": 0.7,
                    "effects": {
                        "money": -3500,
                        "energy": 150,
                        "crime": 0.0,
                        "environment": 0.0
                    }
                }
            ]
        },
        {
            "id": "environment_006",
            "phase": "crisis",
            "title": "Sera Hastalığı",
            "description": "YZ Analiz: Tüm seralarda mantar salgını. Bitkiler ölüyor. Gıda ve oksijen krizi aynı anda.",
            "options": [
                {
                    "id": "A",
                    "text": "Kimyasal İlaçlama: Ağır ilaçlarla müdahale",
                    "ethos": 0.7,
                    "pathos": 0.5,
                    "logos": 0.8,
                    "effects": {
                        "money": -1500,
                        "energy": 100,
                        "environment": -0.04
                    }
                },
                {
                    "id": "B",
                    "text": "Tümünü Yak: Sıfırdan steril başlangıç",
                    "ethos": 0.8,
                    "pathos": 0.4,
                    "logos": 0.7,
                    "effects": {
                        "money": -2500,
                        "energy": 200,
                        "crime": 0.03,
                        "environment": -0.02
                    }
                },
                {
                    "id": "C",
                    "text": "Biyolojik Kontrol: Doğal düşmanlarla savaş",
                    "ethos": 0.5,
                    "pathos": 0.7,
                    "logos": 0.8,
                    "effects": {
                        "money": -1800,
                        "energy": 120,
                        "environment": 0.03
                    }
                }
            ]
        },
        {
            "id": "environment_007",
            "phase": "crisis",
            "title": "Toprak Tükenme",
            "description": "YZ Analiz: Sera toprağı besin değerini kaybetti. Verim %60 düştü. Yeni toprak lazım ama nereden?",
            "options": [
                {
                    "id": "A",
                    "text": "Hidroponik Sistem: Topraksız tarım",
                    "ethos": 0.5,
                    "pathos": 0.6,
                    "logos": 0.9,
                    "effects": {
                        "money": -2000,
                        "energy": 150,
                        "environment": 0.04
                    }
                },
                {
                    "id": "B",
                    "text": "Kompost Üretimi: Atıklardan toprak",
                    "ethos": 0.6,
                    "pathos": 0.7,
                    "logos": 0.7,
                    "effects": {
                        "money": -1000,
                        "energy": 80,
                        "environment": 0.06
                    }
                },
                {
                    "id": "C",
                    "text": "Sentetik Gübre: Kimyasal zenginleştirme",
                    "ethos": 0.7,
                    "pathos": 0.4,
                    "logos": 0.8,
                    "effects": {
                        "money": -1500,
                        "energy": 100,
                        "environment": -0.03
                    }
                }
            ]
        },
        {
            "id": "environment_008",
            "phase": "crisis",
            "title": "Radyasyon Artışı",
            "description": "YZ Analiz: Güneş fırtınası sonrası radyasyon %200 arttı. Koruyucu kalkan yetersiz. Uzun vadeli sağlık riski.",
            "options": [
                {
                    "id": "A",
                    "text": "Yer Altına Taşınma: Derin sığınaklara yerleşim",
                    "ethos": 0.7,
                    "pathos": 0.6,
                    "logos": 0.8,
                    "effects": {
                        "money": -3000,
                        "energy": 250,
                        "crime": 0.04,
                        "environment": 0.0
                    }
                },
                {
                    "id": "B",
                    "text": "Kalkan Güçlendirme: Manyetik alan jeneratörü",
                    "ethos": 0.6,
                    "pathos": 0.7,
                    "logos": 0.9,
                    "effects": {
                        "money": -4000,
                        "energy": 300,
                        "environment": 0.02
                    }
                },
                {
                    "id": "C",
                    "text": "Dönüşümlü Maruziyet: Herkes sırayla dışarı",
                    "ethos": 0.8,
                    "pathos": 0.4,
                    "logos": 0.6,
                    "effects": {
                        "money": -800,
                        "energy": 80,
                        "crime": 0.02,
                        "environment": 0.0
                    }
                }
            ]
        },
        {
            "id": "environment_009",
            "phase": "crisis",
            "title": "Elektrik Kesintileri",
            "description": "YZ Analiz: Enerji talebi üretimi aştı. Günde 4 saat kesinti yapılıyor. Ekonomi duruyor.",
            "options": [
                {
                    "id": "A",
                    "text": "Yeni Jeneratör: Acil kapasite artışı",
                    "ethos": 0.6,
                    "pathos": 0.7,
                    "logos": 0.9,
                    "effects": {
                        "money": -3500,
                        "energy": 400,
                        "environment": -0.05
                    }
                },
                {
                    "id": "B",
                    "text": "Tasarruf Kampanyası: Gönüllü tüketim azaltma",
                    "ethos": 0.5,
                    "pathos": 0.8,
                    "logos": 0.7,
                    "effects": {
                        "money": -500,
                        "energy": -50,
                        "crime": 0.02,
                        "environment": 0.04
                    }
                },
                {
                    "id": "C",
                    "text": "Sanayi Kısıtlaması: Fabrikalar durdurulsun",
                    "ethos": 0.7,
                    "pathos": 0.5,
                    "logos": 0.7,
                    "effects": {
                        "money": -1500,
                        "energy": -100,
                        "crime": 0.04,
                        "environment": 0.05
                    }
                }
            ]
        },
        {
            "id": "environment_010",
            "phase": "crisis",
            "title": "Plastik Krizi",
            "description": "YZ Analiz: Plastik atıklar her yerde. Geri dönüşüm yetersiz. Mikro plastikler su sisteminde tespit edildi.",
            "options": [
                {
                    "id": "A",
                    "text": "Plastik Yasağı: Tek kullanımlık yasak",
                    "ethos": 0.7,
                    "pathos": 0.7,
                    "logos": 0.7,
                    "effects": {
                        "money": -1000,
                        "energy": 70,
                        "crime": 0.02,
                        "environment": 0.08
                    }
                },
                {
                    "id": "B",
                    "text": "Bakteriyel Çözüm: Plastik yiyen bakteri üretimi",
                    "ethos": 0.5,
                    "pathos": 0.6,
                    "logos": 0.9,
                    "effects": {
                        "money": -2000,
                        "energy": 120,
                        "environment": 0.10
                    }
                },
                {
                    "id": "C",
                    "text": "Sıkıştır ve Depola: Gelecek nesile bırak",
                    "ethos": 0.8,
                    "pathos": 0.3,
                    "logos": 0.5,
                    "effects": {
                        "money": -600,
                        "energy": 50,
                        "environment": -0.02
                    }
                }
            ]
        },
        {
            "id": "environment_011",
            "phase": "crisis",
            "title": "Biyoçeşitlilik Kaybı",
            "description": "YZ Analiz: Getirdiğimiz bitki ve hayvan türlerinin %40'ı öldü. Ekosistem dengesi bozuluyor.",
            "options": [
                {
                    "id": "A",
                    "text": "Gen Bankası: Tüm DNA'ları sakla, gelecekte klonla",
                    "ethos": 0.6,
                    "pathos": 0.6,
                    "logos": 0.9,
                    "effects": {
                        "money": -1800,
                        "energy": 100,
                        "environment": 0.03
                    }
                },
                {
                    "id": "B",
                    "text": "Yoğun Koruma: Kalan türlere maksimum kaynak",
                    "ethos": 0.5,
                    "pathos": 0.8,
                    "logos": 0.7,
                    "effects": {
                        "money": -2500,
                        "energy": 150,
                        "environment": 0.08
                    }
                },
                {
                    "id": "C",
                    "text": "Doğal Seçilim: Uyum sağlayanlar yaşar",
                    "ethos": 0.7,
                    "pathos": 0.3,
                    "logos": 0.8,
                    "effects": {
                        "money": -500,
                        "energy": 40,
                        "environment": -0.04
                    }
                }
            ]
        },
        {
            "id": "environment_012",
            "phase": "crisis",
            "title": "İklim Kontrol Talebi",
            "description": "YZ Analiz: Kolonistler yapay mevsimler istiyor. Sürekli aynı sıcaklık ruh sağlığını bozuyor diyorlar.",
            "options": [
                {
                    "id": "A",
                    "text": "Dinamik İklim: 4 mevsim simülasyonu",
                    "ethos": 0.5,
                    "pathos": 0.8,
                    "logos": 0.7,
                    "effects": {
                        "money": -2000,
                        "energy": 200,
                        "environment": 0.02
                    }
                },
                {
                    "id": "B",
                    "text": "Bölgesel Çeşitlilik: Her sektör farklı iklim",
                    "ethos": 0.6,
                    "pathos": 0.7,
                    "logos": 0.8,
                    "effects": {
                        "money": -3000,
                        "energy": 250,
                        "environment": 0.04
                    }
                },
                {
                    "id": "C",
                    "text": "Sabit Kal: Enerji israfı, psikolojik uyum gerek",
                    "ethos": 0.8,
                    "pathos": 0.3,
                    "logos": 0.7,
                    "effects": {
                        "money": -200,
                        "energy": 30,
                        "crime": 0.03,
                        "environment": 0.0
                    }
                }
            ]
        }
    ],
    
    "🔬 Teknoloji": [
        # === KURULUM FAZLARI ===
        {
            "id": "technology_001",
            "phase": "setup",
            "title": "Ar-Ge Önceliği",
            "description": "YZ Analiz: Sınırlı kaynakları hangi teknoloji alanına yatırmalıyız?",
            "options": [
                {
                    "id": "A",
                    "text": "Yaşam Desteği: Hava, su, gıda teknolojileri",
                    "ethos": 0.7,
                    "pathos": 0.7,
                    "logos": 0.8,
                    "effects": {
                        "money": -2000,
                        "energy": 120,
                        "environment": 0.04
                    }
                },
                {
                    "id": "B",
                    "text": "Üretim Teknolojisi: 3D baskı, otomasyon",
                    "ethos": 0.6,
                    "pathos": 0.5,
                    "logos": 0.9,
                    "effects": {
                        "money": -1800,
                        "energy": 150,
                        "environment": 0.02
                    }
                },
                {
                    "id": "C",
                    "text": "İletişim: Dünya'yla bağlantı iyileştirme",
                    "ethos": 0.5,
                    "pathos": 0.8,
                    "logos": 0.7,
                    "effects": {
                        "money": -1500,
                        "energy": 100,
                        "environment": 0.0
                    }
                }
            ]
        },
        {
            "id": "technology_002",
            "phase": "setup",
            "title": "YZ Kullanım Seviyesi",
            "description": "YZ Analiz: Yapay zeka kolonide ne kadar yetkili olmalı? Karar alma süreçlerinde rolü?",
            "options": [
                {
                    "id": "A",
                    "text": "Tam Otomasyon: YZ her şeyi yönetir",
                    "ethos": 0.4,
                    "pathos": 0.3,
                    "logos": 0.9,
                    "effects": {
                        "money": -3000,
                        "energy": 200,
                        "crime": -0.05
                    }
                },
                {
                    "id": "B",
                    "text": "Yardımcı Sistem: Sadece öneride bulunur",
                    "ethos": 0.6,
                    "pathos": 0.6,
                    "logos": 0.8,
                    "effects": {
                        "money": -1500,
                        "energy": 100,
                        "crime": 0.0
                    }
                },
                {
                    "id": "C",
                    "text": "Minimal Kullanım: İnsanlar karar verir",
                    "ethos": 0.8,
                    "pathos": 0.7,
                    "logos": 0.5,
                    "effects": {
                        "money": -500,
                        "energy": 50,
                        "crime": 0.02
                    }
                }
            ]
        },
        {
            "id": "technology_003",
            "phase": "setup",
            "title": "İnternet ve Bağlantı",
            "description": "YZ Analiz: Koloni içi ağ altyapısı kurulacak. Ne kadar açık, ne kadar kontrollü?",
            "options": [
                {
                    "id": "A",
                    "text": "Açık İnternet: Sansürsüz erişim",
                    "ethos": 0.3,
                    "pathos": 0.7,
                    "logos": 0.8,
                    "effects": {
                        "money": -1000,
                        "energy": 80,
                        "crime": 0.02
                    }
                },
                {
                    "id": "B",
                    "text": "Filtrel İnternet: Zararlı içerik engellenir",
                    "ethos": 0.7,
                    "pathos": 0.5,
                    "logos": 0.7,
                    "effects": {
                        "money": -1200,
                        "energy": 90,
                        "crime": -0.02
                    }
                },
                {
                    "id": "C",
                    "text": "Kapalı Ağ: Sadece lokal intranet",
                    "ethos": 0.8,
                    "pathos": 0.4,
                    "logos": 0.6,
                    "effects": {
                        "money": -600,
                        "energy": 50,
                        "crime": -0.03
                    }
                }
            ]
        },
        {
            "id": "technology_004",
            "phase": "crisis",
            "title": "YZ Kritik Hata",
            "description": "ACIL - YZ karar modülünde beklenmedik bir hata tespit edildi. Birçok sistem yanlış öneri üretiyor. Hemen müdahale gerekli.",
            "options": [
                {
                    "id": "A",
                    "text": "Sistemi Kapat: YZ tüm otonom erişimi kaybetsin",
                    "ethos": 0.7,
                    "pathos": 0.4,
                    "logos": 0.6,
                    "effects": {
                        "money": -500,
                        "energy": 50,
                        "crime": 0.01
                    }
                },
                {
                    "id": "B",
                    "text": "Hızlı Yama: Yazılım ekipleri müdahale etsin",
                    "ethos": 0.5,
                    "pathos": 0.6,
                    "logos": 0.8,
                    "effects": {
                        "money": -1200,
                        "energy": 80,
                        "crime": 0.0
                    }
                },
                {
                    "id": "C",
                    "text": "İzleme Modu: Sadece öneri verilsin, uygulama insan kararıyla olsun",
                    "ethos": 0.6,
                    "pathos": 0.5,
                    "logos": 0.7,
                    "effects": {
                        "money": -300,
                        "energy": 40,
                        "crime": 0.0
                    }
                }
            ]
        },
        {
            "id": "technology_005",
            "phase": "crisis",
            "title": "Güvenlik Açığı İhlali",
            "description": "YZ Analiz: Kritik bir sunucuya dışarıdan erişim sağlanmış. Veriler sızmış olabilir. Sızıntı kontrolü gerekli.",
            "options": [
                {
                    "id": "A",
                    "text": "Acil İzolasyon: Etkilenen düğümleri ağdan çıkar",
                    "ethos": 0.8,
                    "pathos": 0.3,
                    "logos": 0.7,
                    "effects": {
                        "money": -700,
                        "energy": 60,
                        "crime": -0.02
                    }
                },
                {
                    "id": "B",
                    "text": "Açık İlan: Halkı bilgilendir, şeffaflığı koru",
                    "ethos": 0.4,
                    "pathos": 0.7,
                    "logos": 0.6,
                    "effects": {
                        "money": -400,
                        "energy": 30,
                        "crime": 0.01
                    }
                },
                {
                    "id": "C",
                    "text": "Gizli Müdahale: Sorunu kapat, sorumluları tespit et",
                    "ethos": 0.6,
                    "pathos": 0.4,
                    "logos": 0.8,
                    "effects": {
                        "money": -900,
                        "energy": 80,
                        "crime": -0.01
                    }
                }
            ]
        },
        {
            "id": "technology_006",
            "phase": "crisis",
            "title": "Patent ve Açık Kaynak Tartışması",
            "description": "YZ Analiz: Bir teknoloji şirketi yaşam destek patentini kapatıyor. Açık kaynak mı, telif mi tartışması alevlendi.",
            "options": [
                {
                    "id": "A",
                    "text": "Patentleri Koru: Yenilik teşviki için haklar saklı kalsın",
                    "ethos": 0.7,
                    "pathos": 0.3,
                    "logos": 0.7,
                    "effects": {
                        "money": 800,
                        "energy": 40,
                        "crime": 0.01
                    }
                },
                {
                    "id": "B",
                    "text": "Açık Kaynak Zorunlu: Temel altyapılar paylaşılmalı",
                    "ethos": 0.4,
                    "pathos": 0.8,
                    "logos": 0.8,
                    "effects": {
                        "money": -500,
                        "energy": 60,
                        "crime": 0.0
                    }
                },
                {
                    "id": "C",
                    "text": "Hibrit Lisans: Kritik modüller açık, geri lisanslı olsun",
                    "ethos": 0.6,
                    "pathos": 0.5,
                    "logos": 0.7,
                    "effects": {
                        "money": -200,
                        "energy": 30,
                        "crime": 0.0
                    }
                }
            ]
        },
        {
            "id": "technology_007",
            "phase": "crisis",
            "title": "Otonom Sistemler Etiği",
            "description": "YZ Analiz: Otonom robotların yetkileri genişletiliyor. Etik sınırlar belirlenmeli. Toplum ikiye bölünmüş.",
            "options": [
                {
                    "id": "A",
                    "text": "Sıkı Kurallar: Otonomi sınırlandırılsın",
                    "ethos": 0.8,
                    "pathos": 0.3,
                    "logos": 0.6,
                    "effects": {
                        "money": -400,
                        "energy": 30,
                        "crime": 0.01
                    }
                },
                {
                    "id": "B",
                    "text": "Deneysel Genişletme: Kontrollü pilotlarla ilerle",
                    "ethos": 0.5,
                    "pathos": 0.6,
                    "logos": 0.8,
                    "effects": {
                        "money": -1000,
                        "energy": 80,
                        "crime": 0.0
                    }
                },
                {
                    "id": "C",
                    "text": "Tam Özerklik: Verim için risk al",
                    "ethos": 0.3,
                    "pathos": 0.4,
                    "logos": 0.9,
                    "effects": {
                        "money": 500,
                        "energy": 120,
                        "crime": 0.02
                    }
                }
            ]
        },
        {
            "id": "technology_008",
            "phase": "crisis",
            "title": "Veri Merkezi Yetersizliği",
            "description": "YZ Analiz: Veri merkezi kapasitesi doldu, gecikmeler kritik hizmetleri etkiliyor. Yükseltme veya taşıma gerekli.",
            "options": [
                {
                    "id": "A",
                    "text": "Yeni Veri Merkezi Kur: Büyük yatırım yap",
                    "ethos": 0.6,
                    "pathos": 0.4,
                    "logos": 0.9,
                    "effects": {
                        "money": -3000,
                        "energy": 200,
                        "crime": 0.0
                    }
                },
                {
                    "id": "B",
                    "text": "Bulut Çözümleri: Uzaktan yedeklemeye taşı",
                    "ethos": 0.5,
                    "pathos": 0.5,
                    "logos": 0.8,
                    "effects": {
                        "money": -1200,
                        "energy": 80,
                        "crime": 0.0
                    }
                },
                {
                    "id": "C",
                    "text": "Kaynak Optimizasyonu: Mevcut sistemleri iyileştir",
                    "ethos": 0.7,
                    "pathos": 0.3,
                    "logos": 0.7,
                    "effects": {
                        "money": -600,
                        "energy": 40,
                        "crime": 0.0
                    }
                }
            ]
        },
        {
            "id": "technology_009",
            "phase": "crisis",
            "title": "Yedekleme ve Felaket Kurtarma",
            "description": "YZ Analiz: Kritik yedekleme protokolleri eksik. Büyük bir arıza durumunda veri kaybı riski yüksek.",
            "options": [
                {
                    "id": "A",
                    "text": "Tam Yedekleme: Her şeyi coğrafi olarak yedekle",
                    "ethos": 0.6,
                    "pathos": 0.4,
                    "logos": 0.8,
                    "effects": {
                        "money": -2000,
                        "energy": 120,
                        "crime": 0.0
                    }
                },
                {
                    "id": "B",
                    "text": "Öncelikli Yedek: Kritik verileri koru, geri kalanı isteğe bağlı",
                    "ethos": 0.7,
                    "pathos": 0.5,
                    "logos": 0.7,
                    "effects": {
                        "money": -800,
                        "energy": 60,
                        "crime": 0.0
                    }
                },
                {
                    "id": "C",
                    "text": "Minimum Yedek: Maliyet düşük, risk yüksek",
                    "ethos": 0.4,
                    "pathos": 0.3,
                    "logos": 0.5,
                    "effects": {
                        "money": -200,
                        "energy": 20,
                        "crime": 0.01
                    }
                }
            ]
        },
        {
            "id": "technology_010",
            "phase": "crisis",
            "title": "Yüksek Riskli Proje Onayı",
            "description": "YZ Analiz: Yeni bir ileri teknoloji projesi büyük kazanç vaat ediyor fakat yüksek başarısızlık riski var. Onay mı, iptal mi?",
            "options": [
                {
                    "id": "A",
                    "text": "Onayla: Risk kabul, potansiyel büyük fayda",
                    "ethos": 0.5,
                    "pathos": 0.6,
                    "logos": 0.8,
                    "effects": {
                        "money": -4000,
                        "energy": 300,
                        "crime": 0.0
                    }
                },
                {
                    "id": "B",
                    "text": "Kısmi Fon: Pilot ile sınırla",
                    "ethos": 0.6,
                    "pathos": 0.4,
                    "logos": 0.7,
                    "effects": {
                        "money": -1200,
                        "energy": 100,
                        "crime": 0.0
                    }
                },
                {
                    "id": "C",
                    "text": "Reddet: Stabilite öncelik",
                    "ethos": 0.8,
                    "pathos": 0.2,
                    "logos": 0.6,
                    "effects": {
                        "money": 0,
                        "energy": 20,
                        "crime": 0.02
                    }
                }
            ]
        },
        {
            "id": "technology_011",
            "phase": "crisis",
            "title": "İnsan-Makine Arayüzü Tartışması",
            "description": "YZ Analiz: Beyin-bilgisayar arayüzleri (BBI) denenmek isteniyor. Mahremiyet ve kimlik tartışması başladı.",
            "options": [
                {
                    "id": "A",
                    "text": "Sıkı Düzenleme: Klinik ve izinli kullanım",
                    "ethos": 0.7,
                    "pathos": 0.4,
                    "logos": 0.8,
                    "effects": {
                        "money": -1500,
                        "energy": 80,
                        "crime": 0.01
                    }
                },
                {
                    "id": "B",
                    "text": "Araştırma İzni: Sınırlı ve denetlenmiş pilotlar",
                    "ethos": 0.5,
                    "pathos": 0.6,
                    "logos": 0.9,
                    "effects": {
                        "money": -1000,
                        "energy": 100,
                        "crime": 0.0
                    }
                },
                {
                    "id": "C",
                    "text": "Serbest Bırak: Bireysel tercih ön planda",
                    "ethos": 0.3,
                    "pathos": 0.7,
                    "logos": 0.6,
                    "effects": {
                        "money": -500,
                        "energy": 50,
                        "crime": 0.02
                    }
                }
            ]
        },
        {
            "id": "technology_012",
            "phase": "crisis",
            "title": "YZ Etiği Komisyonu Talebi",
            "description": "YZ Analiz: Toplum, yapay zekanın etik sınırlarını belirleyecek bağımsız bir komisyon istiyor. Hemen karar gerekmiyor ama önem arz ediyor.",
            "options": [
                {
                    "id": "A",
                    "text": "Bağımsız Komisyon Kur: Uzmanlar ve sivil temsilcilerden oluşsun",
                    "ethos": 0.6,
                    "pathos": 0.7,
                    "logos": 0.9,
                    "effects": {
                        "money": -1200,
                        "energy": 80,
                        "crime": 0.0
                    }
                },
                {
                    "id": "B",
                    "text": "Hükümet Denetimi: Mevcut kurum etik kuralları belirlesin",
                    "ethos": 0.7,
                    "pathos": 0.3,
                    "logos": 0.6,
                    "effects": {
                        "money": -600,
                        "energy": 40,
                        "crime": 0.01
                    }
                },
                {
                    "id": "C",
                    "text": "Bekle ve İncele: Acil değil, panel raporu beklenir",
                    "ethos": 0.5,
                    "pathos": 0.5,
                    "logos": 0.7,
                    "effects": {
                        "money": -200,
                        "energy": 20,
                        "crime": 0.0
                    }
                }
            ]
        }
    ]
}
