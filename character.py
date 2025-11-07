import random
from dataclasses import dataclass
from typing import List

@dataclass
class Character:
    """Kolonideki bir karakteri temsil eder"""
    
    id: str
    ethos: float  # 0-1 arası, ahlaki/otorite odaklı düşünce
    pathos: float  # 0-1 arası, duygusal/empatik düşünce
    logos: float   # 0-1 arası, mantıksal/rasyonel düşünce
    mood: float = 0.5  # 0-1 arası, şu anki ruh hali
    group: str = "citizen"  # Demografik grup
    
    def __post_init__(self):
        """Oranların toplamının 1 olmasını sağla"""
        total = self.ethos + self.pathos + self.logos
        if total > 0:
            self.ethos /= total
            self.pathos /= total
            self.logos /= total
    
    @classmethod
    def generate_random(cls, id: str) -> 'Character':
        """Rastgele bir karakter üret"""
        # Rastgele ağırlıklar oluştur
        ethos = random.uniform(0.1, 1.0)
        pathos = random.uniform(0.1, 1.0)
        logos = random.uniform(0.1, 1.0)
        
        # Rastgele bir grup seç
        groups = ["citizen", "worker", "intellectual", "traditionalist", "progressive"]
        group = random.choice(groups)
        
        return cls(
            id=id,
            ethos=ethos,
            pathos=pathos,
            logos=logos,
            mood=random.uniform(0.3, 0.7),
            group=group
        )
    
    def calculate_support(self, decision_option: dict) -> float:
        """
        Bir karar seçeneğine olan desteği hesapla
        
        Args:
            decision_option: Karar seçeneği (ethos, pathos, logos ağırlıklarını içerir)
        
        Returns:
            0-1 arası destek oranı
        """
        # İdeolojik uyum (cosine similarity benzeri)
        ideology_match = (
            decision_option['ethos'] * self.ethos +
            decision_option['pathos'] * self.pathos +
            decision_option['logos'] * self.logos
        )
        
        # Ruh hali etkisi (mutlu insanlar daha destekleyici)
        mood_factor = 0.8 + (self.mood * 0.4)  # 0.8 - 1.2 arası
        
        # Nihai destek
        support = ideology_match * mood_factor
        
        # 0-1 arasına sınırla
        return max(0, min(1, support))
    
    def update_mood(self, colony_happiness: float, personal_benefit: float):
        """
        Karakterin ruh halini güncelle
        
        Args:
            colony_happiness: Genel koloni mutluluğu (0-1)
            personal_benefit: Kişisel kazanç/kayıp (-1 ile 1 arası)
        """
        # Sosyal bulaşma: Koloni mutluluğu etkisi
        social_effect = (colony_happiness - 0.5) * 0.2
        
        # Kişisel etki
        personal_effect = personal_benefit * 0.3
        
        # Yavaş değişim (momentum)
        momentum = 0.7
        
        # Yeni ruh hali
        new_mood = self.mood * momentum + social_effect + personal_effect
        
        # 0-1 arasına sınırla
        self.mood = max(0, min(1, new_mood))
    
    def __repr__(self):
        return (f"Character({self.id}, "
                f"E:{self.ethos:.2f} P:{self.pathos:.2f} L:{self.logos:.2f}, "
                f"mood:{self.mood:.2f})")
