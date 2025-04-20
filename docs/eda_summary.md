# 🧪 Keşifsel Veri Analizi (EDA) Özeti

Veri üzerinde temel istatistikler ve ilişkiler analiz edilmiştir. EDA görselleri `outputs/eda/` klasöründe bulunur.

## 🔢 Sınıf Dağılımı:
- Onaylanan başvurular: %60
- Reddedilen başvurular: %40

## 📉 Sayısal Değişkenler:
- `income`, `debt`, `credit_score` ve `employment_years` değişkenleri normal dağılıma yakın.
- `debt` ve `credit_score` arasında negatif korelasyon gözlemlendi.

## 🔗 Korelasyonlar:
- Gelir ve kredi skoru pozitif ilişkili.
- Borç miktarı arttıkça kredi skoru düşme eğiliminde.
- Onay durumu ile en ilişkili değişkenler:
    - `credit_score`
    - `income`
    - `employment_years`

## 📦 Kutu Grafikleri:
- Onay alanlar genel olarak daha yüksek gelir, düşük borç ve daha yüksek kredi skoruna sahip.
