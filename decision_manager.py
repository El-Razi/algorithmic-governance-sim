import random
from typing import List, Dict, Optional, Set
from ..decisions.decision_database import DECISION_DATABASE

class DecisionManager:
    """Kararları yöneten sınıf - v2.0"""
    
    def __init__(self):
        self.database = DECISION_DATABASE
        self.used_decisions: Set[str] = set()  # Kullanılan karar ID'leri
        self.module_used_decisions: Dict[str, Set[str]] = {}  # Modül bazında takip
        
        # Her modül için kullanılan kararları ayrı takip et
        for module_name in self.database.keys():
            self.module_used_decisions[module_name] = set()
    
    def get_all_decisions(self) -> List[Dict]:
        """Tüm kararları döndür"""
        all_decisions = []
        for module_name, decisions in self.database.items():
            for decision in decisions:
                all_decisions.append({
                    'module': module_name,
                    **decision
                })
        return all_decisions
    
    def get_decision_for_module(
        self, 
        module_name: str, 
        phase: Optional[str] = None, 
        avoid_repeats: bool = True
    ) -> Optional[Dict]:
        """
        Belirli bir modül için karar seç
        
        Args:
            module_name: Modül adı (ör. "⚖️ Adalet")
            phase: "setup" veya "crisis" - İlk 3 tur için setup, sonrası crisis
            avoid_repeats: Daha önce kullanılan kararları atla
        
        Returns:
            Karar dict'i veya None
        """
        if module_name not in self.database:
            print(f"⚠️ Uyarı: '{module_name}' modülü bulunamadı!")
            return None
        
        decisions = self.database[module_name]
        
        # Faz filtrelemesi
        if phase:
            decisions = [d for d in decisions if d.get('phase') == phase]
            
            # Eğer o fazda karar yoksa (eski format), tümünü kullan
            if not decisions:
                print(f"💡 '{module_name}' için {phase} fazı kararı yok, tüm havuzdan seçiliyor.")
                decisions = self.database[module_name]
        
        if avoid_repeats:
            # Bu modülde henüz kullanılmamış kararları filtrele
            module_used = self.module_used_decisions.get(module_name, set())
            available = [d for d in decisions if d['id'] not in module_used]
            
            # Eğer tüm kararlar kullanıldıysa, bu modül için sıfırla
            if not available:
                print(f"♻️  '{module_name}' havuzu tükendi, yeniden başlatılıyor...")
                self.module_used_decisions[module_name].clear()
                available = decisions
        else:
            available = decisions
        
        if not available:
            print(f"❌ '{module_name}' için kullanılabilir karar yok!")
            return None
        
        # Rastgele bir karar seç
        decision = random.choice(available)
        
        # Kullanıldı olarak işaretle
        self.used_decisions.add(decision['id'])
        self.module_used_decisions[module_name].add(decision['id'])
        
        return decision
    
    def get_decisions_for_turn(
        self, 
        module_names: List[str], 
        turn_number: int = 1
    ) -> Dict[str, Dict]:
        """
        Bir tur için tüm modüllerin kararlarını al
        
        Args:
            module_names: Modül isimleri listesi
            turn_number: Hangi tur (1-7)
        
        Returns:
            Modül adı -> Karar dict
        """
        turn_decisions = {}
        
        # İlk 3 tur setup fazı, sonrası crisis
        phase = "setup" if turn_number <= 3 else "crisis"
        
        print(f"🎯 Faz: {'KURULUM' if phase == 'setup' else 'KRİZ YÖNETİMİ'}")
        print(f"📊 Toplam modül: {len(module_names)}")
        print()
        
        for module_name in module_names:
            decision = self.get_decision_for_module(
                module_name, 
                phase=phase,
                avoid_repeats=True
            )
            if decision:
                turn_decisions[module_name] = decision
        
        return turn_decisions
    
    def get_statistics(self) -> Dict:
        """Karar kullanım istatistiklerini döndür"""
        stats = {
            'total_decisions': len(self.get_all_decisions()),
            'used_decisions': len(self.used_decisions),
            'remaining_decisions': len(self.get_all_decisions()) - len(self.used_decisions),
            'module_stats': {}
        }
        
        for module_name in self.database.keys():
            total = len(self.database[module_name])
            used = len(self.module_used_decisions.get(module_name, set()))
            stats['module_stats'][module_name] = {
                'total': total,
                'used': used,
                'remaining': total - used
            }
        
        return stats
    
    def reset_used_decisions(self, module_name: Optional[str] = None):
        """
        Kullanılan kararları sıfırla
        
        Args:
            module_name: Belirli bir modül için sıfırlama (None ise tümü)
        """
        if module_name:
            # Sadece belirli modülü sıfırla
            if module_name in self.module_used_decisions:
                # Bu modülün ID'lerini global set'ten de kaldır
                for decision_id in self.module_used_decisions[module_name]:
                    self.used_decisions.discard(decision_id)
                
                self.module_used_decisions[module_name].clear()
                print(f"♻️  '{module_name}' kararları sıfırlandı.")
        else:
            # Tüm modülleri sıfırla
            self.used_decisions.clear()
            for module in self.module_used_decisions:
                self.module_used_decisions[module].clear()
            print("♻️  Tüm kararlar sıfırlandı.")
    
    def get_decision_by_id(self, decision_id: str) -> Optional[Dict]:
        """ID ile karar bul"""
        for module_name, decisions in self.database.items():
            for decision in decisions:
                if decision['id'] == decision_id:
                    return {
                        'module': module_name,
                        **decision
                    }
        return None
    
    def get_phase_decisions(self, phase: str) -> List[Dict]:
        """
        Belirli bir fazdaki tüm kararları döndür
        
        Args:
            phase: "setup" veya "crisis"
        
        Returns:
            O fazdaki tüm kararlar
        """
        phase_decisions = []
        for module_name, decisions in self.database.items():
            for decision in decisions:
                if decision.get('phase') == phase:
                    phase_decisions.append({
                        'module': module_name,
                        **decision
                    })
        return phase_decisions
    
    def validate_database(self) -> Dict[str, List[str]]:
        """
        Veritabanını doğrula, sorunları tespit et
        
        Returns:
            Sorun listesi (her modül için)
        """
        issues = {}
        
        for module_name, decisions in self.database.items():
            module_issues = []
            
            # Her modülde 12 karar olmalı
            if len(decisions) != 12:
                module_issues.append(f"Karar sayısı: {len(decisions)} (12 olmalı)")
            
            # Her kararın ID'si unique olmalı
            ids = [d['id'] for d in decisions]
            if len(ids) != len(set(ids)):
                module_issues.append("Tekrarlayan ID var!")
            
            # Her kararın options'ı olmalı
            for decision in decisions:
                if 'options' not in decision:
                    module_issues.append(f"'{decision['id']}' options eksik!")
                elif len(decision['options']) < 2:
                    module_issues.append(f"'{decision['id']}' en az 2 seçenek olmalı!")
            
            if module_issues:
                issues[module_name] = module_issues
        
        return issues if issues else {"status": ["✅ Veritabanı sağlıklı!"]}
