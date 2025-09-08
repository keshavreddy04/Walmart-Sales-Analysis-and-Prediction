import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load predictions (exported CSV from your notebook)
@st.cache_data
def load_data():
    return pd.read_csv("walmart_predictions.csv")

df = load_data()

# Sidebar Filters
st.sidebar.header("Filters")
selected_store = st.sidebar.multiselect("Select Store(s)", options=df["Store"].unique(), default=df["Store"].unique())
selected_dept = st.sidebar.multiselect("Select Department(s)", options=df["Dept"].unique(), default=df["Dept"].unique())
df = load_data()
df["Date_original"] = pd.to_datetime(df["Date_original"])

# Sidebar filter
date_range = st.sidebar.date_input(
    "Select Date Range",
    [df["Date_original"].min().date(), df["Date_original"].max().date()]
)


# Filter data
# Convert date input (date → datetime)
start_date = pd.to_datetime(date_range[0])
end_date = pd.to_datetime(date_range[1])

filtered_df = df[
    (df["Store"].isin(selected_store)) &
    (df["Dept"].isin(selected_dept)) &
    (df["Date_original"].between(start_date, end_date))
]


# KPIs
total_sales = filtered_df["Predicted_Weekly_Sales"].sum()
avg_sales = filtered_df["Predicted_Weekly_Sales"].mean()
holiday_sales = filtered_df[filtered_df["IsHoliday_original"]==True]["Predicted_Weekly_Sales"].sum()

st.title("📊 Walmart Sales Prediction Dashboard")
st.markdown(f"**Total Predicted Sales:** ${total_sales:,.2f}")
st.markdown(f"**Average Weekly Sales:** ${avg_sales:,.2f}")
st.markdown(f"**Holiday Sales Contribution:** ${holiday_sales:,.2f}")

# --- Plots ---
st.subheader("Monthly Sales Trend")
monthly_sales = filtered_df.groupby(filtered_df["Date_original"].dt.to_period("M"))["Predicted_Weekly_Sales"].sum()
st.line_chart(monthly_sales)

st.subheader("Store-wise Sales")
store_sales = filtered_df.groupby("Store")["Predicted_Weekly_Sales"].sum()
st.bar_chart(store_sales)

st.subheader("Department-wise Sales")
dept_sales = filtered_df.groupby("Dept")["Predicted_Weekly_Sales"].sum()
st.bar_chart(dept_sales)

st.subheader("Holiday vs Non-Holiday Sales")
holiday_sales = filtered_df.groupby("IsHoliday_original")["Predicted_Weekly_Sales"].sum()
st.bar_chart(holiday_sales)

# Raw Data
if st.checkbox("Show Raw Data"):
    st.write(filtered_df)