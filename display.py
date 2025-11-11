from typing import Dict, List, Optional
from ..core.colony import Colony
import sys
import os

# Config'i import et
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from config import (
    DisplayConfig,
    MetricLimits,
    SuccessThresholds,
    get_grade
)


class Display:
    """Görüntüleme yardımcı fonksiyonları - v2.0"""
    
    @staticmethod
    def show_colony_status(colony: Colony, show_modules: bool = True):
        """Koloninin mevcut durumunu göster"""
        print("\n" + "=" * 70)
        print(f"  {colony.name.upper()} - DURUM RAPORU")
        print("=" * 70)
        
        status = colony.get_status_summary()
        
        # Genel Metrikler
        print(f"\n📊 GENEL METRİKLER (Tur {status['turn']})")
        print(f"  👥 Nüfus: {status['population']}")
        
        # Mutluluk
        happiness_bar = Display._format_bar(status['happiness'], '█')
        happiness_warning = Display._get_warning_icon('happiness', status['happiness'])
        print(f"  😊 Mutluluk: {happiness_bar} {status['happiness']*100:.1f}% {happiness_warning}")
        
        # Para
        money_warning = Display._get_warning_icon('money', status['money'])
        print(f"  💰 Para: ${status['money']:.0f} {money_warning}")
        
        # Gelişme
        print(f"  📈 Gelişme: {status['development']:.1f}")
        
        # Çevre
        env_bar = Display._format_bar(status['environment'], '█')
        env_warning = Display._get_warning_icon('environment', status['environment'])
        print(f"  🌱 Çevre: {env_bar} {status['environment']*100:.1f}% {env_warning}")
        
        # Suç
        crime_warning = Display._get_warning_icon('crime', status['crime_rate'])
        print(f"  🚨 Suç Oranı: {status['crime_rate']*100:.1f}% {crime_warning}")
        
        # Koloni Kişiliği
        print(f"\n🧠 KOLONİ KİŞİLİĞİ (Ortalama)")
        print(f"  Ethos (Ahlak/Otorite): {status['avg_ethos']*100:.1f}%")
        print(f"  Pathos (Duygu/Empati): {status['avg_pathos']*100:.1f}%")
        print(f"  Logos (Mantık/Akıl): {status['avg_logos']*100:.1f}%")
        
        # Modül Performansları
        if show_modules:
            print("\n🏛️  MODÜL PERFORMANSLARI")
            for module_name, module in colony.modules.items():
                perf_bar = Display._format_bar(module.performance, '▓')
                perf_color = Display._get_performance_icon(module.performance)
                # Emoji'yi kaldır, sadece ismi göster
                clean_name = module_name.split(' ', 1)[-1] if ' ' in module_name else module_name
                print(f"  {module_name[:2]} {clean_name:12s}: {perf_bar} {module.performance*100:.0f}% {perf_color}")
        
        # Kritik Durum Uyarısı
        Display._show_critical_warnings(colony)
        
        print("=" * 70)
    
    @staticmethod
    def show_turn_summary(colony: Colony, turn_number: int):
        """Tur sonu özeti göster"""
        print("\n" + "─" * 70)
        print(f"  📋 TUR {turn_number} ÖZETİ")
        print("─" * 70)
        
        status = colony.get_status_summary()
        
        # Değişim göstergeleri
        if len(colony.history) >= 2:
            prev = colony.history[-2]
            curr = colony.history[-1]
            
            happiness_change = curr['happiness'] - prev['happiness']
            money_change = curr['money'] - prev['money']
            environment_change = curr['environment'] - prev['environment']
            development_change = curr['development'] - prev['development']
            
            print(f"\n📈 DEĞİŞİMLER (Önceki Tura Göre)")
            print(f"  😊 Mutluluk: {Display._format_change(happiness_change, percentage=True)}")
            print(f"  💰 Para: {Display._format_change(money_change, prefix='$')}")
            print(f"  🌱 Çevre: {Display._format_change(environment_change, percentage=True)}")
            print(f"  📈 Gelişme: {Display._format_change(development_change)}")
        
        # Mevcut Durum
        print(f"\n💡 MEVCUT DURUM")
        print(f"  😊 Mutluluk: {status['happiness']*100:.1f}%")
        print(f"  💰 Para: ${status['money']:.0f}")
        print(f"  🌱 Çevre: {status['environment']*100:.1f}%")
        print(f"  📈 Gelişme: {status['development']:.1f}")
        
        # Mini performans özeti
        avg_perf = sum(m.performance for m in colony.modules.values()) / len(colony.modules)
        print(f"\n🏛️  Ortalama Modül Performansı: {avg_perf*100:.0f}%")
        
        print("─" * 70)
    
    @staticmethod
    def show_final_report(colony: Colony):
        """Oyun sonu nihai raporu göster"""
        print("\n📜 NİHAİ RAPOR")
        print("─" * 70)
        
        if not colony.history:
            print("  ⚠️  Kayıtlı veri bulunamadı.")
            return
        
        # Başlangıç ve bitiş değerleri
        start = colony.history[0]
        end = colony.history[-1]
        
        # Performans Özeti
        print(f"\n🎯 PERFORMANS (Tur 1 → Tur {end['turn']})")
        print(f"  😊 Mutluluk: {start['happiness']*100:.1f}% → {end['happiness']*100:.1f}% "
              f"({Display._format_change(end['happiness'] - start['happiness'], percentage=True)})")
        print(f"  💰 Para: ${start['money']:.0f} → ${end['money']:.0f} "
              f"({Display._format_change(end['money'] - start['money'], prefix='$')})")
        print(f"  🌱 Çevre: {start['environment']*100:.1f}% → {end['environment']*100:.1f}% "
              f"({Display._format_change(end['environment'] - start['environment'], percentage=True)})")
        print(f"  📈 Gelişme: {start['development']:.1f} → {end['development']:.1f} "
              f"({Display._format_change(end['development'] - start['development'])})")
        
        # Trend Analizi
        print(f"\n📊 TREND ANALİZİ")
        Display._show_trend(colony.history, 'happiness', '😊 Mutluluk')
        Display._show_trend(colony.history, 'money', '💰 Para')
        Display._show_trend(colony.history, 'environment', '🌱 Çevre')
        Display._show_trend(colony.history, 'development', '📈 Gelişme')
        
        # Başarı Değerlendirmesi
        print(f"\n⭐ GENEL DEĞERLENDİRME")
        score = Display._calculate_overall_score(colony)
        grade = get_grade(score)
        
        print(f"  Toplam Skor: {score:.1f}/100")
        print(f"  Not: {grade}")
        print(f"  {Display._get_grade_comment(grade)}")
        
        # Hedef Karşılaştırması
        Display._show_goal_comparison(colony)
        
        print("\n" + "=" * 70)
        print("  🎊 Simülasyon tamamlandı! Teşekkürler.")
        print("=" * 70)
    
    @staticmethod
    def _format_bar(value: float, char: str = '█', length: int = None) -> str:
        """İlerleme çubuğu oluştur"""
        if length is None:
            length = DisplayConfig.PROGRESS_BAR_LENGTH
        
        filled = int(value * length)
        empty = length - filled
        return f"[{char * filled}{'·' * empty}]"
    
    @staticmethod
    def _format_change(value: float, percentage: bool = False, prefix: str = '') -> str:
        """Değişimi formatla (artış/azalış göstergesiyle)"""
        if value > 0.001:  # Küçük değişimleri pozitif say
            symbol = "↑"
            color = "🟢"
        elif value < -0.001:
            symbol = "↓"
            color = "🔴"
        else:
            symbol = "→"
            color = "⚪"
        
        if percentage:
            return f"{color} {symbol} {abs(value)*100:.1f}%"
        else:
            return f"{color} {symbol} {prefix}{abs(value):.1f}"
    
    @staticmethod
    def _get_warning_icon(metric: str, value: float) -> str:
        """Metrik için uyarı ikonu döndür"""
        if metric == 'happiness':
            if value < MetricLimits.CRITICAL_HAPPINESS:
                return "⚠️ KRİTİK!"
            elif value < 0.4:
                return "⚠️"
        
        elif metric == 'money':
            if value < MetricLimits.CRITICAL_MONEY:
                return "⚠️ KRİTİK!"
            elif value < 2000:
                return "⚠️"
        
        elif metric == 'environment':
            if value < MetricLimits.CRITICAL_ENVIRONMENT:
                return "⚠️ KRİTİK!"
            elif value < 0.5:
                return "⚠️"
        
        elif metric == 'crime':
            if value > MetricLimits.CRITICAL_CRIME:
                return "⚠️ KRİTİK!"
            elif value > 0.5:
                return "⚠️"
        
        return ""
    
    @staticmethod
    def _get_performance_icon(performance: float) -> str:
        """Performans ikonu döndür"""
        if performance >= 0.8:
            return "🌟"
        elif performance >= 0.6:
            return "✅"
        elif performance >= 0.4:
            return "⚠️"
        else:
            return "🔴"
    
    @staticmethod
    def _show_critical_warnings(colony: Colony):
        """Kritik durum uyarılarını göster"""
        warnings = []
        
        if colony.metrics.happiness < MetricLimits.CRITICAL_HAPPINESS:
            warnings.append("😡 Mutluluk çok düşük - İsyan riski!")
        
        if colony.metrics.money < MetricLimits.CRITICAL_MONEY:
            warnings.append("💸 Bütçe tükendi - İflas riski!")
        
        if colony.metrics.environment < MetricLimits.CRITICAL_ENVIRONMENT:
            warnings.append("☠️ Çevre çok kirli - Sağlık krizi!")
        
        if colony.metrics.crime_rate > MetricLimits.CRITICAL_CRIME:
            warnings.append("🚨 Suç çok yüksek - Güvenlik krizi!")
        
        if warnings:
            print("\n⚠️  KRİTİK UYARILAR:")
            for warning in warnings:
                print(f"     {warning}")
    
    @staticmethod
    def _show_trend(history: List[Dict], metric: str, label: str):
        """Metrik trendini göster"""
        if len(history) < 2:
            return
        
        values = [h[metric] for h in history]
        avg = sum(values) / len(values)
        trend = values[-1] - values[0]
        
        if abs(trend) < 0.01 and metric in ['happiness', 'environment']:  # Küçük değişimler
            trend_text = "Sabit"
            trend_icon = "→"
        elif trend > 0:
            trend_text = "Artan"
            trend_icon = "📈"
        else:
            trend_text = "Azalan"
            trend_icon = "📉"
        
        print(f"  {label}: {trend_icon} {trend_text} (Ort: {avg:.2f})")
    
    @staticmethod
    def _calculate_overall_score(colony: Colony) -> float:
        """Genel başarı skorunu hesapla"""
        if not colony.history:
            return 0
        
        end = colony.history[-1]
        
        # Her metriği ağırlıklandır (SuccessThresholds'tan)
        happiness_score = end['happiness'] * SuccessThresholds.SCORING_WEIGHTS['happiness']
        
        # Para skoru (0-25 arası normalize et)
        money_ratio = min(end['money'] / 10000, 1.0)
        money_score = money_ratio * SuccessThresholds.SCORING_WEIGHTS['money']
        
        # Gelişme skoru (0-20 arası normalize et)
        dev_ratio = min(end['development'] / 500, 1.0)
        development_score = dev_ratio * SuccessThresholds.SCORING_WEIGHTS['development']
        
        # Çevre skoru
        environment_score = end['environment'] * SuccessThresholds.SCORING_WEIGHTS['environment']
        
        # Suç skoru (ters: düşük suç = yüksek puan)
        crime_score = (1 - end['crime_rate']) * SuccessThresholds.SCORING_WEIGHTS['crime']
        
        total = happiness_score + money_score + development_score + environment_score + crime_score
        return total
    
    @staticmethod
    def _get_grade_comment(grade: str) -> str:
        """Nota göre yorum"""
        comments = {
            "A+": "🌟 Olağanüstü! Koloniniz mükemmel yönetildi.",
            "A": "🎉 Harika! Çok başarılı bir yönetim sergiledıniz.",
            "A-": "👏 Mükemmel! Koloniniz gelişiyor.",
            "B+": "✨ Çok iyi! Başarılı kararlar aldınız.",
            "B": "👍 İyi! Dengeli bir yönetim.",
            "B-": "🙂 İyi, ama iyileştirme alanları var.",
            "C+": "😐 Orta düzey. Daha iyi olabilir.",
            "C": "😕 Vasat. Bazı kararlar sorunlu oldu.",
            "C-": "😟 Zayıf. Koloni zorlanıyor.",
            "D": "😰 Başarısız. Koloni ciddi sorunlarla karşı karşıya.",
            "F": "💀 Felaket. Koloni çöküşün eşiğinde."
        }
        return comments.get(grade, "")
    
    @staticmethod
    def _show_goal_comparison(colony: Colony):
        """Hedef karşılaştırmasını göster"""
        if not colony.history:
            return
        
        end = colony.history[-1]
        
        print(f"\n🎯 HEDEF KARŞILAŞTIRMASI")
        print("─" * 70)
        
        goals = [
            ("😊 Mutluluk", end['happiness'], SuccessThresholds.MIN_HAPPINESS, True),
            ("💰 Para", end['money'], SuccessThresholds.MIN_MONEY, True),
            ("🌱 Çevre", end['environment'], SuccessThresholds.MIN_ENVIRONMENT, True),
            ("🚨 Suç", end['crime_rate'], SuccessThresholds.MAX_CRIME, False),  # Ters
            ("📈 Gelişme", end['development'], SuccessThresholds.MIN_DEVELOPMENT, True)
        ]
        
        achieved = 0
        for label, actual, target, higher_is_better in goals:
            if higher_is_better:
                success = actual >= target
                comparison = f"{actual:.1f} / {target:.1f}"
            else:
                success = actual <= target
                comparison = f"{actual:.1f} / {target:.1f} (max)"
            
            icon = "✅" if success else "❌"
            achieved += 1 if success else 0
            
            print(f"  {icon} {label}: {comparison}")
        
        print(f"\n  Başarılan Hedef: {achieved}/5")
        print("─" * 70)
