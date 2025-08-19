# Walmart-Sales-Analysis-and-Prediction
This project predicts weekly sales for Walmart stores using machine learning (XGBoost) and provides business insights. It also includes an optional Streamlit dashboard for interactive visualization.

## Project Structure

```
Walmart_Sales_Analysis/
│
├── data/
│   ├── train.csv         # Training dataset
│   └── test.csv          # Test dataset
│
├── notebooks/
│   └── Walmart Sales Analysis.ipynb   # Jupyter notebook with preprocessing, training, prediction, insights
│
├── app.py               # Streamlit dashboard (optional)
│
├── requirements.txt     # Python dependencies
│
└── README.md            # Project description & instructions
```

## Features

* Preprocess and clean data
* Train XGBoost model for weekly sales prediction
* Handle missing columns in test data
* Predict weekly sales for test data
* Extract business insights by month, store, and department
* (Optional) Interactive Streamlit dashboard

## Business Insights

* December has peak sales → suggest seasonal promotions.
* Central region stores may need strategic improvements.
* Office Supplies category has steady profit → safe investment.

*(More insights can be extracted from the notebook using the aggregation code provided.)*

## How to Run

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Run the Jupyter Notebook to see predictions and insights:

```bash
jupyter notebook notebooks/Walmart\ Sales\ Analysis.ipynb
```

3. (Optional) Run the Streamlit dashboard:

```bash
streamlit run app.py
```

## Dependencies

* pandas
* numpy
* scikit-learn
* xgboost
* matplotlib
* seaborn
* streamlit

## Example Code Snippets

### Handle Missing Columns in Test Data

```python
for col in X.columns:
    if col not in test_data.columns:
        if X[col].dtype in ['int64', 'float64']:
            test_data[col] = X[col].mean()
        else:
            test_data[col] = X[col].mode()[0]
Final_test = test_data[X.columns]
```

### Predict Using XGBoost

```python
test_data['Predicted_Weekly_Sales'] = xgb_model.predict(Final_test)
test_data[['Store', 'Dept', 'Date', 'Predicted_Weekly_Sales']].head()
```

### Business Insight Aggregation

```python
monthly_sales = test_data.groupby('Month')['Predicted_Weekly_Sales'].sum().sort_values(ascending=False)
store_sales = test_data.groupby('Store')['Predicted_Weekly_Sales'].sum().sort_values(ascending=False)
dept_sales = test_data.groupby('Dept')['Predicted_Weekly_Sales'].sum().sort_values(ascending=False)
```
