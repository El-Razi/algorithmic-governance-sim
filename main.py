import sys
import os
from pathlib import Path

# Proje kök dizinini Python path'e ekle
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

from src.core.colony import Colony
from src.core.decision_manager import DecisionManager
from src.simulation.game_loop import GameLoop
from src.utils.display import Display
from config import (
    GameConfig, 
    ModuleConfig, 
    DifficultyConfig,
    VersionInfo,
    DisplayConfig
)


def show_splash_screen():
    """Açılış ekranını göster"""
    print("\n" + "=" * 70)
    print(" " * 15 + "🚀 ALGOGOV: UZAY KOLONİSİ SİMÜLATÖRÜ 🚀")
    print(" " * 15 + f"   v{VersionInfo.VERSION} - {VersionInfo.VERSION_NAME}")
    print("=" * 70)
    print()
    print("  📖 HİKAYE:")
    print("  Dünya'dan 50 milyon km uzakta, 1000 kişilik bir koloni kuruldu.")
    print("  Kaynaklar sınırlı, tehlikeler her köşede. Siz yöneticisiniz.")
    print("  Amacınız: Koloninizi hayatta tutmak ve geliştirmek.")
    print()
    print("  🎮 OYUN MODU: Hikaye Modu")
    print(f"     • {GameConfig.TOTAL_TURNS} tur")
    print(f"     • İlk {GameConfig.SETUP_PHASE_TURNS} tur: ⚙️  Sistem kurulumu")
    print(f"     • Son {GameConfig.CRISIS_PHASE_TURNS} tur: 🚨 Kriz yönetimi")
    print(f"     • {GameConfig.TOTAL_MODULES} farklı modülde karar verme")
    print()
    print("  📊 METRİKLER:")
    print("     • 😊 Mutluluk: Nüfusun genel ruh hali")
    print("     • 💰 Para: Koloni bütçesi")
    print("     • 🌱 Çevre: Sürdürülebilirlik seviyesi")
    print("     • 🚨 Suç: Güvenlik durumu")
    print("     • 📈 Gelişme: Genel ilerleme")
    print()
    print("=" * 70)


def show_difficulty_menu() -> str:
    """Zorluk seçimi menüsü"""
    print("\n🎚️  ZORLUK SEÇİMİ")
    print("=" * 70)
    
    for i, (name, config) in enumerate(DifficultyConfig.DIFFICULTIES.items(), 1):
        marker = "→" if name == DifficultyConfig.DEFAULT_DIFFICULTY else " "
        print(f"{marker} {i}. {name.upper()}: {config['description']}")
        print(f"      Çarpan: {config['effect_multiplier']}x")
        print(f"      Bonus Para: {config['starting_money_bonus']:+.0f}")
        print()
    
    print("=" * 70)
    
    while True:
        choice = input(f"Seçiminiz (1-{len(DifficultyConfig.DIFFICULTIES)}) veya Enter (normal): ").strip()
        
        if not choice:
            return DifficultyConfig.DEFAULT_DIFFICULTY
        
        try:
            choice_idx = int(choice) - 1
            difficulties = list(DifficultyConfig.DIFFICULTIES.keys())
            
            if 0 <= choice_idx < len(difficulties):
                selected = difficulties[choice_idx]
                print(f"\n✅ Seçildi: {selected.upper()}")
                return selected
            else:
                print(f"❌ Lütfen 1-{len(DifficultyConfig.DIFFICULTIES)} arası seçin.")
        except ValueError:
            print("❌ Geçersiz giriş.")


def initialize_colony(difficulty: str = "normal") -> Colony:
    """Koloniyi başlat"""
    print("\n🏗️  Koloni başlatılıyor...")
    
    # Zorluk ayarlarını al
    diff_config = DifficultyConfig.DIFFICULTIES[difficulty]
    
    # Koloniyi oluştur
    colony = Colony(
        population_size=GameConfig.POPULATION_SIZE,
        name="Alpha Colony"
    )
    
    # Zorluk bonuslarını uygula
    colony.metrics.money += diff_config['starting_money_bonus']
    colony.metrics.happiness += diff_config['starting_happiness_bonus']
    
    # Sınırları kontrol et
    colony.metrics.happiness = max(0, min(1, colony.metrics.happiness))
    
    print(f"✅ {colony.name} hazır!")
    print(f"   👥 Nüfus: {len(colony.population)}")
    print(f"   💰 Başlangıç Bütçesi: ${colony.metrics.money:.0f}")
    print(f"   😊 Başlangıç Mutluluğu: {colony.metrics.happiness*100:.0f}%")
    
    return colony


def initialize_decision_manager() -> DecisionManager:
    """Karar yöneticisini başlat"""
    print("\n📋 Karar veritabanı yükleniyor...")
    
    decision_manager = DecisionManager()
    
    # Validasyon
    if GameConfig.TOTAL_DECISIONS != len(decision_manager.get_all_decisions()):
        print(f"⚠️  Uyarı: Beklenen {GameConfig.TOTAL_DECISIONS} karar, "
              f"bulunan {len(decision_manager.get_all_decisions())} karar")
    
    # İstatistikler
    setup_decisions = len(decision_manager.get_phase_decisions("setup"))
    crisis_decisions = len(decision_manager.get_phase_decisions("crisis"))
    
    print(f"✅ Karar veritabanı yüklendi!")
    print(f"   📊 Toplam Karar: {len(decision_manager.get_all_decisions())}")
    print(f"   ⚙️  Kurulum Kararları: {setup_decisions}")
    print(f"   🚨 Kriz Kararları: {crisis_decisions}")
    
    return decision_manager


def show_main_menu():
    """Ana menü"""
    print("\n" + "=" * 70)
    print("  ANA MENÜ")
    print("=" * 70)
    print()
    print("  1. 🎮 Yeni Oyun Başlat")
    print("  2. 📖 Nasıl Oynanır?")
    print("  3. ℹ️  Hakkında")
    print("  4. 🚪 Çıkış")
    print()
    print("=" * 70)


def show_how_to_play():
    """Nasıl oynanır rehberi"""
    print("\n" + "=" * 70)
    print("  📖 NASIL OYNANIR?")
    print("=" * 70)
    print()
    print("  🎯 AMAÇ:")
    print("     7 tur boyunca koloninizi hayatta tutun ve geliştirin.")
    print()
    print("  🎮 OYNANIM:")
    print("     • Her turda 9 farklı modülden birer karar alacaksınız")
    print("     • Her kararın 2-4 seçeneği vardır")
    print("     • Seçeneklerin etkileri anında gösterilir")
    print("     • Kararlarınız koloninin metriklerini etkiler")
    print()
    print("  💡 ETİKETLER:")
    print("     • Ethos (Ahlak): Geleneksel değerler, otorite")
    print("     • Pathos (Duygu): Empati, sosyal adalet")
    print("     • Logos (Mantık): Rasyonellik, verimlilik")
    print()
    print("  📊 METRİKLER:")
    print("     • 😊 Mutluluk (0-100%): Düşük olursa isyan!")
    print("     • 💰 Para: Negatife düşmesin!")
    print("     • 🌱 Çevre (0-100%): Sürdürülebilirlik")
    print("     • 🚨 Suç (0-100%): Düşük tutun")
    print("     • 📈 Gelişme: Ne kadar ilerleme kaydettiniz")
    print()
    print("  🏆 BAŞARI:")
    print("     Oyun sonunda 0-100 arası puan alırsınız.")
    print("     Not: F'den A+'ya kadar")
    print()
    print("  💡 İPUÇLARI:")
    print("     • İlk 3 turda sistemi kurun, temel alın")
    print("     • Son 4 turda krizleri yönetin")
    print("     • Dengeli seçimler yapın")
    print("     • Bir metriğe takılmayın, tümüne dikkat edin")
    print("     • 'i' tuşu ile oyun içinde koloni durumunu görebilirsiniz")
    print()
    print("=" * 70)
    input("\nDevam etmek için Enter'a basın...")


def show_about():
    """Hakkında bilgisi"""
    print("\n" + "=" * 70)
    print("  ℹ️  HAKKINDA")
    print("=" * 70)
    print()
    print(f"  📦 AlgoGov Simulator v{VersionInfo.VERSION}")
    print(f"  📅 Sürüm: {VersionInfo.VERSION_NAME}")
    print(f"  🗓️  Tarih: {VersionInfo.RELEASE_DATE}")
    print()
    print("  📝 AÇIKLAMA:")
    print("     Algoritmik yönetişim ve dijital demokrasi üzerine")
    print("     açık kaynak, interaktif simülasyon platformu.")
    print()
    print("  🎯 HEDEF:")
    print("     Farklı karar alma mekanizmalarını test etmek ve")
    print("     dijital demokrasi araştırmalarına katkı sağlamak.")
    print()
    print("  🌟 ÖZELLİKLER:")
    for feature, enabled in VersionInfo.FEATURES.items():
        status = "✅" if enabled else "🔜"
        print(f"     {status} {feature}")
    print()
    print("  👥 PROJE:")
    print("     GitHub: github.com/[username]/algogov-simulator")
    print("     Lisans: MIT License")
    print("     Katkıda Bulunun: CONTRIBUTING.md")
    print()
    print("  🙏 TEŞEKKÜRLER:")
    print("     Bu proje açık kaynak topluluğunun katkılarıyla gelişiyor.")
    print()
    print("=" * 70)
    input("\nDevam etmek için Enter'a basın...")


def play_game(difficulty: str = "normal"):
    """Ana oyun döngüsü"""
    try:
        # Koloniyi başlat
        colony = initialize_colony(difficulty)
        
        # Karar yöneticisini başlat
        decision_manager = initialize_decision_manager()
        
        # Oyun döngüsünü başlat
        game = GameLoop(colony, decision_manager)
        
        # İlk durumu göster
        print()
        Display.show_colony_status(colony)
        print()
        
        # Başlama onayı
        print("=" * 70)
        print("  Simülasyona başlamak için Enter'a basın...")
        print("  (Oyun sırasında 'i' ile koloni durumunu görebilirsiniz)")
        print("=" * 70)
        input()
        
        # 7 tur oyun döngüsü
        for turn in range(1, GameConfig.TOTAL_TURNS + 1):
            print("\n\n" + "=" * 70)
            
            # Faz göstergesi
            if turn <= GameConfig.SETUP_PHASE_TURNS:
                phase_icon = DisplayConfig.PHASE_SYMBOLS["setup"]
                phase_name = "KURULUM FAZI"
            else:
                phase_icon = DisplayConfig.PHASE_SYMBOLS["crisis"]
                phase_name = "KRİZ YÖNETİMİ"
            
            print(f"  {phase_icon} TUR {turn}/{GameConfig.TOTAL_TURNS} - {phase_name}")
            print("=" * 70)
            
            # Bu turu oynat
            game.play_turn()
            
            # Tur sonu özeti
            Display.show_turn_summary(colony, turn)
            
            # Kritik durum kontrolü
            critical = any(colony.get_status_summary().values())
            if critical:
                print("\n⚠️  UYARI: Bazı metrikler kritik seviyelerde!")
            
            # Devam etmek için bekle (son turda hariç)
            if turn < GameConfig.TOTAL_TURNS:
                print("\n" + "─" * 70)
                print("⏭️  Sonraki tura geçmek için Enter'a basın...")
                print("   (veya 'q' ile oyundan çık)")
                print("─" * 70)
                
                choice = input().strip().lower()
                if choice == 'q':
                    print("\n⚠️  Oyundan çıkılıyor...")
                    confirm = input("Emin misiniz? (e/h): ")
                    if confirm.lower() == 'e':
                        print("👋 Görüşmek üzere!")
                        return
        
        # Oyun sonu raporu
        print("\n\n" + "=" * 70)
        print("  🏁 OYUN BİTTİ - FİNAL RAPORU")
        print("=" * 70)
        Display.show_final_report(colony)
        
        # İstatistikleri göster
        stats = game.get_game_statistics()
        print("\n📊 OYUN İSTATİSTİKLERİ")
        print("─" * 70)
        print(f"  Toplam Karar: {stats['total_decisions_made']}")
        print(f"  Ortalama Destek: {stats['average_support']*100:.1f}%")
        print(f"  Kurulum Kararları: {stats['phase_breakdown']['setup']}")
        print(f"  Kriz Kararları: {stats['phase_breakdown']['crisis']}")
        
        # Tekrar oynama teklifi
        print("\n" + "=" * 70)
        print("  Tekrar oynamak ister misiniz?")
        print("=" * 70)
        choice = input("(e/h): ").strip().lower()
        if choice == 'e':
            main()
        else:
            print("\n👋 Oynadığınız için teşekkürler!")
        
    except KeyboardInterrupt:
        print("\n\n⚠️  Oyun kullanıcı tarafından durduruldu")
        print("📊 Mevcut durum:")
        Display.show_colony_status(colony)
        print("\n👋 Görüşmek üzere!")
    except Exception as e:
        print(f"\n❌ Beklenmeyen hata: {e}")
        import traceback
        traceback.print_exc()


def main():
    """Ana fonksiyon"""
    # Splash screen
    show_splash_screen()
    
    while True:
        show_main_menu()
        
        choice = input("Seçiminiz (1-4): ").strip()
        
        if choice == "1":
            # Yeni oyun
            difficulty = show_difficulty_menu()
            play_game(difficulty)
            break
        
        elif choice == "2":
            # Nasıl oynanır
            show_how_to_play()
        
        elif choice == "3":
            # Hakkında
            show_about()
        
        elif choice == "4":
            # Çıkış
            print("\n" + "=" * 70)
            print("  👋 AlgoGov'dan ayrılıyorsunuz...")
            print("=" * 70)
            print()
            print("  🙏 Oynadığınız için teşekkürler!")
            print("  ⭐ Beğendiyseniz GitHub'da yıldızlayın!")
            print("  🤝 Katkıda bulunmak için CONTRIBUTING.md'ye bakın")
            print()
            print("  Görüşmek üzere! 🚀")
            print()
            print("=" * 70)
            sys.exit(0)
        
        else:
            print("\n❌ Geçersiz seçim! Lütfen 1-4 arası bir sayı girin.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️  Program kapatılıyor...")
        print("👋 Görüşmek üzere!")
        sys.exit(0)
