import streamlit as st
import pandas as pd
import joblib

# Load trained Random Forest model
model = joblib.load("Algorithmic_Trading_Strategy_Backtester.pkl")

# Page settings
st.set_page_config(
    page_title="Tesla Stock Predictor",
    page_icon="📈"
)

# Title
st.title("Tesla Stock Buy/Sell Predictor")
st.write("Enter Tesla stock information to generate a trading signal.")

# Input fields
# Input fields
col1, col2 = st.columns(2)

with col1:
    open_price = st.number_input("Open Price", min_value=0.0)
    low_price = st.number_input("Low Price", min_value=0.0)
    close_price = st.number_input("Close Price", min_value=0.0)

with col2:
    high_price = st.number_input("High Price", min_value=0.0)
    volume = st.number_input("Trading Volume", min_value=0)
# Predict button
if st.button("Predict Signal"):

    # Feature engineering
    price_change = close_price - open_price
    price_range = high_price - low_price
    daily_return = (close_price - open_price) / open_price
    high_low_ratio = high_price / low_price
    open_close_diff = open_price - close_price
    high_close_diff = high_price - close_price

    # Create input DataFrame
    input_data = pd.DataFrame({
        "Open": [open_price],
        "High": [high_price],
        "Low": [low_price],
        "Close": [close_price],
        "Volume": [volume],
        "Price_Change": [price_change],
        "Price_Range": [price_range],
        "Daily_Return": [daily_return],
        "High_Low_Ratio": [high_low_ratio],
        "Open_Close_Diff": [open_close_diff],
        "High_Close_Diff": [high_close_diff]
    })

    # Make prediction
    prediction = model.predict(input_data)[0]

    # Display result
    if prediction == 1:
        st.success("📈 BUY SIGNAL")
        st.write("The model predicts that the next-day closing price will be higher.")
    else:
        st.error("📉 SELL SIGNAL")
        st.write("The model predicts that the next-day closing price will not be higher.")