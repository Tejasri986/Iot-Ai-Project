import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file you created earlier
df = pd.read_csv("iot_data.csv")

# Plot Temperature and Humidity over Time
plt.figure(figsize=(10,5))
plt.plot(df["Time"], df["Temperature"], label="Temperature", color="red")
plt.plot(df["Time"], df["Humidity"], label="Humidity", color="blue")

# Add labels and title
plt.xlabel("Time")
plt.ylabel("Sensor Reading")
plt.title("IoT Sensor Data Simulation")
plt.legend()

# Show the graph
plt.show()
