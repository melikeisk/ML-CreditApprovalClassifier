"""
Veri Üretimi ve Kaydetme Modülü
Bu modül, kredi başvurusu verilerini üretir ve csv formatında kaydeder.
"""

import pandas as pd # Veri işleme ve analiz için
import numpy as np  # Sayısal hesaplamalar için
import os # Dosya ve dizin işlemleri için

# Bu fonksiyon, kredi başvurusunun onaylanıp onaylanmadığını belirler.
# Kredi başvurusunun onaylanması için gereken koşulları kontrol eder.
# Ayrıca, rastgele bir gürültü ekleyerek sonuçları etkileyebilir.
# Gürültü olasılığı %10 olarak varsayılan bir parametre ile ayarlanmıştır.
def determine_approval(income, credit_score, debt, employment_years, noise_prob=0.1): 
    rule = income > 8000 and credit_score > 600 and debt < 20000 and employment_years > 2
    noise = np.random.rand() < noise_prob
    return int(rule and not noise or (not rule and noise))

# Bu fonksiyon, kredi başvurusuna ait verileri üretir ve belirtilen bir dosya yoluna kaydeder.
# Veri üretimi için gerekli olan parametreler: n (veri sayısı) ve save_path (dosya yolu).
# Veri üretimi için rastgele sayılar kullanılır ve bu sayılar belirli kurallara göre işlenir.
# Üretilen veriler, bir pandas DataFrame nesnesine dönüştürülür ve belirtilen dosya yoluna CSV formatında kaydedilir.
def generate_data(n=2000, save_path="data/raw/kredi_verisi.csv"):
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    np.random.seed(42)

    ages = np.random.randint(18, 66, n)
    employment_years = np.array([np.random.randint(0, age - 17) for age in ages])
    income = np.clip([np.random.normal(loc=3000 + (age * 300), scale=2000) for age in ages], 3000, 30000)
    debt = np.clip([np.random.normal(loc=inc * 0.8, scale=5000) for inc in income], 0, 50000)
    credit_score = np.clip([
        np.random.normal(loc=600 + (inc / 10000) * 100 - (d / 20000) * 100, scale=50)
        for inc, d in zip(income, debt)
    ], 300, 900)

    approved = [
        determine_approval(income[i], credit_score[i], debt[i], employment_years[i])
        for i in range(n)
    ]

    df = pd.DataFrame({
        "age": ages,
        "income": np.round(income, 2),
        "debt": np.round(debt, 2),
        "credit_score": np.round(credit_score, 0),
        "employment_years": employment_years,
        "approved": approved
    })

    df.to_csv(save_path, index=False)
    print(f"✅ Veri başarıyla oluşturuldu ve kaydedildi: {save_path}")

if __name__ == "__main__":
    generate_data() # Örnek veri üretimi ve kaydetme işlemi