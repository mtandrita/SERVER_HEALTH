import pandas as pd

file_path = "../data/system_metrics.csv"

df = pd.read_csv(file_path)

df["timestamp"] = pd.to_datetime(df["timestamp"])

print(df.head())

import matplotlib.pyplot as plt
df.loc[20:25, "cpu_percent"] = 95
df.loc[50:55, "ram_percent"] = 90

plt.figure(figsize=(12,5))
plt.plot(df["timestamp"], df["cpu_percent"], label="CPU")
plt.plot(df["timestamp"], df["ram_percent"], label="RAM")
plt.legend()
plt.title("CPU & RAM Usage Over Time")
plt.xticks(rotation=45)
plt.tight_layout()


df["cpu_smooth"] = df["cpu_percent"].rolling(window=5).mean()

plt.figure(figsize=(12,5))
plt.plot(df["timestamp"], df["cpu_percent"], alpha=0.4, label="Original")
plt.plot(df["timestamp"], df["cpu_smooth"], label="Smoothed")
plt.legend()
plt.show()
