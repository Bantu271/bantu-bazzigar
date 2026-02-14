import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
import joblib

# Sample dataset (replace with your dataset)
data = {
    "tenure": [1, 2, 5, 7, 10, 12, 15, 18, 20, 22],
    "monthly_charges": [20, 30, 40, 60, 70, 80, 90, 100, 110, 120],
    "churn": [0, 0, 0, 1, 0, 1, 1, 1, 0, 1]
}

df = pd.DataFrame(data)

X = df[["tenure", "monthly_charges"]]
y = df["churn"]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

model = LogisticRegression()
model.fit(X_scaled, y)

# Save model and scaler
joblib.dump(model, "model.pkl")
joblib.dump(scaler, "scaler.pkl")

print("Model saved successfully!")
