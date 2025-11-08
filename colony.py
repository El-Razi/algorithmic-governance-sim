from typing import List, Dict
from dataclasses import dataclass, field
from .character import Character
from .module import Module

@dataclass
class ColonyMetrics:
    """Koloni metriklerini tutar"""
    happiness: float = 0.5  # 0-1 arası
    money: float = 10000.0  # Başlangıç bütçesi
    energy_consumed: float = 0.0
    environment: float = 1.0  # 0-1 arası, 1=temiz
    crime_rate: float = 0.2  # 0-1 arası
    development: float = 0.0  # Hesaplanan: çevre * enerji
    
    def calculate_development(self):
        """Gelişme metriğini hesapla"""
        self.development = self.environment * self.energy_consumed

@dataclass  
class Colony:
    """Ana koloni sınıfı"""
    
    name: str
    population_size: int = 1000
    turn: int = 0
    population: List[Character] = field(default_factory=list)
    modules: Dict[str, Module] = field(default_factory=dict)
    metrics: ColonyMetrics = field(default_factory=ColonyMetrics)
    history: List[Dict] = field(default_factory=list)
    
    def __post_init__(self):
        """Koloniyi başlat"""
        # Nüfusu oluştur
        self._generate_population()
        
        # Modülleri oluştur
        self._initialize_modules()
        
        # İlk metrikleri hesapla
        self._update_metrics()
    
    def _generate_population(self):
        """Koloninin nüfusunu oluştur"""
        self.population = [
            Character.generate_random(f"C{i:04d}")
            for i in range(self.population_size)
        ]
    
    def _initialize_modules(self):
        """9 yönetim modülünü başlat"""
        module_names = [
            "Adalet", "Güvenlik", "Sağlık", "Eğitim", "Ekonomi",
            "İçişleri", "Dışişleri", "Çevre", "Teknoloji"
        ]
        
        for name in module_names:
            self.modules[name] = Module(
                name=name,
                budget=self.metrics.money / len(module_names),
                performance=0.5
            )
    
    def _update_metrics(self):
        """Tüm metrikleri güncelle"""
        # Mutluluk: Tüm karakterlerin ruh halinin ortalaması
        if self.population:
            self.metrics.happiness = sum(c.mood for c in self.population) / len(self.population)
        
        # Gelişme metriğini hesapla
        self.metrics.calculate_development()
    
    def apply_decision_effects(self, decision_option: Dict):
        """
        Bir karar seçeneğinin etkilerini uygula
        
        Args:
            decision_option: Seçilen karar seçeneği
        """
        effects = decision_option.get('effects', {})
        
        # Para etkisi
        if 'money' in effects:
            self.metrics.money += effects['money']
        
        # Enerji etkisi
        if 'energy' in effects:
            self.metrics.energy_consumed += effects['energy']
        
        # Çevre etkisi
        if 'environment' in effects:
            self.metrics.environment = max(0, min(1, 
                self.metrics.environment + effects['environment']))
        
        # Suç oranı etkisi
        if 'crime' in effects:
            self.metrics.crime_rate = max(0, min(1,
                self.metrics.crime_rate + effects['crime']))
        
        # Karakterlerin ruh halini güncelle
        self._update_population_mood(decision_option)
        
        # Metrikleri yeniden hesapla
        self._update_metrics()
    
    def _update_population_mood(self, decision_option: Dict):
        """Karar sonrası nüfusun ruh halini güncelle"""
        # Her karakter için destek oranına göre ruh hali değişimi
        for character in self.population:
            support = character.calculate_support(decision_option)
            
            # Desteklenen kararlar mutluluk verir, desteklenmeyen üzer
            personal_benefit = (support - 0.5) * 0.2
            
            character.update_mood(self.metrics.happiness, personal_benefit)
    
    def calculate_decision_support(self, decision_option: Dict) -> float:
        """
        Bir karar seçeneğinin toplam destek oranını hesapla
        
        Returns:
            Nüfusun yüzde kaçının desteklediği (0-1)
        """
        if not self.population:
            return 0.5
        
        total_support = sum(
            character.calculate_support(decision_option)
            for character in self.population
        )
        
        return total_support / len(self.population)
    
    def advance_turn(self):
        """Bir sonraki tura geç"""
        # Mevcut durumu kaydet
        self.history.append({
            'turn': self.turn,
            'happiness': self.metrics.happiness,
            'money': self.metrics.money,
            'development': self.metrics.development,
            'environment': self.metrics.environment,
            'crime_rate': self.metrics.crime_rate
        })
        
        self.turn += 1
    
    def get_status_summary(self) -> Dict:
        """Koloni durumunun özetini döndür"""
        return {
            'turn': self.turn,
            'population': len(self.population),
            'happiness': self.metrics.happiness,
            'money': self.metrics.money,
            'development': self.metrics.development,
            'environment': self.metrics.environment,
            'crime_rate': self.metrics.crime_rate,
            'avg_ethos': sum(c.ethos for c in self.population) / len(self.population),
            'avg_pathos': sum(c.pathos for c in self.population) / len(self.population),
            'avg_logos': sum(c.logos for c in self.population) / len(self.population)
        }
