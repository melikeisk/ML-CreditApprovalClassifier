# ML-CreditApprovalClassifier
GYK - Kredi başvurusu onayını tahmin eden bir makine öğrenmesi projesi

## 🎯 Projenin Amacı

Bu projenin temel amacı, kredi başvurularının onaylanıp onaylanmayacağını tahmin edebilen bir makine öğrenmesi modeli geliştirmektir. 

Gerçek veriler yerine, kurallı yapı ve rastgelelik içeren yapay veriler oluşturularak, modelin eğitim ve değerlendirme süreci gerçekleştirilmiştir.  
**RandomForestClassifier** kullanılarak sınıflandırma modeli eğitilmiş, sonuçlar detaylı analiz ve görsellerle desteklenmiştir.

## Veri Seti Özellikleri

Aşağıda, veri setinde kullanılan özellikler ve bunların açıklamaları yer almaktadır:

| Özellik Adı       | Açıklama                                         | Örnek Değerler  |
|-------------------|-------------------------------------------------|-----------------|
| `age`             | Müşterinin yaşı                                 | 18 - 65         |
| `income`          | Aylık geliri (₺)                                | 3000 - 30000    |
| `debt`            | Toplam kredi kartı / kredi borcu               | 0 - 50000       |
| `credit_score`    | Kredi puanı (0–1000 arası)                     | 300 - 900       |
| `employment_years`| İş yerinde çalışma süresi (yıl)                | 0 - 40          |
| `approved`        | Kredi onayı (1 = Onaylandı, 0 = Reddedildi)    | 0 veya 1        |

## Onay Kuralları

Kredi onayı şu kurallara göre hesaplanmaktadır:

- **Kredi onayı (approved = 1)** verilir, eğer:
    - `income > 8000`
    - `credit_score > 600`
    - `debt < 20000`
    - `employment_years > 2`
- Aksi takdirde **Reddedilir (approved = 0)**

Rastgelelik (noise) eklenerek bu kurala uymayan durumlar da yaratılmıştır.

## Kullanılan Yöntem

Bu projede **RandomForestClassifier** modeli kullanılmıştır. Modelin eğitimi ve başarı değerlendirmesi aşamalarında şu metrikler incelenmiştir:
- **Accuracy**: Modelin genel doğruluğu
- **Confusion Matrix**: Gerçek ve tahmin edilen değerlerin karşılaştırılması
- **Classification Report**: Precision, Recall, F1 Score gibi detaylı başarı metrikleri

## Proje İçeriği

- **Veri Üretimi**: Kredi başvuru verilerini rastgele üretmek ve kaydetmek için kullanılan script: `generate_data.py`
- **Veri Keşfi**: Veri setinin keşifsel analizi (EDA) ve görselleştirmeleri: `eda.py`
- **Model Eğitimi**: RandomForestClassifier modelinin eğitimi: `trained.py`
- **Model Değerlendirmesi**: Test verisi üzerinden modelin değerlendirilmesi: `evaluate.py`

## Gereksinimler

- Python 3.x
- Gerekli kütüphaneler:
    - `pandas`
    - `numpy`
    - `scikit-learn`
    - `matplotlib`
    - `seaborn`
    - `joblib`

## Çalıştırma Talimatları

1. Gerekli kütüphaneleri yükleyin:

    ```bash
    pip install -r requirements.txt
    ```

2. Veri setini oluşturun ve kaydedin:

    ```bash
    python generate_data.py
    ```

3. Keşifsel veri analizini (EDA) yapın:

    ```bash
    python eda.py
    ```

4. Modeli eğitin:

    ```bash
    python trained.py
    ```

5. Modeli değerlendirin:

    ```bash
    python evaluate.py
    ```

## Sonuçlar

Modelin doğruluğu, sınıf dağılımı, confusion matrix ve diğer başarı metrikleri `outputs/models/` klasörüne kaydedilmiştir. Ayrıca tahmin sonuçları görsel olarak da karşılaştırılmıştır.
# 📊 Kredi Başvuru Onayı Tahmini

Bu proje, yapay olarak üretilmiş banka başvuru verilerini kullanarak bir başvurunun kredi onayı alıp almayacağını tahmin eden bir makine öğrenmesi modelini içerir.  

Amaç, veri üretiminden model eğitimine kadar tüm süreci baştan sona gerçekleştirmek ve değerlendirilebilir çıktılar sunmaktır.

---

## 🚀 Proje Adımları

1. **Veri Üretimi:**  
   Kurallara dayalı ve %10 oranında gürültü (noise) içeren 2000 kayıtlık veri seti oluşturulur.

2. **Keşifsel Veri Analizi (EDA):**  
   Dağılımlar, korelasyonlar ve onay durumuna göre değişkenlerin görsel incelemesi yapılır.

3. **Model Eğitimi:**  
   Random Forest algoritmasıyla sınıflandırma modeli eğitilir ve başarı metrikleri hesaplanır.

4. **Model Değerlendirme:**  
   Confusion matrix, tahmin-gözlem karşılaştırmaları ve metrik raporları görselleştirilir.

---

## 🔧 Kullanılan Araçlar

- Python 🐍
- pandas, numpy  
- seaborn, matplotlib  
- scikit-learn  
- joblib  

---

## 📁 Çıktılar

Model çıktılarına `outputs/` klasöründen ulaşabilirsiniz:
- `eda/` klasörü: Veri analiz görselleri  
- `models/` klasörü: Confusion matrix, başarı metrikleri, tahmin karşılaştırmaları  
- `trained_model.pkl`: Eğitilmiş model dosyası  

---

## 📚 Dökümantasyon

Projenin yapısı ve çalışma mantığını daha iyi anlamak için aşağıdaki dokümanlara göz atabilirsiniz:

- [`📄 docs/proje_mimarisi.md`](docs/proje_mimarisi.md)  
  ➤ Projenin klasör yapısı, veri akışı, dosyaların görevleri ve genel işleyişi açıklanır.

- [`📄 docs/veri_olusturma.md`](docs/veri_olusturma.md)  
  ➤ Üretilen yapay verinin nasıl oluşturulduğu, kullanılan değişkenler, değer aralıkları ve etiketleme kuralları detaylandırılır.

- [`📄 docs/model_egitimi.md`](docs/model_egitimi.md)  
  ➤ Modelin eğitimi, test işlemi, kullanılan algoritma, başarı metrikleri ve değerlendirme sonuçları açıklanır.

---


