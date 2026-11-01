
import pandas as pd
import numpy as np
from pathlib import Path

from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Create output folder
OUTPUT_DIR = Path(__file__).parent / "week4_outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

# 1. Create hypothetical logistics dataset
np.random.seed(42)

n = 200

df = pd.DataFrame({
    "Shipment_ID": range(101, 101 + n),
    "Distance_KM": np.random.randint(50, 1000, n),
    "Shipment_Volume": np.random.randint(10, 200, n),
    "Transport_Mode": np.random.choice(
        ["Road", "Air", "Sea"], n
    )
})

# 2. Generate hypothetical delivery times
mode_days = {"Road": 2, "Air": 1, "Sea": 4}

df["Delivery_Days"] = (
    1
    + df["Distance_KM"] / 250
    + df["Shipment_Volume"] / 150
    + df["Transport_Mode"].map(mode_days)
    + np.random.normal(0, 0.8, n)
).clip(lower=1).round(2)

# 3. Generate transportation costs
mode_cost = {"Road": 5, "Air": 12, "Sea": 3}

df["Transport_Cost"] = (
    df["Distance_KM"] * df["Transport_Mode"].map(mode_cost)
    + df["Shipment_Volume"] * 2
)

# Save dataset
df.to_csv(OUTPUT_DIR / "week4_logistics_dataset.csv", index=False)

# 4. Prepare data for machine learning
X = df[
    ["Distance_KM", "Shipment_Volume",
     "Transport_Cost", "Transport_Mode"]
]

y = df["Delivery_Days"]

# Convert transport mode into numerical columns
X = pd.get_dummies(
    X, columns=["Transport_Mode"], dtype=int
)

# 5. Split dataset into training and testing
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=42
)

# 6. Create machine learning models
models = {
    "Linear Regression": LinearRegression(),
    "Random Forest": RandomForestRegressor(
        n_estimators=100,
        random_state=42
    )
}

results = []

# 7. Train and evaluate models
for name, model in models.items():

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    mae = mean_absolute_error(y_test, predictions)
    rmse = np.sqrt(mean_squared_error(y_test, predictions))
    r2 = r2_score(y_test, predictions)

    results.append({
        "Model": name,
        "MAE": round(mae, 3),
        "RMSE": round(rmse, 3),
        "R2_Score": round(r2, 3)
    })

    print("\nModel:", name)
    print("MAE:", round(mae, 3))
    print("RMSE:", round(rmse, 3))
    print("R2 Score:", round(r2, 3))

    # Five-fold cross-validation on training data
    cv_scores = cross_val_score(
        model, X_train, y_train,
        cv=5, scoring="neg_mean_absolute_error"
    )

    print("Average Cross-Validation MAE:",
          round(-cv_scores.mean(), 3))

# 8. Compare model performance
results_df = pd.DataFrame(results)

results_df.to_csv(
    OUTPUT_DIR / "model_performance_results.csv",
    index=False
)

print("\nMODEL COMPARISON")
print(results_df.to_string(index=False))

# 9. Select the model with the lowest MAE
best_model_name = results_df.loc[
    results_df["MAE"].idxmin(), "Model"
]

print("\nBest Model:", best_model_name)

# 10. Save actual and predicted delivery times
best_model = models[best_model_name]
best_predictions = best_model.predict(X_test)

prediction_results = pd.DataFrame({
    "Actual_Delivery_Days": y_test.values,
    "Predicted_Delivery_Days": best_predictions.round(2)
})

prediction_results.to_csv(
    OUTPUT_DIR / "delivery_predictions.csv",
    index=False
)

print("\nWeek 4 Predictive Modeling Completed!")
print("Check the week4_outputs folder.")
