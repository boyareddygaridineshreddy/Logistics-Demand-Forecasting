
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

# Create output folder
OUTPUT_DIR = Path("week3_outputs")
OUTPUT_DIR.mkdir(exist_ok=True)

# 1. Create hypothetical logistics dataset
np.random.seed(42)

n = 100

df = pd.DataFrame({
    "Shipment_ID": range(101, 101 + n),
    "Delivery_Days": np.random.randint(1, 11, n),
    "Shipment_Volume": np.random.randint(10, 200, n),
    "Distance_KM": np.random.randint(50, 1000, n),
    "Transport_Mode": np.random.choice(
        ["Road", "Air", "Sea"], n
    )
})

# Calculate hypothetical transportation costs
mode_cost = {"Road": 5, "Air": 12, "Sea": 3}

df["Transport_Cost"] = (
    df["Distance_KM"] * df["Transport_Mode"].map(mode_cost)
    + df["Shipment_Volume"] * 2
)

# Create delivery status
df["Delivery_Status"] = np.where(
    df["Delivery_Days"] > 7,
    "Delayed",
    "Delivered"
)

# Save dataset
df.to_csv(OUTPUT_DIR / "logistics_dataset.csv", index=False)

# 2. Basic Exploratory Data Analysis
print("DATASET INFORMATION")
print(df.info())

print("\nSTATISTICAL SUMMARY")
print(df.describe())

print("\nAVERAGE DELIVERY TIME")
print(df["Delivery_Days"].mean())

print("\nMEDIAN DELIVERY TIME")
print(df["Delivery_Days"].median())

print("\nMOST COMMON TRANSPORT MODE")
print(df["Transport_Mode"].mode()[0])

print("\nDELIVERY STATUS")
print(df["Delivery_Status"].value_counts())

print("\nCORRELATION")
print(df[
    ["Delivery_Days", "Shipment_Volume",
     "Distance_KM", "Transport_Cost"]
].corr())

# 3. Histogram - Delivery Time Distribution
plt.figure(figsize=(8, 5))
plt.hist(df["Delivery_Days"], bins=10, edgecolor="black")
plt.title("Delivery Time Distribution")
plt.xlabel("Delivery Days")
plt.ylabel("Number of Shipments")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "delivery_time_histogram.png")
plt.close()

# 4. Bar Chart - Shipment Volume by Transport Mode
volume = df.groupby("Transport_Mode")["Shipment_Volume"].sum()

plt.figure(figsize=(8, 5))
volume.plot(kind="bar")
plt.title("Shipment Volume by Transport Mode")
plt.xlabel("Transport Mode")
plt.ylabel("Total Shipment Volume")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "shipment_volume_bar_chart.png")
plt.close()

# 5. Box Plot - Transportation Cost
plt.figure(figsize=(8, 5))
sns.boxplot(x=df["Transport_Cost"])
plt.title("Transportation Cost Distribution")
plt.xlabel("Transportation Cost")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "transport_cost_boxplot.png")
plt.close()

# 6. Scatter Plot - Distance vs Transportation Cost
plt.figure(figsize=(8, 5))
sns.scatterplot(
    data=df,
    x="Distance_KM",
    y="Transport_Cost",
    hue="Transport_Mode"
)
plt.title("Distance vs Transportation Cost")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "distance_cost_scatterplot.png")
plt.close()

# 7. Correlation Heatmap
plt.figure(figsize=(8, 5))
sns.heatmap(
    df[
        ["Delivery_Days", "Shipment_Volume",
         "Distance_KM", "Transport_Cost"]
    ].corr(),
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)
plt.title("Logistics Data Correlation Heatmap")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "correlation_heatmap.png")
plt.close()

print("\nAll five visualizations have been generated!")
print("Check the week3_outputs folder.")

print("\nWeek 3 Logistics Analysis Completed!")
