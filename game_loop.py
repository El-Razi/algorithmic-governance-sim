from typing import Dict
from ..core.colony import Colony
from ..core.decision_manager import DecisionManager
from ..utils.display import Display

class GameLoop:
    """Oyun döngüsünü yöneten sınıf"""
    
    def __init__(self, colony: Colony, decision_manager: DecisionManager):
        self.colony = colony
        self.decision_manager = decision_manager
        self.turn_history = []
    
    def play_turn(self):
        """Bir tur oynat"""
        print(f"\n📅 Tur {self.colony.turn + 1} Başlıyor...\n")
        
        # Her modül için karar al
        module_names = list(self.colony.modules.keys())
        turn_decisions = self.decision_manager.get_decisions_for_turn(module_names)
        
        turn_results = []
        
        # Her modül için karar ver
        for module_name in module_names:
            if module_name not in turn_decisions:
                continue
            
            decision = turn_decisions[module_name]
            
            # Kararı göster ve kullanıcıdan seçim al
            chosen_option = self._present_decision_and_get_choice(module_name, decision)
            
            if chosen_option is None:
                continue
            
            # Seçeneğin destek oranını hesapla
            support_rate = self.colony.calculate_decision_support(chosen_option)
            
            # Kararı uygula
            self.colony.apply_decision_effects(chosen_option)
            
            # Modül performansını güncelle
            impact = (support_rate - 0.5) * 2  # -1 ile 1 arası
            self.colony.modules[module_name].update_performance(impact)
            
            # Sonucu kaydet
            turn_results.append({
                'module': module_name,
                'decision': decision['title'],
                'chosen': chosen_option['text'],
                'support_rate': support_rate
            })
        
        # Turu kaydet
        self.turn_history.append({
            'turn': self.colony.turn + 1,
            'results': turn_results,
            'metrics': self.colony.get_status_summary()
        })
        
        # Koloniyi bir sonraki tura geçir
        self.colony.advance_turn()
    
    def _present_decision_and_get_choice(self, module_name: str, decision: Dict) -> Dict:
        """
        Kararı göster ve kullanıcıdan seçim al
        
        Returns:
            Seçilen option dict'i
        """
        print("─" * 60)
        print(f"🏛️  MODÜL: {module_name}")
        print(f"📋 KARAR: {decision['title']}")
        print(f"❓ {decision['description']}")
        print()
        
        options = decision['options']
        
        # Seçenekleri göster
        for i, option in enumerate(options, 1):
            print(f"{i}. {option['text']}")
            
            # Ethos/Pathos/Logos göster
            print(f"   💭 Ethos: {option['ethos']:.1f} | "
                  f"Pathos: {option['pathos']:.1f} | "
                  f"Logos: {option['logos']:.1f}")
            
            # Etkileri göster
            if 'effects' in option:
                effects_str = []
                for key, value in option['effects'].items():
                    if value > 0:
                        effects_str.append(f"{key} +{value}")
                    else:
                        effects_str.append(f"{key} {value}")
                print(f"   📊 Etkiler: {', '.join(effects_str)}")
            
            # Destek oranını hesapla ve göster
            support = self.colony.calculate_decision_support(option)
            print(f"   👥 Tahmini Destek: {support*100:.1f}%")
            print()
        
        # Kullanıcı seçimi
        while True:
            try:
                choice = input(f"Seçiminiz (1-{len(options)}): ").strip()
                choice_idx = int(choice) - 1
                
                if 0 <= choice_idx < len(options):
                    chosen = options[choice_idx]
                    print(f"✅ Seçtiniz: {chosen['text']}\n")
                    return chosen
                else:
                    print(f"❌ Lütfen 1-{len(options)} arası bir sayı girin.")
            except ValueError:
                print("❌ Geçersiz giriş. Lütfen bir sayı girin.")
            except KeyboardInterrupt:
                print("\n⚠️  Oyun durduruldu.")
                return None
    
    def get_turn_summary(self, turn_number: int) -> Dict:
        """Belirli bir turun özetini döndür"""
        if 0 <= turn_number - 1 < len(self.turn_history):
            return self.turn_history[turn_number - 1]
        return None
