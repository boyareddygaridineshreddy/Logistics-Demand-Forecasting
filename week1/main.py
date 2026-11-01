from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

DATA_FILE = Path(__file__).parent / "sample_sales_data.csv"
OUTPUT_DIR = Path(__file__).parent / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)


def load_data():
    df = pd.read_csv(DATA_FILE)

    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    df["quantity_sold"] = pd.to_numeric(
        df["quantity_sold"], errors="coerce"
    )
    df["unit_price"] = pd.to_numeric(
        df["unit_price"], errors="coerce"
    )

    df = df.dropna()
    df = df.drop_duplicates()
    df = df[df["quantity_sold"] > 0]

    return df.sort_values("date")


def calculate_kpis(df):
    df["revenue"] = df["quantity_sold"] * df["unit_price"]

    kpis = df.groupby(
        ["product_id", "product_name"]
    ).agg(
        total_units_sold=("quantity_sold", "sum"),
        average_demand=("quantity_sold", "mean"),
        total_revenue=("revenue", "sum")
    ).reset_index()

    return kpis


def create_forecast(df):
    daily = df.groupby(
        ["product_id", "product_name", "date"]
    )["quantity_sold"].sum().reset_index()

    forecasts = []

    for (product_id, product_name), group in daily.groupby(
        ["product_id", "product_name"]
    ):
        forecast = group.tail(7)["quantity_sold"].mean()

        forecasts.append({
            "product_id": product_id,
            "product_name": product_name,
            "forecast_next_day": round(forecast, 2)
        })

    return pd.DataFrame(forecasts)


def create_chart(df):
    daily = df.groupby(
        ["date", "product_name"]
    )["quantity_sold"].sum().unstack(fill_value=0)

    daily.plot(figsize=(10, 5), marker="o")
    plt.title("Daily Product Demand")
    plt.xlabel("Date")
    plt.ylabel("Units Sold")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "daily_demand.png")
    plt.close()


def main():
    df = load_data()

    kpis = calculate_kpis(df)
    forecasts = create_forecast(df)

    kpis.to_csv(OUTPUT_DIR / "product_kpis.csv", index=False)
    forecasts.to_csv(OUTPUT_DIR / "demand_forecast.csv", index=False)

    create_chart(df)

    print("Logistics Demand Forecasting Completed!")
    print("\nProduct KPIs:")
    print(kpis)

    print("\nDemand Forecast:")
    print(forecasts)


if __name__ == "__main__":
    main()
