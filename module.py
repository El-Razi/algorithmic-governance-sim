from dataclasses import dataclass
from typing import Dict

@dataclass
class Module:
    """Yönetim modülü"""
    
    name: str
    budget: float
    performance: float = 0.5  # 0-1 arası, modülün etkinliği
    employee_count: int = 50
    
    # Diğer modüllerle bağımlılıklar (gelecek versiyon için)
    dependencies: Dict[str, float] = None
    
    def __post_init__(self):
        if self.dependencies is None:
            self.dependencies = {}
    
    def update_performance(self, decision_impact: float):
        """
        Modül performansını güncelle
        
        Args:
            decision_impact: -1 ile 1 arası etki değeri
        """
        self.performance += decision_impact * 0.1
        # 0-1 arasına sınırla
        self.performance = max(0, min(1, self.performance))
    
    def allocate_budget(self, amount: float):
        """Modüle bütçe tahsis et"""
        self.budget += amount
    
    def __repr__(self):
        return f"Module({self.name}, budget={self.budget:.0f}, perf={self.performance:.2f})"
