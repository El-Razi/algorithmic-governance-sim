"""Oyun döngüsü yönetimi - v2.0"""
from typing import Dict, List
from ..core.colony import Colony
from ..core.decision_manager import DecisionManager
from ..utils.display import Display

class GameLoop:
    """Oyun döngüsünü yöneten sınıf - v2.0"""
    
    def __init__(self, colony: Colony, decision_manager: DecisionManager):
        self.colony = colony
        self.decision_manager = decision_manager
        self.turn_history = []
        self.current_turn = 0
        self.total_turns = 7
        self.setup_phase_turns = 3  # İlk 3 tur kurulum
    
    def play_turn(self):
        """Bir tur oynat"""
        self.current_turn += 1
        
        # Faz bilgisi
        phase = self._get_current_phase()
        phase_name = "KURULUM FAZI" if phase == "setup" else "KRİZ YÖNETİMİ"
        phase_icon = "⚙️" if phase == "setup" else "🚨"
        
        print(f"\n📅 Tur {self.current_turn}/{self.total_turns}")
        print(f"{phase_icon} {phase_name}")
        
        # Faz açıklaması (sadece ilk turda ve faz geçişinde)
        if self.current_turn == 1:
            print()
            print("💡 İLK 3 TUR:")
            print("   Koloninizin temel sistemlerini kuracaksınız.")
            print("   Altyapı, politikalar ve organizasyon kararları.")
        elif self.current_turn == 4:
            print()
            print("⚠️  SON 4 TUR:")
            print("   Artık acil durumlar ve taleplerle karşılaşacaksınız.")
            print("   Hızlı düşünün, kararlarınız kritik!")
        
        print()
        
        # Her modül için karar al
        module_names = list(self.colony.modules.keys())
        turn_decisions = self.decision_manager.get_decisions_for_turn(
            module_names, 
            turn_number=self.current_turn
        )
        
        if not turn_decisions:
            print("❌ Bu tur için karar alınamadı!")
            return
        
        turn_results = []
        
        # Her modül için karar ver
        for i, (module_name, decision) in enumerate(turn_decisions.items(), 1):
            print(f"\n{'='*60}")
            print(f"  KARAR {i}/{len(turn_decisions)}")
            print(f"{'='*60}")
            
            # Kararı göster ve kullanıcıdan seçim al
            chosen_option = self._present_decision_and_get_choice(module_name, decision)
            
            if chosen_option is None:
                print("⚠️  Karar atlandı.")
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
                'decision_id': decision['id'],
                'chosen': chosen_option['text'],
                'chosen_id': chosen_option['id'],
                'support_rate': support_rate,
                'phase': decision.get('phase', 'unknown')
            })
            
            # İlerleme göster
            remaining = len(turn_decisions) - i
            if remaining > 0:
                print(f"\n⏭️  Kalan karar: {remaining}")
        
        # Turu kaydet
        self.turn_history.append({
            'turn': self.current_turn,
            'phase': phase,
            'results': turn_results,
            'metrics': self.colony.get_status_summary()
        })
        
        # Koloniyi bir sonraki tura geçir
        self.colony.advance_turn()
    
    def _get_current_phase(self) -> str:
        """Mevcut fazı döndür"""
        return "setup" if self.current_turn <= self.setup_phase_turns else "crisis"
    
    def _present_decision_and_get_choice(self, module_name: str, decision: Dict) -> Dict:
        """
        Kararı göster ve kullanıcıdan seçim al
        
        Returns:
            Seçilen option dict'i veya None
        """
        print(f"🏛️  MODÜL: {module_name}")
        print(f"📋 KARAR: {decision['title']}")
        
        # Faz göstergesi
        phase = decision.get('phase', 'unknown')
        if phase == 'setup':
            print(f"⚙️  [Kurulum Kararı]")
        elif phase == 'crisis':
            print(f"🚨 [Kriz/Talep Kararı]")
        
        print()
        print(f"❓ {decision['description']}")
        print()
        
        options = decision['options']
        
        # Seçenekleri göster
        for i, option in enumerate(options, 1):
            print(f"━━━ SEÇENEK {i} ━━━")
            print(f"📝 {option['text']}")
            print()
            
            # Ethos/Pathos/Logos göster
            print(f"   💭 İdeolojik Profil:")
            print(f"      Ethos (Ahlak/Otorite): {option['ethos']:.1f}")
            print(f"      Pathos (Duygu/Empati): {option['pathos']:.1f}")
            print(f"      Logos (Mantık/Akıl): {option['logos']:.1f}")
            print()
            
            # Etkileri göster
            if 'effects' in option:
                print(f"   📊 Beklenen Etkiler:")
                effects_list = []
                for key, value in option['effects'].items():
                    if key == 'money':
                        symbol = '💰'
                    elif key == 'energy':
                        symbol = '⚡'
                    elif key == 'environment':
                        symbol = '🌱'
                    elif key == 'crime':
                        symbol = '🚨'
                    else:
                        symbol = '📈'
                    
                    if value > 0:
                        effects_list.append(f"{symbol} {key}: +{value}")
                    else:
                        effects_list.append(f"{symbol} {key}: {value}")
                
                for effect in effects_list:
                    print(f"      {effect}")
                print()
            
            # Destek oranını hesapla ve göster
            support = self.colony.calculate_decision_support(option)
            support_bar = self._get_support_bar(support)
            print(f"   👥 Nüfus Desteği: {support_bar} {support*100:.1f}%")
            print()
        
        # Kullanıcı seçimi
        print("─" * 60)
        while True:
            try:
                choice = input(f"🎯 Seçiminiz (1-{len(options)}) veya 'i' (bilgi), 's' (atla): ").strip().lower()
                
                # Özel komutlar
                if choice == 'i':
                    self._show_colony_info()
                    continue
                elif choice == 's':
                    confirm = input("⚠️  Bu kararı atlamak istediğinize emin misiniz? (e/h): ")
                    if confirm.lower() == 'e':
                        return None
                    continue
                
                choice_idx = int(choice) - 1
                
                if 0 <= choice_idx < len(options):
                    chosen = options[choice_idx]
                    print()
                    print(f"✅ SEÇİLDİ: Seçenek {choice_idx + 1}")
                    print(f"   {chosen['text'][:60]}...")
                    print()
                    return chosen
                else:
                    print(f"❌ Lütfen 1-{len(options)} arası bir sayı girin.")
            except ValueError:
                print("❌ Geçersiz giriş. Lütfen bir sayı veya 'i'/'s' girin.")
            except KeyboardInterrupt:
                print("\n⚠️  Oyundan çıkmak için ana menüye dönün.")
                confirm = input("Bu kararı atlamak ister misiniz? (e/h): ")
                if confirm.lower() == 'e':
                    return None
    
    def _get_support_bar(self, support: float) -> str:
        """Destek oranı için görsel çubuk"""
        bar_length = 20
        filled = int(support * bar_length)
        empty = bar_length - filled
        
        if support >= 0.7:
            color = "🟩"
        elif support >= 0.4:
            color = "🟨"
        else:
            color = "🟥"
        
        return f"[{'█' * filled}{'·' * empty}] {color}"
    
    def _show_colony_info(self):
        """Mevcut koloni durumunu göster"""
        print("\n" + "="*60)
        print("  GÜNCEL KOLONİ DURUMU")
        print("="*60)
        Display.show_colony_status(self.colony)
        print("="*60)
        print("\nDevam etmek için Enter'a basın...")
        input()
    
    def get_turn_summary(self, turn_number: int) -> Dict:
        """Belirli bir turun özetini döndür"""
        if 0 <= turn_number - 1 < len(self.turn_history):
            return self.turn_history[turn_number - 1]
        return None
    
    def get_game_statistics(self) -> Dict:
        """Oyun istatistiklerini döndür"""
        if not self.turn_history:
            return {}
        
        stats = {
            'total_turns_played': len(self.turn_history),
            'total_decisions_made': sum(len(t['results']) for t in self.turn_history),
            'average_support': 0,
            'phase_breakdown': {
                'setup': 0,
                'crisis': 0
            },
            'module_decisions': {}
        }
        
        # Ortalama destek hesapla
        all_supports = []
        for turn in self.turn_history:
            for result in turn['results']:
                all_supports.append(result['support_rate'])
                
                # Faz sayımı
                phase = result.get('phase', 'unknown')
                if phase in stats['phase_breakdown']:
                    stats['phase_breakdown'][phase] += 1
                
                # Modül sayımı
                module = result['module']
                if module not in stats['module_decisions']:
                    stats['module_decisions'][module] = 0
                stats['module_decisions'][module] += 1
        
        if all_supports:
            stats['average_support'] = sum(all_supports) / len(all_supports)
        
        return stats
    
    def save_game_history(self, filename: str = "game_history.json"):
        """Oyun geçmişini kaydet"""
        import json
        from datetime import datetime
        
        data = {
            'colony_name': self.colony.name,
            'date': datetime.now().isoformat(),
            'turns_played': len(self.turn_history),
            'history': self.turn_history,
            'final_metrics': self.colony.get_status_summary(),
            'statistics': self.get_game_statistics()
        }
        
        try:
            with open(f"data/{filename}", 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            print(f"💾 Oyun kaydedildi: data/{filename}")
        except Exception as e:
            print(f"❌ Kaydetme hatası: {e}")
