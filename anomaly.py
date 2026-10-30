import pandas as pd
from sklearn.ensemble import IsolationForest

# Load the sensor data
df = pd.read_csv("iot_data.csv")

# Train anomaly detection model
model = IsolationForest(contamination=0.1, random_state=42)  # 10% anomalies
pred = model.fit_predict(df[["Temperature", "Humidity"]])

# Add results to DataFrame
df["Anomaly"] = pred

# Show first 10 rows
print(df.head(10))

# Count anomalies
print("Number of anomalies detected:", list(df["Anomaly"]).count(-1))
# Save results to a new CSV file
df.to_csv("anomaly_results.csv", index=False)

print("Results saved to anomaly_results.csv")
