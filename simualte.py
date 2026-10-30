import random
import pandas as pd
random.seed(42)

# Create empty list to store data
data = []

# Generate 100 fake sensor readings
for i in range(100):
    temp = random.uniform(20, 40)       # temperature between 20-40
    humidity = random.uniform(30, 70)   # humidity between 30-70
    data.append([i, temp, humidity])

# Convert to DataFrame
df = pd.DataFrame(data, columns=["Time", "Temperature", "Humidity"])

# Save to CSV file
df.to_csv("iot_data.csv", index=False)

print(df.head())   # show first 5 rows
