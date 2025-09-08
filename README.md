# Walmart-Sales-Analysis-and-Prediction
This project focuses on forecasting weekly sales for Walmart stores using XGBoost, a powerful gradient boosting algorithm.
The aim is to help Walmart improve inventory management, staffing, and promotions planning by predicting future sales.

We used historical sales data, holiday information, and economic indicators to build and evaluate the model.

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
## Dataset

The dataset includes Walmart’s weekly sales data along with external features.

**Key Columns:**

* Store → Store ID

* Dept → Department ID

* Date → Week of sales

* Weekly_Sales → Actual sales (target variable)

* IsHoliday → Whether the week includes a holiday

* Temperature, Fuel_Price, CPI, Unemployment → External economic factors

* MarkDown1–5 → Promotional markdown data

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

## ⚙️ Methodology

### 1.Data Preprocessing

* Handled missing values in markdowns.

* Converted IsHoliday to Boolean.

* Extracted Year, Month, and Week from Date.

### 2.Modeling with XGBoost

* Tuned hyperparameters (n_estimators=500, max_depth=6, learning_rate=0.1).

* Trained model on historical sales data.

### 3.Evaluation

* RMSE: 72.06

* R² Score: 0.9481

* Normalized RMSE: 0.0045 (Excellent accuracy ✅)

## 📈 Results

### Sample predictions (walmart_predictions.csv):
```
Store	Dept    Date	    IsHoliday	Predicted_Weekly_Sales
1	    1	    2012-11-02	False	    15025.16
1	    1	    2012-11-09	False	    8027.39
1	    1	    2012-11-16	False	    7028.98
1	    1	    2012-11-23	True	    6591.77
```
## Conclusion

* ✅ XGBoost delivered highly accurate predictions for Walmart sales.
* ✅ Normalized RMSE of 0.0045 shows the model generalizes well.
* ✅ The Streamlit app makes results interactive and business-friendly.

## 👨‍💻 Author

* V Om Keshava Reddy
* 📌 B.Tech CSE (AI & ML), SRM University
* 🔗 [LinkedIn](https://www.linkedin.com/in/v-om-keshava-reddy-792478349/)| [GitHub](https://github.com/keshavreddy04)| [LeetCode](https://leetcode.com/u/keshav_30/)
