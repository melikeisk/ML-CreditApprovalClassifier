import pandas as pd
import matplotlib.pyplot as plt # Veri görselleştirme için
import seaborn as sns # İstatistiksel veri görselleştirme için
import os

# 📁 Klasör oluştur
os.makedirs("outputs/eda", exist_ok=True)

# 📄 Veriyi oku
df = pd.read_csv("data/raw/kredi_verisi.csv")

# 🧠 Veri bilgisi
print("🔍 Veri Şekli:", df.shape)
print("\n📌 Veri Tipleri ve Eksik Değer Durumu:")
print(df.info())
print("\n🧮 Tanımlayıcı İstatistikler:\n", df.describe())
print("\n🚨 Eksik Değer Sayısı:\n", df.isnull().sum())

# 📊 Sınıf dağılımı
plt.figure(figsize=(6, 4))
sns.countplot(x='approved', data=df, palette="Set2")
plt.title("Kredi Onayı Dağılımı")
plt.xlabel("Onay Durumu (0 = Reddedildi, 1 = Onaylandı)")
plt.ylabel("Kayıt Sayısı")
plt.tight_layout()
plt.savefig("outputs/eda/class_distribution.png")
plt.close()

# 📈 Sayısal değişken histogramları 
numeric_cols = ['age', 'income', 'debt', 'credit_score', 'employment_years']
for col in numeric_cols:
    plt.figure(figsize=(6, 4))
    sns.histplot(df[col], bins=30, kde=True, color='skyblue', edgecolor='black')
    plt.title(f"{col.capitalize()} Dağılımı")
    plt.xlabel(col)
    plt.ylabel("Frekans")
    plt.tight_layout()
    plt.savefig(f"outputs/eda/hist_{col}.png")
    plt.close()

# 🔗 Korelasyon matrisi
plt.figure(figsize=(10, 8))
sns.heatmap(df.corr(), annot=True, cmap="coolwarm", fmt=".2f")
plt.title("📊 Korelasyon Matrisi")
plt.tight_layout()
plt.savefig("outputs/eda/correlation_matrix.png")
plt.close()

# 🪟 Onay durumuna göre boxplotlar
for col in ['income', 'debt', 'credit_score']:
    plt.figure(figsize=(6, 4))
    sns.boxplot(x='approved', y=col, data=df, palette="Set3")
    plt.title(f"{col.capitalize()} Dağılımı (Onay Durumuna Göre)")
    plt.tight_layout()
    plt.savefig(f"outputs/eda/boxplot_{col}_by_approval.png")
    plt.close()

# Pairplot çok yavaş çalışabileceği için yoruma alındı, ihtiyaç olursa aktif edilebilir.
# sns.pairplot(df, hue="approved", vars=numeric_cols, palette="husl")
# plt.savefig("outputs/eda/pairplot_by_approval.png")
# plt.close()

print("✅ EDA tamamlandı, tüm görseller outputs/eda/ klasörüne kaydedildi.")
