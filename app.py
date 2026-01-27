import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load sensor data
df = pd.read_csv("iot_data.csv")
from sklearn.ensemble import IsolationForest

# Run anomaly detection
model = IsolationForest(contamination=0.1, random_state=42)
df["Anomaly"] = model.fit_predict(df[["Temperature", "Humidity"]])

st.title("IoT Data Simulation + AI Analysis")

# Show raw data
st.subheader("Sensor Data")
st.write(df.head(20))

# Line chart
st.subheader("Temperature & Humidity Over Time")
st.line_chart(df[["Temperature", "Humidity"]])

# Anomaly detection results
st.subheader("Anomaly Detection")
st.write("Number of anomalies detected:", list(df["Anomaly"]).count(-1))

# Highlight anomalies in red
fig, ax = plt.subplots()
normal = df[df["Anomaly"] == 1]
anomaly = df[df["Anomaly"] == -1]

ax.scatter(normal["Time"], normal["Temperature"], c="blue", label="Normal")
ax.scatter(anomaly["Time"], anomaly["Temperature"], c="red", label="Anomaly")
ax.set_xlabel("Time")
ax.set_ylabel("Temperature")
ax.legend()

st.pyplot(fig)

