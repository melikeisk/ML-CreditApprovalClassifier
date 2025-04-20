import pandas as pd
import os
from sklearn.model_selection import train_test_split # Eğitim ve test verilerini ayırmak için
from sklearn.ensemble import RandomForestClassifier # Model oluşturmak için
import joblib

# 📂 Klasörleri oluştur
os.makedirs("models", exist_ok=True)

# 📄 Veriyi oku
df = pd.read_csv("data/raw/kredi_verisi.csv")

# 🎯 Özellikleri ve hedef değişkeni ayır
X = df.drop("approved", axis=1)
y = df["approved"]

# 🔀 Veriyi eğitim ve test olarak ayır 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 💾 Test verisini kaydet 
os.makedirs("data/processed", exist_ok=True)
X_test.to_csv("data/processed/X_test.csv", index=False)
y_test.to_csv("data/processed/y_test.csv", index=False)

# 🌲 Modeli oluştur ve eğit
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# 💾 Eğitilmiş modeli kaydet
joblib.dump(model, "models/trained_model.pkl")

print("✅ Model eğitildi ve 'models/trained_model.pkl' olarak kaydedildi.")
