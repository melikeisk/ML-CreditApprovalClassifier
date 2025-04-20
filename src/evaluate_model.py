import pandas as pd
import numpy as np
import os
import joblib # Modeli yüklemek için
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix # Başarı metrikleri için
import matplotlib.pyplot as plt 
import seaborn as sns 

# 📂 Gerekli klasörleri oluştur
os.makedirs("outputs/models", exist_ok=True)

# 🧪 Test verisini yükle
X_test = pd.read_csv("data/processed/X_test.csv")
y_test = pd.read_csv("data/processed/y_test.csv")

# 🧠 Eğitilmiş modeli yükle
model = joblib.load("models/trained_model.pkl")

# 🔮 Tahmin
y_pred = model.predict(X_test)

# 📊 Başarı metrikleri
acc = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)
cm = confusion_matrix(y_test, y_pred)

# 📄 Metrikleri txt olarak kaydet
with open("outputs/models/evaluation_metrics.txt", "w") as f:
    f.write(f"Accuracy: {acc:.4f}\n\n")
    f.write("Classification Report:\n")
    f.write(report)

# 🔁 Confusion Matrix
plt.figure(figsize=(6, 5))
sns.heatmap(cm, annot=True, fmt="d", cmap="Purples")
plt.xlabel("Tahmin")
plt.ylabel("Gerçek")
plt.title("Confusion Matrix (Test Seti)")
plt.savefig("outputs/models/confusion_matrix_test.png")
plt.close()

# 📈 Gerçek vs Tahmin Histogramı
plt.figure(figsize=(6, 4))
sns.histplot(y_test, label="Gerçek", color="blue", alpha=0.6, bins=2)
sns.histplot(y_pred, label="Tahmin", color="orange", alpha=0.6, bins=2)
plt.legend()
plt.title("Gerçek vs Tahmin (Test Verisi)")
plt.xlabel("Kredi Onayı (0=Red, 1=Onay)")
plt.ylabel("Kayıt Sayısı")
plt.savefig("outputs/models/pred_vs_true_test.png")
plt.close()

print("📈 Test verisi üzerinde model başarıyla değerlendirildi.")
