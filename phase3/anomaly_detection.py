import pandas as pd
import joblib

file_path = "../data/system_metrics.csv"
df = pd.read_csv(file_path)

df["timestamp"] = pd.to_datetime(df["timestamp"])

features = df[[
    "cpu_percent",
    "ram_percent",
    "bytes_sent",
    "bytes_received"
]]
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
scaled_features = scaler.fit_transform(features)
from sklearn.ensemble import IsolationForest

model = IsolationForest(
    n_estimators=100,
    contamination=0.05,  # assume 5% anomalies
    random_state=42
)

model.fit(scaled_features)
df["anomaly"] = model.predict(scaled_features)
print(df["anomaly"].value_counts())

import matplotlib.pyplot as plt

plt.figure(figsize=(12,5))

# Normal points
normal = df[df["anomaly"] == 1]
plt.plot(normal["timestamp"], normal["cpu_percent"], label="Normal")

# Anomaly points
anomaly = df[df["anomaly"] == -1]
plt.scatter(anomaly["timestamp"], anomaly["cpu_percent"],
            color="red", label="Anomaly")

plt.legend()
plt.xticks(rotation=45)
plt.title("CPU Usage with Anomalies")
plt.tight_layout()

joblib.dump(model, "isolation_forest_model.pkl")
joblib.dump(scaler, "scaler.pkl")
