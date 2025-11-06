from src.core.colony import Colony
from src.core.decision_manager import DecisionManager
from src.simulation.game_loop import GameLoop
from src.utils.display import Display
import time

def main():
    print("=" * 60)
    print("  ALGOGOV: Algorithmic Governance Simulator v0.1")
    print("=" * 60)
    print()
    
    # Koloniyi başlat
    print("🏗️  Koloni başlatılıyor...")
    colony = Colony(population_size=1000, name="Alpha Colony")
    print(f"✅ {colony.name} hazır! Nüfus: {len(colony.population)}")
    print()
    
    # Karar yöneticisini başlat
    decision_manager = DecisionManager()
    print(f"📋 Karar veritabanı yüklendi: {len(decision_manager.get_all_decisions())} karar")
    print()
    
    # Oyun döngüsünü başlat
    game = GameLoop(colony, decision_manager)
    
    # İlk durumu göster
    Display.show_colony_status(colony)
    print()
    
    # Kullanıcıya başlama seçeneği sun
    print("Simülasyona başlamak için Enter'a basın (veya 'q' ile çıkış)...")
    choice = input().strip().lower()
    if choice == 'q':
        print("👋 Görüşmek üzere!")
        return
    
    # 7 tur boyunca oyun döngüsü
    target_turns = 7
    
    try:
        for turn in range(1, target_turns + 1):
            print("\n" + "=" * 60)
            print(f"  TUR {turn}/{target_turns}")
            print("=" * 60)
            
            # Bu turu oynat
            game.play_turn()
            
            # Tur sonu özeti
            Display.show_turn_summary(colony, turn)
            
            # Devam etmek için bekle (son turda hariç)
            if turn < target_turns:
                print("\nDevam etmek için Enter'a basın...")
                input()
        
        # Oyun sonu raporu
        print("\n" + "=" * 60)
        print("  OYUN BİTTİ - FİNAL RAPORU")
        print("=" * 60)
        Display.show_final_report(colony)
        
    except KeyboardInterrupt:
        print("\n\n⚠️  Simülasyon kullanıcı tarafından durduruldu")
        Display.show_colony_status(colony)

if __name__ == "__main__":
    main()
