# 🏛️ AlgoGov: Algorithmic Governance Simulator

## 📌 Mevcut Diller | Available Languages | 可用语言 | Idiomas Disponibles
- [Türkçe](#-türkçe-versiyon)
- [English](#-english-version)
- [中文](#-chinese-version)
- [Español](#-spanish-version)

---

# türkçe versiyon
## 🎯 Proje Hakkında

AlgoGov, 1000 kişilik bir uzay kolonisinde farklı yönetim modellerini test etmek için tasarlanmış interaktif bir simülasyondur. Proje, dijital demokrasi, algoritmik karar alma ve katılımcı yönetişim konularında deneysel araştırma yapmayı hedefler.

### Ana Özellikler

- 🧑‍🤝‍🧑 **1000 Karakterli Dinamik Toplum**: Her biri Ethos-Pathos-Logos dengesiyle karakterize edilmiş bireyler
- 🏛️ **9 Yönetim Modülü**: Adalet, Güvenlik, Sağlık, Eğitim, Ekonomi, İçişleri, Dışişleri, Çevre, Teknoloji
- 🎮 **3 Aşamalı Deney**: İnsan → Algoritma → Hibrit yönetim modelleri
- 📊 **Gerçek Zamanlı Metrikler**: Mutluluk, ekonomi, çevre, suç, gelişme
- 🔬 **Bilimsel Metodoloji**: Tekrarlanabilir, veri odaklı araştırma

## 🚀 Hızlı Başlangıç

### Gereksinimler

- Python 3.9 veya üzeri
- Hiçbir ek paket gerekmez! (Sadece standard library)

### Kurulum

```bash
# Repo'yu klonla
git clone https://github.com/[your-username]/algogov-simulator.git
cd algogov-simulator

# Doğrudan çalıştır (sanal ortam opsiyonel)
python main.py
```

### İlk Oyununuz

```bash
$ python main.py

============================================================
  ALGOGOV: Algorithmic Governance Simulator v0.1
============================================================

🏗️  Koloni başlatılıyor...
✅ Alpha Colony hazır! Nüfus: 1000

📋 Karar veritabanı yüklendi: 100 karar

Simülasyona başlamak için Enter'a basın...
```

## 📁 Proje Yapısı

```
algogov-simulator/
│
├── main.py                    # Ana giriş noktası
├── requirements.txt           # Python bağımlılıkları (şimdilik boş)
├── README.md                  # Bu dosya
│
├── src/
│   ├── core/                  # Temel sınıflar
│   │   ├── character.py       # Karakter sistemi
│   │   ├── colony.py          # Koloni yönetimi
│   │   ├── module.py          # Yönetim modülleri
│   │   └── decision_manager.py# Karar yöneticisi
│   │
│   ├── decisions/             # Karar veritabanı
│   │   └── decision_database.py # 100 karar (9 modül × 7-10 karar)
│   │
│   ├── simulation/            # Simülasyon motoru
│   │   └── game_loop.py       # Oyun döngüsü
│   │
│   ├── algorithms/            # Yönetim algoritmaları (Faz 2)
│   │   └── (gelecekte eklenecek)
│   │
│   └── utils/                 # Yardımcı araçlar
│       └── display.py         # Konsol görüntüleme
│
├── tests/                     # Birim testler
│   └── (gelecekte eklenecek)
│
├── data/                      # Simülasyon sonuçları
│   └── (otomatik oluşturulur)
│
└── docs/                      # Dokümantasyon
    ├── game_design.md         # Oyun tasarım dokümanı
    ├── algorithm_specs.md     # Algoritma detayları
    └── research_questions.md  # Araştırma soruları
```

## 🎮 Nasıl Oynanır?

### Faz 1: Manuel Yönetim (İlk Versiyon)

Siz koloni yöneticisisiniz! Her turda 9 farklı modül için kararlar alacaksınız.

#### Karar Alma Süreci

1. **Karar Sunulur**: Her modül için bir sorun ve 2-4 seçenek gösterilir
2. **Seçenekleri İnceleyin**: Her seçeneğin özellikleri:
   - **Ethos/Pathos/Logos Ağırlıkları**: İdeolojik karakteristik
   - **Etkiler**: Para, enerji, çevre, suç oranına etkisi
   - **Destek Oranı**: Nüfusun ne kadarının destekleyeceği
3. **Seçim Yapın**: Numarasını yazıp Enter'a basın
4. **Sonuçları İzleyin**: Seçiminiz koloninizi nasıl etkiledi?

#### Örnek Karar

```
────────────────────────────────────────────────────────────
🏛️  MODÜL: Sağlık
📋 KARAR: Sağlık Sisteminin Yapısı
❓ Koloninin sağlık hizmetleri nasıl organize edilmeli?

1. Ücretsiz Evrensel Sağlık: Herkes için tam kapsamlı
   💭 Ethos: 0.4 | Pathos: 0.9 | Logos: 0.5
   📊 Etkiler: money -1200, energy 100
   👥 Tahmini Destek: 67.3%

2. Özel + Kamu Karma: Temel hizmetler ücretsiz
   💭 Ethos: 0.5 | Pathos: 0.5 | Logos: 0.7
   📊 Etkiler: money -600, energy 60, crime 0.01
   👥 Tahmini Destek: 58.2%

3. Sigortaya Dayalı: Herkes kendi sigortasını alır
   💭 Ethos: 0.7 | Pathos: 0.2 | Logos: 0.8
   📊 Etkiler: money -200, energy 30, crime 0.02
   👥 Tahmini Destek: 42.1%

Seçiminiz (1-3): 
```

### Metrikler

Kararlarınız 5 ana metriği etkiler:

- 😊 **Mutluluk** (0-100%): Nüfusun genel ruh hali
- 💰 **Para**: Koloni bütçesi (başlangıç: 10,000)
- 📈 **Gelişme**: Çevre kalitesi × Enerji tüketimi
- 🌱 **Çevre** (0-100%): Çevresel sürdürülebilirlik
- 🚨 **Suç Oranı** (0-100%): Düşük olması iyidir

## 🧠 Ethos-Pathos-Logos Sistemi

Her karakter ve karar seçeneği üç ideolojik boyutta ağırlıklandırılır:

### Ethos (Ahlak/Otorite) 
- Geleneksel değerler
- Hiyerarşi ve otorite
- Toplumsal düzen

### Pathos (Duygu/Empati)
- Duygusal bağ
- Sosyal adalet
- Toplumsal refah

### Logos (Mantık/Akıl)
- Rasyonel analiz
- Verimlilik
- Pragmatik çözümler

**Destek Hesaplama**: Bir karakterin bir kararı destekleme olasılığı, karakter ve karar ağırlıklarının benzerliğine (cosine similarity) bağlıdır.

## 🔬 Araştırma Amaçları

Bu simülasyon şu soruları yanıtlamayı hedefler:

1. **Yönetim Modelleri**: Hangi karar stratejisi (insan, algoritma, hibrit) en başarılı?
2. **Toplumsal Tercihler**: Farklı karakter kompozisyonları nasıl sonuçlar üretir?
3. **Kısa vs Uzun Vade**: Popülist kararlar mı yoksa uzun vadeli planlama mı daha etkili?
4. **Demokratik Meşruiyet**: Destek oranı yüksek kararlar her zaman en iyisi mi?
5. **Çok Boyutlu Optimizasyon**: Tüm metrikleri dengelemek mümkün mü?

## 🗺️ Yol Haritası

### ✅ v0.1 - İlk MVP (Gelecek)
- [x] Temel koloni simülasyonu
- [x] 9 modül × 7 karar = 100 karar veritabanı
- [x] Manuel karar alma arayüzü
- [x] 5 temel metrik takibi
- [x] Konsol tabanlı görselleştirme

### 🔄 v0.2 - Algoritma Yarışması 
- [ ] 7 farklı algoritma implementasyonu
- [ ] Otomatik simülasyon modu
- [ ] Algoritma performans karşılaştırması
- [ ] CSV/JSON veri export

### 🚧 v0.3 - Web Arayüzü
- [ ] FastAPI backend
- [ ] React frontend
- [ ] Gerçek zamanlı grafikler
- [ ] Karar geçmişi görselleştirme

### 🌟 v1.0 - Multiplayer
- [ ] Kullanıcı hesap sistemi
- [ ] Gerçek oyuncular ile hibrit mod
- [ ] Her 7 turda algoritma seçimi
- [ ] Liderboard ve karşılaştırma

## 🤝 Katkıda Bulunma

Katkılarınızı bekliyoruz! İşte yapabilecekleriniz:

### Kolay Katkılar
- 📝 Yeni karar senaryoları yazma
- 🐛 Bug raporları
- 📚 Dokümantasyon iyileştirme
- 🌐 Çeviri (İngilizce/diğer diller)

### Orta Seviye
- 🎨 Görselleştirme iyileştirmeleri
- 🔢 Yeni metrik önerileri
- ⚙️ Performans optimizasyonları
- 🧪 Test yazma

### İleri Seviye
- 🤖 Yeni algoritma stratejileri
- 🌐 Web arayüzü geliştirme
- 📊 Veri analiz araçları
- 🎮 Oyun mekaniği eklentileri

### Katkı Süreci

1. Fork yapın
2. Feature branch oluşturun (`git checkout -b feature/amazing-feature`)
3. Commit yapın (`git commit -m 'Add some amazing feature'`)
4. Push edin (`git push origin feature/amazing-feature`)
5. Pull Request açın

## 📄 Lisans

Bu proje MIT lisansı altında açık kaynak olarak sunulmaktadır. Detaylar için [LICENSE](LICENSE) dosyasına bakın.

## 🙏 İlham Kaynakları

- [Pol.is](https://pol.is) - Konsensüs bulma algoritması
- [Decidim](https://decidim.org) - Katılımcı demokrasi platformu
- [vTaiwan](https://info.vtaiwan.tw) - Dijital yönetişim deneyi
- Democracy 3 & 4 - Yönetim simülasyon oyunları

## 📬 İletişim

- **GitHub Issues**: Bug raporu ve özellik önerileri
- **GitHub Discussions**: Genel tartışmalar ve sorular
- **Email**: [elrazi00@protonmail.com]

## 🌟 Yıldızlayın!

Bu projeyi beğendiyseniz, GitHub'da ⭐ vermeyi unutmayın!

---

**Not**: Bu proje aktif geliştirme aşamasındadır. İlk kararlı sürüm olan v1.0 için yol haritasını takip edin.

#  English Version

# 🏛️ AlgoGov: Algorithmic Governance Simulator

**An open-source game platform simulating algorithmic governance and digital democracy**

## 🎯 About the Project

AlgoGov is an interactive simulation designed to test different governance models in a 1000-person space colony. The project aims to conduct experimental research on digital democracy, algorithmic decision-making, and participatory governance.

### Main Features

- 🧑‍🤝‍🧑 **Dynamic Society of 1000 Characters**: Each individual characterized by Ethos-Pathos-Logos balance
- 🏛️ **9 Governance Modules**: Justice, Security, Health, Education, Economy, Internal Affairs, Foreign Affairs, Environment, Technology
- 🎮 **3-Phase Experiment**: Human → Algorithm → Hybrid governance models
- 📊 **Real-Time Metrics**: Happiness, economy, environment, crime, development
- 🔬 **Scientific Methodology**: Repeatable, data-driven research

## 🚀 Quick Start

### Requirements

- Python 3.9 or higher
- No additional packages needed! (Standard library only)

### Installation

```bash
# Clone the repository
git clone https://github.com/[your-username]/algogov-simulator.git
cd algogov-simulator

# Run directly (virtual environment optional)
python main.py
```

### Your First Game

```bash
$ python main.py

============================================================
  ALGOGOV: Algorithmic Governance Simulator v0.1
============================================================

🏗️  Initializing colony...
✅ Alpha Colony ready! Population: 1000

📋 Decision database loaded: 100 decisions

Press Enter to begin simulation...
```

## 📁 Project Structure

```
algogov-simulator/
│
├── main.py                    # Main entry point
├── requirements.txt           # Python dependencies (empty for now)
├── README.md                  # This file
│
├── src/
│   ├── core/                  # Core classes
│   │   ├── character.py       # Character system
│   │   ├── colony.py          # Colony management
│   │   ├── module.py          # Governance modules
│   │   └── decision_manager.py# Decision manager
│   │
│   ├── decisions/             # Decision database
│   │   └── decision_database.py # 100 decisions (9 modules × 7-10 decisions)
│   │
│   ├── simulation/            # Simulation engine
│   │   └── game_loop.py       # Game loop
│   │
│   ├── algorithms/            # Governance algorithms (Phase 2)
│   │   └── (to be added)
│   │
│   └── utils/                 # Utilities
│       └── display.py         # Console display
│
├── tests/                     # Unit tests
│   └── (to be added)
│
├── data/                      # Simulation results
│   └── (auto-generated)
│
└── docs/                      # Documentation
    ├── game_design.md         # Game design document
    ├── algorithm_specs.md     # Algorithm details
    └── research_questions.md  # Research questions
```

## 🎮 How to Play?

### Phase 1: Manual Governance (Current Version)

You are the colony administrator! Each turn you'll make decisions for 9 different modules.

#### Decision Making Process

1. **A Decision is Presented**: Each module presents a problem with 2-4 options
2. **Examine Options**: Each option shows:
   - **Ethos/Pathos/Logos Weights**: Ideological characteristics
   - **Impact**: Effects on money, energy, environment, crime rate
   - **Support Rate**: What percentage of population would support this
3. **Make Your Choice**: Type the number and press Enter
4. **Watch Results**: See how your decision affects your colony

#### Example Decision

```
────────────────────────────────────────────────────────────
🏛️  MODULE: Health
📋 DECISION: Health System Structure
❓ How should the colony's health services be organized?

1. Free Universal Healthcare: Full coverage for everyone
   💭 Ethos: 0.4 | Pathos: 0.9 | Logos: 0.5
   📊 Impact: money -1200, energy 100
   👥 Estimated Support: 67.3%

2. Mixed Public-Private: Basic services free
   💭 Ethos: 0.5 | Pathos: 0.5 | Logos: 0.7
   📊 Impact: money -600, energy 60, crime 0.01
   👥 Estimated Support: 58.2%

3. Insurance-Based: Everyone buys their own insurance
   💭 Ethos: 0.7 | Pathos: 0.2 | Logos: 0.8
   📊 Impact: money -200, energy 30, crime 0.02
   👥 Estimated Support: 42.1%

Your choice (1-3): 
```

### Metrics

Your decisions affect 5 main metrics:

- 😊 **Happiness** (0-100%): Population's general mood
- 💰 **Money**: Colony budget (starting: 10,000)
- 📈 **Development**: Environmental quality × Energy consumption
- 🌱 **Environment** (0-100%): Environmental sustainability
- 🚨 **Crime Rate** (0-100%): Lower is better

## 🧠 Ethos-Pathos-Logos System

Each character and decision option is weighted across three ideological dimensions:

### Ethos (Morality/Authority)
- Traditional values
- Hierarchy and authority
- Social order

### Pathos (Emotion/Empathy)
- Emotional connection
- Social justice
- Community welfare

### Logos (Logic/Reason)
- Rational analysis
- Efficiency
- Pragmatic solutions

**Support Calculation**: A character's likelihood of supporting a decision depends on the similarity between character and decision weights (cosine similarity).

## 🔬 Research Objectives

This simulation aims to answer these questions:

1. **Governance Models**: Which decision strategy (human, algorithm, hybrid) is most successful?
2. **Societal Preferences**: How do different character compositions produce different results?
3. **Short vs Long Term**: Are populist decisions or long-term planning more effective?
4. **Democratic Legitimacy**: Is high support always the best decision?
5. **Multi-dimensional Optimization**: Is it possible to balance all metrics?

## 🗺️ Roadmap

### ✅ v0.1 - Initial MVP (Coming Soon)
- [x] Basic colony simulation
- [x] 9 modules × 7 decisions = 100 decision database
- [x] Manual decision-making interface
- [x] 5 core metrics tracking
- [x] Console-based visualization

### 🔄 v0.2 - Algorithm Competition
- [ ] 7 different algorithm implementations
- [ ] Automatic simulation mode
- [ ] Algorithm performance comparison
- [ ] CSV/JSON data export

### 🚧 v0.3 - Web Interface
- [ ] FastAPI backend
- [ ] React frontend
- [ ] Real-time graphics
- [ ] Decision history visualization

### 🌟 v1.0 - Multiplayer
- [ ] User account system
- [ ] Hybrid mode with real players
- [ ] Algorithm selection every 7 turns
- [ ] Leaderboard and comparisons

## 🤝 Contributing

We welcome your contributions! Here's what you can do:

### Easy Contributions
- 📝 Write new decision scenarios
- 🐛 Report bugs
- 📚 Improve documentation
- 🌐 Translations (English/other languages)

### Intermediate Level
- 🎨 Visualization improvements
- 🔢 New metric suggestions
- ⚙️ Performance optimizations
- 🧪 Write tests

### Advanced Level
- 🤖 New algorithm strategies
- 🌐 Web interface development
- 📊 Data analysis tools
- 🎮 Game mechanic extensions

### Contributing Process

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is open source under the MIT License. See [LICENSE](LICENSE) file for details.

## 🙏 Inspirations

- [Pol.is](https://pol.is) - Consensus finding algorithm
- [Decidim](https://decidim.org) - Participatory democracy platform
- [vTaiwan](https://info.vtaiwan.tw) - Digital governance experiment
- Democracy 3 & 4 - Governance simulation games

## 📬 Contact

- **GitHub Issues**: Bug reports and feature requests
- **GitHub Discussions**: General discussions and questions
- **Email**: [elrazi00@protonmail.com]

## 🌟 Star us!

If you like this project, don't forget to give us a ⭐ on GitHub!

---

**Note**: This project is in active development. Follow the roadmap for the stable v1.0 release.

---

#  Chinese Version

# 🏛️ AlgoGov: 算法治理模拟器

**一个开源游戏平台，用于模拟算法治理和数字民主**

## 🎯 项目介绍

AlgoGov 是一个交互式模拟系统，旨在测试 1000 人太空殖民地中的不同治理模式。该项目致力于对数字民主、算法决策和参与式治理进行实验性研究。

### 主要功能

- 🧑‍🤝‍🧑 **1000 个角色的动态社会**：每个个体都由伦理-情感-逻辑平衡表征
- 🏛️ **9 个治理模块**：司法、安全、卫生、教育、经济、内政、外交、环境、技术
- 🎮 **3 阶段实验**：人类 → 算法 → 混合治理模式
- 📊 **实时指标**：幸福度、经济、环境、犯罪、发展
- 🔬 **科学方法论**：可重复的、数据驱动的研究

## 🚀 快速开始

### 系统要求

- Python 3.9 或更高版本
- 无需额外包！（仅标准库）

### 安装

```bash
# 克隆仓库
git clone https://github.com/[your-username]/algogov-simulator.git
cd algogov-simulator

# 直接运行（虚拟环境可选）
python main.py
```

### 开始你的第一场游戏

```bash
$ python main.py

============================================================
  ALGOGOV: 算法治理模拟器 v0.1
============================================================

🏗️  初始化殖民地...
✅ Alpha 殖民地就绪！人口：1000

📋 决策数据库已加载：100 个决策

按 Enter 开始模拟...
```

## 📁 项目结构

```
algogov-simulator/
│
├── main.py                    # 主入口
├── requirements.txt           # Python 依赖（暂为空）
├── README.md                  # 此文件
│
├── src/
│   ├── core/                  # 核心类
│   │   ├── character.py       # 角色系统
│   │   ├── colony.py          # 殖民地管理
│   │   ├── module.py          # 治理模块
│   │   └── decision_manager.py# 决策管理器
│   │
│   ├── decisions/             # 决策数据库
│   │   └── decision_database.py # 100 个决策（9 个模块 × 7-10 个决策）
│   │
│   ├── simulation/            # 模拟引擎
│   │   └── game_loop.py       # 游戏循环
│   │
│   ├── algorithms/            # 治理算法（第 2 阶段）
│   │   └── (待添加)
│   │
│   └── utils/                 # 工具类
│       └── display.py         # 控制台显示
│
├── tests/                     # 单元测试
│   └── (待添加)
│
├── data/                      # 模拟结果
│   └── (自动生成)
│
└── docs/                      # 文档
    ├── game_design.md         # 游戏设计文档
    ├── algorithm_specs.md     # 算法详情
    └── research_questions.md  # 研究问题
```

## 🎮 如何游玩？

### 第 1 阶段：人工治理（当前版本）

你是殖民地管理员！每一回合你需要为 9 个不同的模块做出决策。

#### 决策流程

1. **呈现决策**：每个模块提出一个问题和 2-4 个选项
2. **查看选项**：每个选项显示：
   - **伦理/情感/逻辑权重**：意识形态特征
   - **影响**：对金钱、能源、环境、犯罪率的影响
   - **支持率**：人口中支持该选项的百分比
3. **做出选择**：输入编号并按 Enter
4. **观察结果**：看你的决策如何影响殖民地

#### 决策示例

```
────────────────────────────────────────────────────────────
🏛️  模块：卫生
📋 决策：卫生系统结构
❓ 殖民地的卫生服务应如何组织？

1. 免费通用医疗：全民全覆盖
   💭 伦理：0.4 | 情感：0.9 | 逻辑：0.5
   📊 影响：金钱 -1200，能源 100
   👥 预计支持：67.3%

2. 公私混合：基础服务免费
   💭 伦理：0.5 | 情感：0.5 | 逻辑：0.7
   📊 影响：金钱 -600，能源 60，犯罪 0.01
   👥 预计支持：58.2%

3. 保险制度：个人购买保险
   💭 伦理：0.7 | 情感：0.2 | 逻辑：0.8
   📊 影响：金钱 -200，能源 30，犯罪 0.02
   👥 预计支持：42.1%

你的选择 (1-3)：
```

### 核心指标

你的决策会影响 5 个主要指标：

- 😊 **幸福度** (0-100%)：人口总体情绪
- 💰 **金钱**：殖民地预算（初始：10,000）
- 📈 **发展**：环境质量 × 能源消耗
- 🌱 **环境** (0-100%)：环境可持续性
- 🚨 **犯罪率** (0-100%)：越低越好

## 🧠 伦理-情感-逻辑系统

每个角色和决策选项都在三个意识形态维度上加权：

### 伦理（道德/权威）
- 传统价值观
- 等级制度和权威
- 社会秩序

### 情感（情绪/同理心）
- 情感联系
- 社会公正
- 社区福祉

### 逻辑（理性/推理）
- 理性分析
- 效率
- 实用解决方案

**支持率计算**：角色支持某项决策的可能性取决于角色和决策权重的相似度（余弦相似度）。

## 🔬 研究目标

本模拟系统旨在回答以下问题：

1. **治理模式**：哪种决策策略（人类、算法、混合）最成功？
2. **社会偏好**：不同角色组合如何产生不同结果？
3. **短期 vs 长期**：民粹主义决策还是长期规划更有效？
4. **民主合法性**：高支持率决策总是最好的吗？
5. **多维优化**：能否平衡所有指标？

## 🗺️ 开发路线图

### ✅ v0.1 - 初始 MVP（即将推出）
- [x] 基础殖民地模拟
- [x] 9 个模块 × 7 个决策 = 100 个决策数据库
- [x] 人工决策界面
- [x] 5 项核心指标跟踪
- [x] 基于控制台的可视化

### 🔄 v0.2 - 算法竞赛
- [ ] 7 种不同算法实现
- [ ] 自动模拟模式
- [ ] 算法性能对比
- [ ] CSV/JSON 数据导出

### 🚧 v0.3 - Web 界面
- [ ] FastAPI 后端
- [ ] React 前端
- [ ] 实时图表
- [ ] 决策历史可视化

### 🌟 v1.0 - 多人游戏
- [ ] 用户账户系统
- [ ] 与真实玩家的混合模式
- [ ] 每 7 回合选择算法
- [ ] 排行榜和对比

## 🤝 贡献指南

欢迎参与贡献！以下是你可以做的事：

### 简单贡献
- 📝 编写新的决策场景
- 🐛 报告 bug
- 📚 改进文档
- 🌐 翻译（英文/其他语言）

### 中级贡献
- 🎨 改进可视化
- 🔢 新指标建议
- ⚙️ 性能优化
- 🧪 编写测试

### 高级贡献
- 🤖 新算法策略
- 🌐 Web 界面开发
- 📊 数据分析工具
- 🎮 游戏机制扩展

### 贡献流程

1. Fork 仓库
2. 创建特性分支 (`git checkout -b feature/amazing-feature`)
3. 提交更改 (`git commit -m 'Add some amazing feature'`)
4. 推送到分支 (`git push origin feature/amazing-feature`)
5. 开启 Pull Request

## 📄 许可证

本项目以 MIT 许可证开源。详见 [LICENSE](LICENSE) 文件。

## 🙏 灵感来源

- [Pol.is](https://pol.is) - 共识查找算法
- [Decidim](https://decidim.org) - 参与式民主平台
- [vTaiwan](https://info.vtaiwan.tw) - 数字治理实验
- Democracy 3 & 4 - 治理模拟游戏

## 📬 联系方式

- **GitHub Issues**：Bug 报告和功能请求
- **GitHub Discussions**：一般讨论和问题
- **Email**：[elrazi00@protonmail.com]

## 🌟 给我们一个星标！

如果你喜欢这个项目，别忘记在 GitHub 上给我们一个 ⭐！

---

**说明**：本项目正在积极开发中。关注路线图以了解稳定的 v1.0 版本发布。

---

# Spanish Version

# 🏛️ AlgoGov: Simulador de Gobernanza Algorítmica

**Una plataforma de juego de código abierto que simula la gobernanza algorítmica y la democracia digital**

## 🎯 Acerca del Proyecto

AlgoGov es una simulación interactiva diseñada para probar diferentes modelos de gobernanza en una colonia espacial de 1000 personas. El proyecto tiene como objetivo realizar investigación experimental sobre democracia digital, toma de decisiones algorítmica y gobernanza participativa.

### Características Principales

- 🧑‍🤝‍🧑 **Sociedad Dinámica de 1000 Personajes**: Cada individuo caracterizado por balance Ethos-Pathos-Logos
- 🏛️ **9 Módulos de Gobernanza**: Justicia, Seguridad, Salud, Educación, Economía, Asuntos Internos, Relaciones Exteriores, Medio Ambiente, Tecnología
- 🎮 **Experimento de 3 Fases**: Humano → Algoritmo → Gobernanza híbrida
- 📊 **Métricas en Tiempo Real**: Felicidad, economía, medio ambiente, crimen, desarrollo
- 🔬 **Metodología Científica**: Investigación repetible y basada en datos

## 🚀 Inicio Rápido

### Requisitos

- Python 3.9 o superior
- ¡Sin paquetes adicionales necesarios! (Solo librería estándar)

### Instalación

```bash
# Clonar el repositorio
git clone https://github.com/[your-username]/algogov-simulator.git
cd algogov-simulator

# Ejecutar directamente (entorno virtual opcional)
python main.py
```

### Tu Primer Juego

```bash
$ python main.py

============================================================
  ALGOGOV: Simulador de Gobernanza Algorítmica v0.1
============================================================

🏗️  Inicializando colonia...
✅ ¡Colonia Alpha lista! Población: 1000

📋 Base de datos de decisiones cargada: 100 decisiones

Presiona Enter para comenzar la simulación...
```

## 📁 Estructura del Proyecto

```
algogov-simulator/
│
├── main.py                    # Punto de entrada principal
├── requirements.txt           # Dependencias de Python (vacío por ahora)
├── README.md                  # Este archivo
│
├── src/
│   ├── core/                  # Clases centrales
│   │   ├── character.py       # Sistema de personajes
│   │   ├── colony.py          # Gestión de colonia
│   │   ├── module.py          # Módulos de gobernanza
│   │   └── decision_manager.py# Gestor de decisiones
│   │
│   ├── decisions/             # Base de datos de decisiones
│   │   └── decision_database.py # 100 decisiones (9 módulos × 7-10 decisiones)
│   │
│   ├── simulation/            # Motor de simulación
│   │   └── game_loop.py       # Bucle de juego
│   │
│   ├── algorithms/            # Algoritmos de gobernanza (Fase 2)
│   │   └── (por agregar)
│   │
│   └── utils/                 # Utilidades
│       └── display.py         # Visualización de consola
│
├── tests/                     # Pruebas unitarias
│   └── (por agregar)
│
├── data/                      # Resultados de simulación
│   └── (generado automáticamente)
│
└── docs/                      # Documentación
    ├── game_design.md         # Documento de diseño del juego
    ├── algorithm_specs.md     # Detalles de algoritmos
    └── research_questions.md  # Preguntas de investigación
```

## 🎮 ¿Cómo Jugar?

### Fase 1: Gobernanza Manual (Versión Actual)

¡Eres el administrador de la colonia! Cada turno tomarás decisiones para 9 módulos diferentes.

#### Proceso de Toma de Decisiones

1. **Se Presenta una Decisión**: Cada módulo presenta un problema con 2-4 opciones
2. **Examina las Opciones**: Cada opción muestra:
   - **Pesos Ethos/Pathos/Logos**: Características ideológicas
   - **Impacto**: Efectos en dinero, energía, medio ambiente, tasa de crimen
   - **Tasa de Apoyo**: Qué porcentaje de la población apoyaría esto
3. **Elige tu Opción**: Escribe el número y presiona Enter
4. **Observa Resultados**: Ve cómo tu decisión afecta tu colonia

#### Ejemplo de Decisión

```
────────────────────────────────────────────────────────────
🏛️  MÓDULO: Salud
📋 DECISIÓN: Estructura del Sistema de Salud
❓ ¿Cómo deben organizarse los servicios de salud de la colonia?

1. Atención Médica Universal Gratuita: Cobertura completa para todos
   💭 Ethos: 0.4 | Pathos: 0.9 | Logos: 0.5
   📊 Impacto: dinero -1200, energía 100
   👥 Apoyo Estimado: 67.3%

2. Sistema Mixto Público-Privado: Servicios básicos gratuitos
   💭 Ethos: 0.5 | Pathos: 0.5 | Logos: 0.7
   📊 Impacto: dinero -600, energía 60, crimen 0.01
   👥 Apoyo Estimado: 58.2%

3. Basado en Seguros: Cada uno compra su propio seguro
   💭 Ethos: 0.7 | Pathos: 0.2 | Logos: 0.8
   📊 Impacto: dinero -200, energía 30, crimen 0.02
   👥 Apoyo Estimado: 42.1%

Tu elección (1-3):
```

### Métricas

Tus decisiones afectan 5 métricas principales:

- 😊 **Felicidad** (0-100%): Estado de ánimo general de la población
- 💰 **Dinero**: Presupuesto de la colonia (inicio: 10,000)
- 📈 **Desarrollo**: Calidad ambiental × Consumo de energía
- 🌱 **Medio Ambiente** (0-100%): Sostenibilidad ambiental
- 🚨 **Tasa de Crimen** (0-100%): Cuanto más bajo, mejor

## 🧠 Sistema Ethos-Pathos-Logos

Cada personaje y opción de decisión se pondera en tres dimensiones ideológicas:

### Ethos (Moralidad/Autoridad)
- Valores tradicionales
- Jerarquía y autoridad
- Orden social

### Pathos (Emoción/Empatía)
- Conexión emocional
- Justicia social
- Bienestar comunitario

### Logos (Lógica/Razón)
- Análisis racional
- Eficiencia
- Soluciones pragmáticas

**Cálculo de Apoyo**: La probabilidad de que un personaje apoye una decisión depende de la similitud entre los pesos del personaje y la decisión (similitud del coseno).

## 🔬 Objetivos de Investigación

Esta simulación tiene como objetivo responder estas preguntas:

1. **Modelos de Gobernanza**: ¿Cuál estrategia de decisión (humana, algoritmo, híbrida) es más exitosa?
2. **Preferencias Sociales**: ¿Cómo producen resultados diferentes diferentes composiciones de personajes?
3. **Corto vs Largo Plazo**: ¿Son las decisiones populistas o la planificación a largo plazo más efectivas?
4. **Legitimidad Democrática**: ¿La alta aprobación siempre es la mejor decisión?
5. **Optimización Multidimensional**: ¿Es posible equilibrar todas las métricas?

## 🗺️ Hoja de Ruta

### ✅ v0.1 - MVP Inicial (Próximamente)
- [x] Simulación básica de colonia
- [x] 9 módulos × 7 decisiones = Base de datos de 100 decisiones
- [x] Interfaz manual de toma de decisiones
- [x] Seguimiento de 5 métricas principales
- [x] Visualización basada en consola

### 🔄 v0.2 - Competencia de Algoritmos
- [ ] 7 implementaciones de algoritmos diferentes
- [ ] Modo de simulación automática
- [ ] Comparación de desempeño de algoritmos
- [ ] Exportación de datos CSV/JSON

### 🚧 v0.3 - Interfaz Web
- [ ] Backend con FastAPI
- [ ] Frontend con React
- [ ] Gráficos en tiempo real
- [ ] Visualización del historial de decisiones

### 🌟 v1.0 - Multijugador
- [ ] Sistema de cuenta de usuario
- [ ] Modo híbrido con jugadores reales
- [ ] Selección de algoritmo cada 7 turnos
- [ ] Tabla de clasificación y comparaciones

## 🤝 Contribuciones

¡Bienvenidas tus contribuciones! Aquí hay cosas que puedes hacer:

### Contribuciones Fáciles
- 📝 Escribir nuevos escenarios de decisión
- 🐛 Reportar errores
- 📚 Mejorar documentación
- 🌐 Traducciones (inglés/otros idiomas)

### Nivel intermedio
- 🎨 Mejoras en la visualización
- 🔢 Nuevas sugerencias de métricas
- ⚙️ Optimizaciones de rendimiento
- 🧪 Redacción de pruebas

### Nivel avanzado
- 🤖 Nuevas estrategias algorítmicas
- 🌐 Desarrollo de la interfaz web
- 📊 Herramientas de análisis de datos
- 🎮 Extensiones de la mecánica del juego

### Proceso de contribución

1. Bifurca el repositorio
2. Crea una rama de características (`git checkout -b feature/amazing-feature`)
3. Confirma los cambios (`git commit -m “Añadir alguna característica increíble”`)
4. Envía a la rama (`git push origin feature/amazing-feature`)
5. Abre una solicitud de extracción

## 📄 Licencia

Este proyecto es de código abierto bajo la licencia MIT. Consulta el archivo [LICENCIA](LICENCIA) para obtener más detalles.

## 🙏 Inspiraciones

- [Pol.is](https://pol.is) - Algoritmo para alcanzar el consenso
- [Decidim](https://decidim.org) - Plataforma de democracia participativa
- [vTaiwan](https://info.vtaiwan.tw) - Experimento de gobernanza digital
- Democracy 3 y 4 - Juegos de simulación de gobernanza

## 📬 Contacto

- **GitHub Issues**: informes de errores y solicitudes de funciones
- **GitHub Discussions**: debates generales y preguntas
- **Correo electrónico**: [elrazi00@protonmail.com]
**Algoritmik yönetişim ve dijital demokrasiyi simüle eden açık kaynak oyun platformu**



