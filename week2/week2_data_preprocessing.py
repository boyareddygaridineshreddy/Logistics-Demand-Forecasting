
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

# 1. Create sample logistics data
data = {
    "shipment_id": [101, 102, 103, 104, 105, 106, 107, 108],
    "weight_kg": [500, 700, 600, 800, np.nan, 900, 700, 500],
    "shipping_cost": [2000, 2500, 2200, 3000, 2800, 3500, 2500, 2000],
    "transport_mode": [
        "Road", "Air", "Sea", "Road",
        "Air", "Sea", "Road", "Road"
    ],
    "delivery_status": [
        "Delivered", "Delivered", "Pending", "Delivered",
        "Pending", "Delivered", "Delivered", "Delivered"
    ]
}

df = pd.DataFrame(data)

print("Original Dataset:")
print(df)

# 2. Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# 3. Handle missing numerical values
df["weight_kg"] = df["weight_kg"].fillna(
    df["weight_kg"].median()
)

# 4. Remove duplicate records
df = df.drop_duplicates()

# 5. Correct data types
df["shipment_id"] = df["shipment_id"].astype(int)
df["weight_kg"] = pd.to_numeric(df["weight_kg"])
df["shipping_cost"] = pd.to_numeric(df["shipping_cost"])

# 6. Standardize text categories
df["transport_mode"] = (
    df["transport_mode"].str.strip().str.title()
)

df["delivery_status"] = (
    df["delivery_status"].str.strip().str.title()
)

# 7. Detect outliers using IQR
Q1 = df["shipping_cost"].quantile(0.25)
Q3 = df["shipping_cost"].quantile(0.75)

IQR = Q3 - Q1

lower_limit = Q1 - 1.5 * IQR
upper_limit = Q3 + 1.5 * IQR

outliers = df[
    (df["shipping_cost"] < lower_limit) |
    (df["shipping_cost"] > upper_limit)
]

print("\nDetected Outliers:")
print(outliers)

# 8. Normalize numerical columns
scaler = MinMaxScaler()

df[["weight_kg", "shipping_cost"]] = scaler.fit_transform(
    df[["weight_kg", "shipping_cost"]]
)

# 9. Display cleaned dataset
print("\nCleaned and Preprocessed Dataset:")
print(df)

# 10. Save processed data
df.to_csv("week2_cleaned_logistics_data.csv", index=False)

print("\nWeek 2 Data Preprocessing Completed!")
print("Cleaned dataset saved successfully.")
