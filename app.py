import streamlit as st
import pandas as pd
import pickle

# Load trained Ridge model
with open('Ridgemodel.pkl', 'rb') as file:
    model = pickle.load(file)

st.title("🏠 Bengaluru House Price Predictor")
st.markdown("Enter the details below to predict the house price (in lakhs) 💸")

# Input Fields
location = st.text_input("📍 Location (e.g., Whitefield, Rajaji Nagar, etc.)")
sqft = st.number_input("📐 Total Square Feet", min_value=300.0, step=10.0)
bath = st.number_input("🚿 Number of Bathrooms", min_value=1, step=1)
bhk = st.number_input("🛏️ Number of BHK", min_value=1, step=1)

# Prediction
if st.button("🎯 Predict Price"):
    if location.strip() == "":
        st.warning("⚠️ Please enter a location.")
    else:
        # ✅ Create DataFrame with column names matching training data
        input_df = pd.DataFrame([[location, sqft, bath, bhk]],
                                columns=['location', 'total_sqft', 'bath', 'bhk'])

        # Predict using model
        prediction = model.predict(input_df)[0]

        # ✅ Format output: Cr if > 99 Lakhs
        if prediction >= 100:
            price_str = f"₹ {round(prediction / 100, 2)} Cr"
        else:
            price_str = f"₹ {round(prediction, 2)} Lakhs"

        st.success(f"🏡 Estimated Price: {price_str}")

# streamlit run app.py