# 🤝 AlgoGov'a Katkıda Bulunma Kılavuzu

AlgoGov açık kaynak bir projedir ve topluluğun katkılarını memnuniyetle karşılıyoruz! Bu kılavuz, projeye nasıl katkıda bulunabileceğinizi detaylı olarak açıklar.

## 📋 İçindekiler

- [Davranış Kuralları](#davranış-kuralları)
- [Nasıl Başlarım?](#nasıl-başlarım)
- [Katkı Türleri](#katkı-türleri)
- [Geliştirme Süreci](#geliştirme-süreci)
- [Kod Standartları](#kod-standartları)
- [Commit Mesaj Kuralları](#commit-mesaj-kuralları)
- [Pull Request Süreci](#pull-request-süreci)
- [Test Yazma](#test-yazma)
- [Dokümantasyon](#dokümantasyon)

---

## 📜 Davranış Kuralları

### Taahhüdümüz

AlgoGov topluluğu olarak, herkese açık, kapsayıcı ve saygılı bir ortam yaratmayı taahhüt ediyoruz.

### Beklentilerimiz

**✅ Yapılması Gerekenler:**
- Saygılı ve yapıcı dil kullanın
- Farklı bakış açılarına açık olun
- Yapıcı geri bildirim verin ve kabul edin
- Topluluk yararını önceleyin
- Yeni katılımcılara yardımcı olun

**❌ Kabul Edilemez Davranışlar:**
- Taciz, hakaret veya aşağılayıcı yorumlar
- Kişisel saldırılar
- Başkalarının özel bilgilerini paylaşma
- Profesyonel olmayan davranışlar
- Spam veya trolleme

### Şikayet Süreci

Davranış kurallarının ihlal edildiğini düşünüyorsanız:
1. Durumu proje yöneticilerine bildirin: [email@example.com]
2. Şikayetiniz gizli tutulacak ve ciddi şekilde ele alınacaktır
3. 48 saat içinde yanıt alacaksınız

---

## 🚀 Nasıl Başlarım?

### 1. Projeyi Tanıyın

```bash
# Repo'yu klonlayın
git clone https://github.com/[username]/algogov-simulator.git
cd algogov-simulator

# README'yi okuyun
cat README.md

# İlk oyunu oynayın
python main.py
```

### 2. Geliştirme Ortamını Kurun

```bash
# Python 3.9+ kurulu olduğundan emin olun
python --version

# Sanal ortam oluşturun
python -m venv venv

# Aktifleştirin
# Linux/Mac:
source venv/bin/activate
# Windows:
venv\Scripts\activate

# Bağımlılıkları yükleyin (gelecekte)
pip install -r requirements.txt
```

### 3. Bir Issue Seçin

- [GitHub Issues](https://github.com/[username]/algogov-simulator/issues) sayfasını ziyaret edin
- "good first issue" veya "help wanted" etiketli issue'ları arayın
- Issue'ya yorum yaparak üzerinde çalıştığınızı belirtin

---

## 🎯 Katkı Türleri

### 1. 🐛 Bug Raporlama

**Bug bulduğunuzda:**

```markdown
**Başlık:** [BUG] Kısa açıklama

**Açıklama**
Ne oldu? Detaylı açıklayın.

**Yeniden Oluşturma Adımları**
1. '...' adımını izleyin
2. '...' seçeneğine tıklayın
3. Hatayı görün

**Beklenen Davranış**
Ne olması gerekiyordu?

**Ekran Görüntüleri**
Varsa ekleyin

**Ortam**
- OS: [ör. Ubuntu 22.04]
- Python: [ör. 3.9.7]
- Commit: [ör. a1b2c3d]

**Ek Bilgi**
Başka önemli detay var mı?
```

**Örnek Issue:**
```markdown
**Başlık:** [BUG] Mutluluk metriği negatif değer alabiliyor

**Açıklama**
Tur 5'te koloninin mutluluk metriği -0.15 değerine düştü. 
Bu 0-1 arası sınırlamayı ihlal ediyor.

**Yeniden Oluşturma**
1. 5 tur oyna
2. Her karardan "A" seçeneğini seç
3. Tur 5 sonunda mutluluğu kontrol et

**Beklenen Davranış**
Mutluluk değeri 0'ın altına düşmemeli.

**Ortam**
- OS: Windows 11
- Python: 3.10.2
- Commit: main branch
```

### 2. 💡 Özellik Önerisi

**Yeni özellik önerirken:**

```markdown
**Başlık:** [FEATURE] Kısa açıklama

**Problem**
Hangi sorunu çözüyor?

**Önerilen Çözüm**
Nasıl çalışmalı?

**Alternatifler**
Başka yaklaşımlar düşündünüz mü?

**Ek Bağlam**
Mockup, diyagram vb.

**Etki Analizi**
- Hangi dosyalar değişecek?
- Performans etkisi var mı?
- Breaking change mi?
```

**Örnek Özellik:**
```markdown
**Başlık:** [FEATURE] Oyunu duraklatma ve kaydetme

**Problem**
Oyun 7 tur sürdüğü için tek oturumda bitmeyebiliyor.

**Önerilen Çözüm**
- Her tur sonunda "Kaydet ve Çık" seçeneği
- JSON formatında oyun durumu kaydı
- Başlangıçta "Kaldığın yerden devam et" seçeneği

**Teknik Detay**
```python
# colony.save_state('save_game.json')
# colony.load_state('save_game.json')
```

**Etki**
- colony.py: save/load metodları
- main.py: menü seçenekleri
- Breaking change: Hayır
```

### 3. 📝 Yeni Karar Senaryosu Ekleme

**En kolay katkı türü!**

#### Karar Şablonu

```python
{
    "id": "module_xxx",
    "phase": "setup",  # veya "crisis"
    "title": "Karar Başlığı",
    "description": "YZ Analiz: Durum açıklaması. Sorun nedir?",
    "options": [
        {
            "id": "A",
            "text": "Seçenek açıklaması",
            "ethos": 0.6,    # 0.1-0.9 arası
            "pathos": 0.5,   # 0.1-0.9 arası
            "logos": 0.7,    # 0.1-0.9 arası
            "effects": {
                "money": -500,           # Para etkisi
                "energy": 50,            # Enerji etkisi
                "crime": -0.02,          # Suç oranı (-0.1 ile 0.1)
                "environment": 0.01      # Çevre (-0.1 ile 0.1)
            }
        },
        # ... en az 2, en fazla 4 seçenek
    ]
}
```

#### Karar Tasarım İlkeleri

**✅ İyi Karar Özellikleri:**
1. **Dengeli Seçenekler**: Her seçenek farklı ideolojiye hitap etmeli
2. **Anlamlı Trade-off'lar**: Her seçeneğin avantajı ve dezavantajı olmalı
3. **Temaya Uygunluk**: Uzay kolonisi bağlamında mantıklı olmalı
4. **Gerçekçi Etkiler**: Aşırı değerlerden kaçının

**❌ Kaçınılması Gerekenler:**
- Bir seçeneğin açıkça "en iyisi" olması
- Tüm seçeneklerin benzer EPL değerleri
- İlgisiz veya absürt senaryolar
- Aşırı politik veya tartışmalı konular

#### Örnek Karar

```python
{
    "id": "health_013",
    "phase": "crisis",
    "title": "Gen Tedavisi Talebi",
    "description": "YZ Analiz: Genetik hastalıklı bebekler için CRISPR tedavisi talep ediliyor. Teknoloji mevcut ama etik tartışmalı.",
    "options": [
        {
            "id": "A",
            "text": "Sınırlı İzin: Sadece ölümcül hastalıklar için",
            "ethos": 0.6,
            "pathos": 0.6,
            "logos": 0.8,
            "effects": {
                "money": -1500,
                "energy": 120,
                "crime": 0.01
            }
        },
        {
            "id": "B",
            "text": "Tam Serbestlik: Ebeveyn isterse yapılsın",
            "ethos": 0.3,
            "pathos": 0.7,
            "logos": 0.8,
            "effects": {
                "money": -2000,
                "energy": 150,
                "crime": 0.02
            }
        },
        {
            "id": "C",
            "text": "Yasak: Doğaya müdahale etik değil",
            "ethos": 0.8,
            "pathos": 0.4,
            "logos": 0.4,
            "effects": {
                "money": 0,
                "energy": 10,
                "crime": 0.03
            }
        }
    ]
}
```

#### Katkı Süreci

```bash
# 1. Branch oluştur
git checkout -b feature/add-health-decisions

# 2. decision_database.py'ı düzenle
# İlgili modüle yeni kararını ekle

# 3. Test et
python main.py
# Oynarken yeni kararını test et

# 4. Commit
git add src/decisions/decision_database.py
git commit -m "feat(decisions): add 3 new health decisions

- Gene therapy dilemma
- Pandemic protocol
- Mental health screening

Each decision has 3 balanced options with appropriate EPL values."

# 5. Push ve PR
git push origin feature/add-health-decisions
```

### 4. 🤖 Yeni Algoritma Geliştirme

**Faz 2 için hazırlık!**

#### Algoritma Şablonu

```python
# src/algorithms/your_algorithm.py

class YourAlgorithm:
    """
    Kısa açıklama: Bu algoritma ne yapar?
    
    Strateji: Hangi yaklaşımı kullanır?
    """
    
    def __init__(self):
        self.name = "Algorithm Name"
        self.description = "Detaylı açıklama"
        self.version = "1.0.0"
    
    def make_decision(self, colony, decision_options):
        """
        Verilen seçenekler arasından en iyisini seç
        
        Args:
            colony: Colony objesi (mevcut durum)
            decision_options: Liste[Dict] - Mevcut seçenekler
        
        Returns:
            Dict - Seçilen option
        """
        # Algoritma mantığınızı buraya yazın
        
        # Örnek: En yüksek desteği seç
        best_option = max(
            decision_options,
            key=lambda opt: colony.calculate_decision_support(opt)
        )
        
        return best_option
    
    def get_reasoning(self, chosen_option):
        """
        Neden bu seçeneği seçtik? (Opsiyonel)
        
        Returns:
            str - Açıklama
        """
        return f"Seçildi çünkü: {chosen_option['text']}"
```

#### Örnek Algoritmalar

**1. Greedy Happiness**
```python
def make_decision(self, colony, decision_options):
    """Her zaman en yüksek mutluluğu hedefle"""
    return max(decision_options, 
               key=lambda opt: self._predict_happiness(opt, colony))
```

**2. Risk Minimizer**
```python
def make_decision(self, colony, decision_options):
    """En düşük riskli seçeneği tercih et"""
    risks = [self._calculate_risk(opt) for opt in decision_options]
    min_risk_idx = risks.index(min(risks))
    return decision_options[min_risk_idx]
```

**3. Balanced Portfolio**
```python
def make_decision(self, colony, decision_options):
    """Tüm metrikleri dengele"""
    scores = []
    for opt in decision_options:
        score = (
            0.3 * self._predict_happiness(opt, colony) +
            0.3 * self._predict_economy(opt, colony) +
            0.2 * self._predict_environment(opt, colony) +
            0.2 * self._predict_stability(opt, colony)
        )
        scores.append(score)
    
    return decision_options[scores.index(max(scores))]
```

### 5. 🎨 UI/UX İyileştirmeleri

**Konsol çıktılarını güzelleştirin!**

#### Örnek İyileştirmeler

**Renkli Çıktı (opsiyonel):**
```python
# src/utils/colors.py
class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    RESET = '\033[0m'
    
    @staticmethod
    def error(text):
        return f"{Colors.RED}{text}{Colors.RESET}"
    
    @staticmethod
    def success(text):
        return f"{Colors.GREEN}{text}{Colors.RESET}"
```

**İlerleme Çubuğu:**
```python
def show_progress(current, total):
    """Animasyonlu ilerleme çubuğu"""
    percentage = current / total
    bar_length = 30
    filled = int(bar_length * percentage)
    
    bar = '█' * filled + '░' * (bar_length - filled)
    print(f"\r[{bar}] {percentage*100:.0f}%", end='', flush=True)
```

### 6. 📚 Dokümantasyon

**Dokümantasyon katkıları çok değerlidir!**

#### Dokümantasyon Türleri

1. **Kod Yorumları**
   ```python
   def calculate_support(self, decision_option: Dict[str, float]) -> float:
       """
       Bir karar seçeneğine olan desteği hesapla.
       
       Bu metod, karakterin EPL değerleri ile kararın EPL ağırlıklarını
       karşılaştırarak cosine similarity hesaplar.
       
       Args:
           decision_option: Karar seçeneği dict'i, 'ethos', 'pathos', 
                           'logos' anahtarlarını içermeli
       
       Returns:
           float: 0-1 arası destek oranı
       
       Example:
           >>> character = Character.generate_random("C001")
           >>> decision = {"ethos": 0.7, "pathos": 0.5, "logos": 0.3}
           >>> support = character.calculate_support(decision)
           >>> 0 <= support <= 1
           True
       """
   ```

2. **README Güncellemeleri**
   - Yeni özellikler
   - Kurulum adımları
   - Sorun giderme

3. **Wiki Sayfaları**
   - Detaylı rehberler
   - Tutorial'ler
   - Best practices

4. **Çeviri**
   - İngilizce README
   - Diğer diller

---

## 🔧 Geliştirme Süreci

### Git Workflow

```bash
# 1. Repo'yu fork edin (GitHub'da)

# 2. Fork'unuzu klonlayın
git clone https://github.com/YOUR-USERNAME/algogov-simulator.git
cd algogov-simulator

# 3. Upstream ekleyin
git remote add upstream https://github.com/ORIGINAL-OWNER/algogov-simulator.git

# 4. Feature branch oluşturun
git checkout -b feature/amazing-feature

# 5. Değişikliklerinizi yapın
# ... kod yazın ...

# 6. Test edin
python main.py
# veya
python -m pytest tests/

# 7. Commit yapın
git add .
git commit -m "feat: add amazing feature"

# 8. Upstream'i pull edin (güncel kalın)
git fetch upstream
git rebase upstream/main

# 9. Push edin
git push origin feature/amazing-feature

# 10. Pull Request oluşturun (GitHub'da)
```

### Branch İsimlendirme

```
feature/feature-name   # Yeni özellik
fix/bug-description    # Bug düzeltme
docs/update-readme     # Dokümantasyon
refactor/cleanup-code  # Yeniden yapılandırma
test/add-unit-tests    # Test ekleme
```

---

## 📏 Kod Standartları

### Python Style Guide

**PEP 8 uyumlu olun:**

```python
# ✅ İyi
def calculate_total_score(happiness: float, money: float) -> float:
    """Calculate weighted total score."""
    return happiness * 0.6 + (money / 10000) * 0.4

# ❌ Kötü
def calc(h,m):
    return h*0.6+m/10000*0.4
```

### İsimlendirme Kuralları

```python
# Classes: PascalCase
class DecisionManager:
    pass

# Functions/Methods: snake_case
def get_decision_for_module():
    pass

# Constants: UPPER_CASE
MAX_POPULATION = 1000
DEFAULT_MONEY = 10000

# Private: _leading_underscore
def _internal_method():
    pass

# Variables: snake_case
decision_count = 0
is_valid = True
```

### Type Hints

```python
from typing import List, Dict, Optional

def process_decisions(
    decisions: List[Dict[str, any]], 
    colony: Colony
) -> Optional[Dict]:
    """Always use type hints for clarity."""
    pass
```

### Docstrings

**Google Style:**

```python
def complex_function(param1: int, param2: str) -> bool:
    """
    One line summary.
    
    Longer description if needed. Explain what the function does,
    not how it does it.
    
    Args:
        param1: Description of param1
        param2: Description of param2
    
    Returns:
        Description of return value
    
    Raises:
        ValueError: When param1 is negative
    
    Example:
        >>> complex_function(5, "test")
        True
    """
    pass
```

### Kod Organizasyonu

```python
# 1. Standard library imports
import os
import sys
from typing import List

# 2. Third-party imports
import numpy as np

# 3. Local imports
from .colony import Colony
from .character import Character

# 4. Constants
MAX_TURNS = 7

# 5. Classes
class MyClass:
    pass

# 6. Functions
def my_function():
    pass

# 7. Main execution
if __name__ == "__main__":
    main()
```

---

## 💬 Commit Mesaj Kuralları

### Conventional Commits

Format: `<type>(<scope>): <subject>`

#### Types

- `feat`: Yeni özellik
- `fix`: Bug düzeltme
- `docs`: Dokümantasyon
- `style`: Formatting (kod davranışını değiştirmez)
- `refactor`: Yeniden yapılandırma
- `test`: Test ekleme/düzeltme
- `chore`: Build, CI/CD, dependencies

#### Örnekler

```bash
# Yeni özellik
git commit -m "feat(decisions): add 5 new technology decisions"

# Bug düzeltme
git commit -m "fix(colony): prevent happiness from going negative

- Added bounds check in update_mood()
- Clamp value between 0 and 1
- Fixes #42"

# Dokümantasyon
git commit -m "docs(readme): add installation instructions for Windows"

# Refactor
git commit -m "refactor(display): extract progress bar into separate function"

# Test
git commit -m "test(colony): add unit tests for metric calculations"
```

#### Detaylı Mesaj Yapısı

```
<type>(<scope>): <subject>

<body>

<footer>
```

**Örnek:**
```
feat(algorithms): add machine learning decision algorithm

Implemented a basic ML algorithm that learns from past decisions.
Uses scikit-learn's RandomForest to predict best outcomes.

Features:
- Trains on historical turn data
- Predicts happiness impact
- Balances exploration vs exploitation

Closes #15
```

---

## 🔍 Pull Request Süreci

### PR Açmadan Önce

**Checklist:**
- [ ] Kod çalışıyor ve test edildi
- [ ] Yeni testler eklendi (gerekiyorsa)
- [ ] Dokümantasyon güncellendi
- [ ] Commit mesajları düzenli
- [ ] Conflicts yok
- [ ] CONTRIBUTING.md okundu

### PR Şablonu

```markdown
## Özet
Bu PR ne yapıyor? Kısa açıklama.

## Değişiklikler
- [x] Yeni özellik eklendi
- [x] Bug düzeltildi
- [ ] Dokümantasyon güncellendi
- [ ] Testler eklendi

## Detaylar
Teknik detaylar, tasarım kararları, trade-off'lar.

## Test
Nasıl test edildi?
```bash
python main.py
# 7 tur oynadım, yeni kararlar çalışıyor
```

## Ekran Görüntüleri
Varsa ekleyin

## Breaking Changes
Var mı? Ne değişti?

## İlgili Issue
Fixes #123
Related to #456

## Checklist
- [x] Kod testi yapıldı
- [x] Dokümantasyon güncellendi
- [x] Commit mesajları uygun
- [x] CONTRIBUTING.md'ye uygun
```

### Review Süreci

1. **Otomatik Kontroller** (gelecekte)
   - Syntax check
   - Tests pass
   - Code coverage

2. **Maintainer Review**
   - Kod kalitesi
   - Tasarım uygunluğu
   - Dokümantasyon

3. **Değişiklik Talepleri**
   - Yorumları ele alın
   - Commit ekleyin
   - Push edin (otomatik güncellenir)

4. **Approval & Merge**
   - Onaylandığında merge edilir
   - Branch silinir

---

## 🧪 Test Yazma

### Test Yapısı

```python
# tests/test_colony.py
import pytest
from src.core.colony import Colony
from src.core.character import Character

class TestColony:
    """Colony sınıfı için testler"""
    
    def test_colony_initialization(self):
        """Koloni doğru başlatılıyor mu?"""
        colony = Colony(population_size=100, name="Test")
        
        assert colony.name == "Test"
        assert len(colony.population) == 100
        assert len(colony.modules) == 9
        assert 0 <= colony.metrics.happiness <= 1
    
    def test_happiness_bounds(self):
        """Mutluluk değeri sınırları aşmıyor mu?"""
        colony = Colony(100, "Test")
        
        # Extreme decision
        decision = {
            "ethos": 0, "pathos": 0, "logos": 0,
            "effects": {"money": -10000}
        }
        
        colony.apply_decision_effects(decision)
        
        # Happiness should stay in bounds
        assert 0 <= colony.metrics.happiness <= 1
    
    @pytest.mark.parametrize("size", [10, 100, 1000])
    def test_different_population_sizes(self, size):
        """Farklı nüfus boyutları çalışıyor mu?"""
        colony = Colony(population_size=size, name="Test")
        assert len(colony.population) == size
```

### Test Çalıştırma

```bash
# Tüm testler
pytest

# Belirli dosya
pytest tests/test_colony.py

# Verbose mode
pytest -v

# Coverage raporu
pytest --cov=src tests/
```

---

## 📖 Dokümantasyon Yazma

### Docstring Örneği

```python
def calculate_colony_score(colony: Colony) -> float:
    """
    Koloninin genel başarı skorunu hesapla.
    
    Skor, çeşitli metriklerin ağırlıklı toplamıdır:
    - Mutluluk (30%)
    - Para (25%)
    - Gelişme (20%)
    - Çevre (15%)
    - Düşük suç (10%)
    
    Args:
        colony: Skorlanacak Colony objesi
    
    Returns:
        0-100 arası skor değeri. Yüksek skor daha başarılı.
    
    Example:
        >>> colony = Colony(1000, "Test")
        >>> score = calculate_colony_score(colony)
        >>> 0 <= score <= 100
        True
    
    Note:
        Bu fonksiyon yan etki yaratmaz, sadece okuma yapar.
    """
    pass
```

### README Güncellemesi

Yeni özellik eklediyseniz README'yi güncelleyin:

```markdown
## Yeni Özellikler (v0.2)

### Kaydetme/Yükleme Sistemi

Artık oyununuzu kaydedip daha sonra devam edebilirsiniz!

\```bash
# Oyunda kaydetme
# Tur sonunda 's' tuşuna basın

# Yükleme
python main.py --load save_game.json
\```
```

---

## 🎯 Öncelikli Katkı Alanları

### Yüksek Öncelik
1. ✅ **Karar Veritabanı Genişletme** (En kolay!)
   - Her modül için 5-10 yeni karar
   - Mevcut: 108 karar
   - Hedef: 200+ karar

2. ✅ **Algoritma Geliştirme** (Faz 2 hazırlığı)
   - 7 farklı strateji gerekli
   - Utilitarian, Economist, ML-based vb.

3. ✅ **Test Coverage** (Kritik)
   - Unit testler
   - Integration testler
   - Mevcut: %0
   - Hedef: %80+

### Orta Öncelik
4. 🔧 **UI/UX İyileştirmeleri**
   - Renkli konsol çıktısı
   - Grafikler (matplotlib)
   - Progress bar'lar

5. 🔧 **Veri Analizi Araçları**
   - CSV export
   - Pandas dataframe'lere dönüştürme
   - Görselleştirme scriptleri

### Düşük Öncelik
6. 💡 **Web Arayüzü** (Faz 3)
   - FastAPI backend
   - React frontend
   - WebSocket real-time updates

---

## 🏆 İlk Katkınızı Yaptınız!

İlk PR'ınız merge edildiğinde:
- ✨ Contributors listesine ekleneceksiniz
- 🎖️ GitHub profilinizde görünecek
- 💬 Discord'da özel rol alacaksınız (gelecekte)

---

## 📞 Yardım ve İletişim

### Sorularınız mı var?

- 💬 [GitHub Discussions](https://github.com/[username]/algogov-simulator/discussions)
- 🐛 [GitHub Issues](https://github.com/[username]/algogov-simulator/issues)
- 📧 Email: [your-email]

### Faydalı Kaynaklar

- [Python Style Guide (PEP 8)](https://pep8.org/)
- [Git Best Practices](https://git-scm.com/book/en/v2)
- [Conventional Commits](https://www.conventionalcommits.org/)
- [How to Write a Git Commit Message](https://chris.beams.io/posts/git-commit/)

---

## 🙏 Teşekkürler!

AlgoGov'a katkıda bulunmayı düşündüğünüz için teşekkürler! Her katkı, büy
