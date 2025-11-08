import random
from typing import List, Dict, Optional
from ..decisions.decision_database import DECISION_DATABASE

class DecisionManager:
    """Kararları yöneten sınıf"""
    
    def __init__(self):
        self.database = DECISION_DATABASE
        self.used_decisions = set()  # Kullanılan kararları takip et
    
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
    
    def get_decision_for_module(self, module_name: str, avoid_repeats: bool = True) -> Optional[Dict]:
        """
        Belirli bir modül için karar seç
        
        Args:
            module_name: Modül adı
            avoid_repeats: Daha önce kullanılan kararları atla
        
        Returns:
            Karar dict'i veya None
        """
        if module_name not in self.database:
            return None
        
        decisions = self.database[module_name]
        
        if avoid_repeats:
            # Henüz kullanılmamış kararları filtrele
            available = [d for d in decisions if d['id'] not in self.used_decisions]
            
            # Eğer tüm kararlar kullanıldıysa, sıfırla
            if not available:
                self.used_decisions.clear()
                available = decisions
        else:
            available = decisions
        
        # Rastgele bir karar seç
        decision = random.choice(available)
        
        # Kullanıldı olarak işaretle
        self.used_decisions.add(decision['id'])
        
        return decision
    
    def get_decisions_for_turn(self, module_names: List[str]) -> Dict[str, Dict]:
        """
        Bir tur için tüm modüllerin kararlarını al
        
        Args:
            module_names: Modül isimleri listesi
        
        Returns:
            Modül adı -> Karar dict
        """
        turn_decisions = {}
        
        for module_name in module_names:
            decision = self.get_decision_for_module(module_name)
            if decision:
                turn_decisions[module_name] = decision
        
        return turn_decisions
    
    def reset_used_decisions(self):
        """Kullanılan kararları sıfırla"""
        self.used_decisions.clear()
