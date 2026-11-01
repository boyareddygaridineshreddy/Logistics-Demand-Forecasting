# Logistics-Demand-Forecasting
Data Science project for inventory demand forecasting and logistics optimization using Python.
# Logistics Demand Forecasting

## Project Overview
This project demonstrates a simple logistics demand forecasting system. It analyzes product sales data, calculates important KPIs, and predicts the next day's demand using a 7-day moving average.

## Objectives
- Analyze product sales data.
- Calculate product-level KPIs.
- Understand daily demand patterns.
- Generate basic demand forecasts.
- Support better inventory planning.

## Technologies Used
- Python
- Pandas
- Matplotlib
- CSV Dataset

## Project Files
- main.py – Main Python application.
- sample_sales_data.csv – Illustrative sample sales dataset.
- requirements.txt – Required Python libraries.

## KPIs
- Total Units Sold
- Average Demand
- Total Sales Revenue

## How to Run

1. Install Python.
2. Install the required libraries:

   pip install -r requirements.txt

3. Run the application:

   python main.py

## Output
The project generates:
- Product KPI report.
- Next-day demand forecast.
- Daily demand visualization.

Generated files are saved in the outputs folder.

## Dataset Note
The included dataset is synthetic sample data created for demonstration purposes. It does not represent actual company or customer information.

## Future Improvements
- Use real logistics datasets.
- Implement machine learning forecasting models.
- Add inventory optimization.
- Develop an interactive dashboard.

## Conclusion
This project demonstrates how data analysis and demand forecasting can support inventory planning and logistics decision-making.


## Week 2: Data Collection, Cleaning, and Preprocessing

### Objective
To prepare logistics data for analysis by identifying and handling data quality issues.

### Tasks Completed
- Created a sample logistics dataset.
- Identified missing values.
- Handled missing numerical values using median imputation.
- Removed duplicate records.
- Corrected data types.
- Standardized categorical values.
- Detected outliers using the IQR method.
- Applied Min-Max normalization.

### Tools Used
- Python
- Pandas
- NumPy
- Scikit-learn

### Output
Generated a cleaned logistics dataset named `week2_cleaned_logistics_data.csv`.

### Project File
`week2_data_preprocessing.py`

Note: The project uses simulated sample data for demonstration.
