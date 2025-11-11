from typing import Dict, List, Tuple

# ============================================================================
# OYUN PARAMETRELERİ
# ============================================================================

class GameConfig:
    """Oyun yapılandırma sabitleri"""
    
    # Tur Ayarları
    TOTAL_TURNS: int = 7
    SETUP_PHASE_TURNS: int = 3  # İlk 3 tur kurulum
    CRISIS_PHASE_TURNS: int = 4  # Son 4 tur kriz
    
    # Koloni Başlangıç Değerleri
    POPULATION_SIZE: int = 1000
    STARTING_MONEY: float = 10000.0
    STARTING_ENVIRONMENT: float = 1.0
    STARTING_CRIME_RATE: float = 0.2
    STARTING_HAPPINESS: float = 0.5
    STARTING_ENERGY: float = 0.0
    
    # Karar Veritabanı
    DECISIONS_PER_MODULE: int = 12
    TOTAL_MODULES: int = 9
    TOTAL_DECISIONS: int = 108  # 9 modül × 12 karar
    MIN_OPTIONS_PER_DECISION: int = 2
    MAX_OPTIONS_PER_DECISION: int = 4
    
    # Performans
    DECISION_IMPACT_MULTIPLIER: float = 0.1  # Modül performans değişim hızı
    MOOD_UPDATE_MOMENTUM: float = 0.7  # Ruh hali değişim momentumu
    SOCIAL_CONTAGION_FACTOR: float = 0.2  # Sosyal bulaşma etkisi


class DifficultyConfig:
    """Zorluk seviyesi çarpanları"""
    
    DIFFICULTIES: Dict[str, Dict[str, float]] = {
        "easy": {
            "effect_multiplier": 0.5,  # Etkiler yarı yarıya
            "starting_money_bonus": 5000,
            "starting_happiness_bonus": 0.1,
            "description": "Rahat - Yeni başlayanlar için"
        },
        "normal": {
            "effect_multiplier": 1.0,  # Normal
            "starting_money_bonus": 0,
            "starting_happiness_bonus": 0.0,
            "description": "Normal - Dengeli deneyim"
        },
        "hard": {
            "effect_multiplier": 1.5,  # Etkiler 1.5x
            "starting_money_bonus": -2000,
            "starting_happiness_bonus": -0.1,
            "description": "Zor - Deneyimli oyuncular için"
        },
        "brutal": {
            "effect_multiplier": 2.0,  # Etkiler 2x
            "starting_money_bonus": -5000,
            "starting_happiness_bonus": -0.2,
            "description": "Acımasız - Uzmanlar için"
        }
    }
    
    DEFAULT_DIFFICULTY: str = "normal"


# ============================================================================
# MODÜL TANIMLARI
# ============================================================================

class ModuleConfig:
    """Modül isimleri ve özellikleri"""
    
    MODULE_NAMES: List[str] = [
        "⚖️ Adalet",
        "🛡️ Güvenlik", 
        "🏥 Sağlık",
        "🎓 Eğitim",
        "💰 Ekonomi",
        "🏛️ İçişleri",
        "🌍 Dışişleri",
        "🌱 Çevre",
        "🔬 Teknoloji"
    ]
    
    # Modül özellikleri (emoji olmadan)
    MODULE_KEYS: List[str] = [
        "Adalet", "Güvenlik", "Sağlık", "Eğitim", "Ekonomi",
        "İçişleri", "Dışişleri", "Çevre", "Teknoloji"
    ]
    
    # Modül başlangıç performansları
    DEFAULT_MODULE_PERFORMANCE: float = 0.5
    DEFAULT_MODULE_BUDGET_RATIO: float = 1.0 / 9  # Eşit dağıtım
    DEFAULT_EMPLOYEE_COUNT: int = 50


# ============================================================================
# METRİK LİMİTLERİ
# ============================================================================

class MetricLimits:
    """Metrik sınır değerleri"""
    
    # (min, max) tuple'ları
    HAPPINESS: Tuple[float, float] = (0.0, 1.0)
    MONEY: Tuple[float, float] = (-10000, 100000)
    ENVIRONMENT: Tuple[float, float] = (0.0, 1.0)
    CRIME_RATE: Tuple[float, float] = (0.0, 1.0)
    DEVELOPMENT: Tuple[float, float] = (0, 2000)
    ENERGY: Tuple[float, float] = (0, 10000)
    
    # Kritik eşik değerleri
    CRITICAL_HAPPINESS: float = 0.2  # Bu değerin altı tehlikeli
    CRITICAL_MONEY: float = 0  # Negatife geçerse sorun
    CRITICAL_ENVIRONMENT: float = 0.3  # Bu değerin altı tehlikeli
    CRITICAL_CRIME: float = 0.7  # Bu değerin üstü tehlikeli


# ============================================================================
# BAŞARI KRİTERLERİ
# ============================================================================

class SuccessThresholds:
    """Başarı değerlendirme eşikleri"""
    
    # Minimum başarı kriterleri (oyun sonu için)
    MIN_HAPPINESS: float = 0.6
    MIN_MONEY: float = 5000
    MIN_ENVIRONMENT: float = 0.5
    MAX_CRIME: float = 0.3  # Düşük olmalı
    MIN_DEVELOPMENT: float = 300
    
    # Notlandırma sistemi ağırlıkları (toplam 100)
    SCORING_WEIGHTS: Dict[str, float] = {
        "happiness": 30,      # 0-30 puan
        "money": 25,          # 0-25 puan
        "development": 20,    # 0-20 puan
        "environment": 15,    # 0-15 puan
        "crime": 10           # 0-10 puan (ters: düşük=yüksek puan)
    }
    
    # Not eşikleri
    GRADE_THRESHOLDS: Dict[str, float] = {
        "A+": 90, "A": 85, "A-": 80,
        "B+": 75, "B": 70, "B-": 65,
        "C+": 60, "C": 55, "C-": 50,
        "D": 40, "F": 0
    }


# ============================================================================
# GÖRÜNTÜLEME AYARLARI
# ============================================================================

class DisplayConfig:
    """Konsol görüntüleme ayarları"""
    
    # Çubuk uzunlukları
    PROGRESS_BAR_LENGTH: int = 20
    SUPPORT_BAR_LENGTH: int = 20
    
    # Renkler (terminal destekliyorsa)
    USE_COLORS: bool = False  # Şimdilik kapalı
    
    # Emoji kullanımı
    USE_EMOJIS: bool = True
    
    # Metrik sembolleri
    METRIC_SYMBOLS: Dict[str, str] = {
        "happiness": "😊",
        "money": "💰",
        "energy": "⚡",
        "environment": "🌱",
        "crime": "🚨",
        "development": "📈",
        "population": "👥"
    }
    
    # Faz sembolleri
    PHASE_SYMBOLS: Dict[str, str] = {
        "setup": "⚙️",
        "crisis": "🚨"
    }
    
    # Destek çubuğu renkleri (emoji)
    SUPPORT_COLORS: Dict[str, str] = {
        "high": "🟩",    # >= 0.7
        "medium": "🟨",  # 0.4 - 0.7
        "low": "🟥"      # < 0.4
    }


# ============================================================================
# DOSYA YÖNETİMİ
# ============================================================================

class PathConfig:
    """Dosya yolları"""
    
    # Klasörler
    DATA_DIR: str = "data"
    SAVE_DIR: str = "data/saves"
    EXPORT_DIR: str = "data/exports"
    LOG_DIR: str = "logs"
    
    # Dosya formatları
    SAVE_FILE_FORMAT: str = "save_{colony_name}_{timestamp}.json"
    EXPORT_FILE_FORMAT: str = "export_{colony_name}_{timestamp}.csv"
    LOG_FILE_FORMAT: str = "game_{timestamp}.log"


# ============================================================================
# OYUN MODELLERİ
# ============================================================================

class GameModes:
    """Farklı oyun modları (gelecek versiyonlar için)"""
    
    MODES: Dict[str, Dict[str, any]] = {
        "story": {
            "name": "Hikaye Modu",
            "description": "7 turlu standart hikaye",
            "turns": 7,
            "allow_save": True,
            "timed": False
        },
        "sandbox": {
            "name": "Sandbox Modu",
            "description": "Sınırsız kaynak, deneme amaçlı",
            "turns": -1,  # Sınırsız
            "allow_save": True,
            "timed": False
        },
        "challenge": {
            "name": "Meydan Okuma",
            "description": "Zor koşullar, sınırlı zaman",
            "turns": 5,
            "allow_save": False,
            "timed": True,
            "time_per_decision": 60  # saniye
        },
        "algorithm_battle": {
            "name": "Algoritma Savaşı",
            "description": "Farklı algoritmalar yarışır (Faz 2)",
            "turns": 7,
            "allow_save": False,
            "timed": False
        }
    }
    
    DEFAULT_MODE: str = "story"


# ============================================================================
# DİL AYARLARI
# ============================================================================

class LanguageConfig:
    """Çok dilli destek (gelecek versiyonlar için)"""
    
    SUPPORTED_LANGUAGES: List[str] = ["tr", "en"]
    DEFAULT_LANGUAGE: str = "tr"
    
    # Anahtar mesajlar
    MESSAGES: Dict[str, Dict[str, str]] = {
        "tr": {
            "welcome": "AlgoGov'a Hoş Geldiniz!",
            "game_over": "Oyun Bitti!",
            "turn": "Tur",
            "phase_setup": "KURULUM FAZI",
            "phase_crisis": "KRİZ YÖNETİMİ"
        },
        "en": {
            "welcome": "Welcome to AlgoGov!",
            "game_over": "Game Over!",
            "turn": "Turn",
            "phase_setup": "SETUP PHASE",
            "phase_crisis": "CRISIS MANAGEMENT"
        }
    }


# ============================================================================
# GELİŞMİŞ AYARLAR
# ============================================================================

class AdvancedConfig:
    """Gelişmiş ayarlar"""
    
    # Debug modu
    DEBUG_MODE: bool = False
    VERBOSE_LOGGING: bool = False
    
    # Performans
    USE_CACHING: bool = True
    MAX_CACHE_SIZE: int = 100
    
    # İstatistikler
    TRACK_STATISTICS: bool = True
    AUTO_SAVE_STATISTICS: bool = True
    
    # Validasyon
    VALIDATE_DECISIONS: bool = True
    STRICT_MODE: bool = False  # Katı hata kontrolü


# ============================================================================
# VERSİYON BİLGİSİ
# ============================================================================

class VersionInfo:
    """Sürüm bilgileri"""
    
    VERSION: str = "0.1.0"
    VERSION_NAME: str = "Alpha Genesis"
    RELEASE_DATE: str = "2025-01-11"
    
    # Özellik bayrakları
    FEATURES: Dict[str, bool] = {
        "phase_system": True,
        "save_load": False,  # Henüz yok
        "multiplayer": False,  # Faz 3
        "algorithms": False,  # Faz 2
        "web_ui": False  # Faz 3
    }


# ============================================================================
# YARDIMCI FONKSİYONLAR
# ============================================================================

def get_difficulty_multiplier(difficulty: str = "normal") -> float:
    """Zorluk çarpanını döndür"""
    return DifficultyConfig.DIFFICULTIES.get(
        difficulty, 
        DifficultyConfig.DIFFICULTIES["normal"]
    )["effect_multiplier"]


def validate_metric(metric_name: str, value: float) -> float:
    """Metrik değerini sınırlar içinde tut"""
    limits = {
        "happiness": MetricLimits.HAPPINESS,
        "money": MetricLimits.MONEY,
        "environment": MetricLimits.ENVIRONMENT,
        "crime_rate": MetricLimits.CRIME_RATE,
        "development": MetricLimits.DEVELOPMENT,
        "energy": MetricLimits.ENERGY
    }
    
    if metric_name in limits:
        min_val, max_val = limits[metric_name]
        return max(min_val, min(max_val, value))
    
    return value


def get_grade(score: float) -> str:
    """Skordan not hesapla"""
    for grade, threshold in SuccessThresholds.GRADE_THRESHOLDS.items():
        if score >= threshold:
            return grade
    return "F"


def is_critical_state(colony) -> Dict[str, bool]:
    """Koloninin kritik durumda olup olmadığını kontrol et"""
    return {
        "happiness": colony.metrics.happiness < MetricLimits.CRITICAL_HAPPINESS,
        "money": colony.metrics.money < MetricLimits.CRITICAL_MONEY,
        "environment": colony.metrics.environment < MetricLimits.CRITICAL_ENVIRONMENT,
        "crime": colony.metrics.crime_rate > MetricLimits.CRITICAL_CRIME
    }


# ============================================================================
# KULLANIM ÖRNEĞİ
# ============================================================================

if __name__ == "__main__":
    print("AlgoGov Configuration")
    print("=" * 60)
    print(f"Version: {VersionInfo.VERSION} ({VersionInfo.VERSION_NAME})")
    print(f"Total Turns: {GameConfig.TOTAL_TURNS}")
    print(f"Modules: {GameConfig.TOTAL_MODULES}")
    print(f"Total Decisions: {GameConfig.TOTAL_DECISIONS}")
    print()
    
    print("Difficulty Levels:")
    for name, config in DifficultyConfig.DIFFICULTIES.items():
        print(f"  {name.upper()}: {config['description']}")
    print()
    
    print("Modules:")
    for module in ModuleConfig.MODULE_NAMES:
        print(f"  {module}")
    print()
    
    print("Success Thresholds:")
    for metric, weight in SuccessThresholds.SCORING_WEIGHTS.items():
        print(f"  {metric}: {weight} points")
