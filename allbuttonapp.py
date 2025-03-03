import streamlit as st
import pickle
import numpy as np
from mappings import (Company_Name_mapping, Model_Name_mapping, Front_Camera_mapping, Back_Camera_mapping, Processor_mapping)

# Load Models
models = {
    "India": "indianmodel.pkl",
    "Pakistan": "pakistanmodel.pkl",
    "Dubai": "Dubaimodel.pkl",
    "USA": "USAmodel.pkl",
    "China": "Chinamodel.pkl"
}

loaded_models = {}
for country, model_path in models.items():
    with open(model_path, "rb") as p:
        loaded_models[country] = pickle.load(p)

# Page Title
st.title("Mobile Price Prediction")
st.write("Please enter the required values to predict the price of your Mobile")

# Get Company List from mappings
Company_Name_list = list(Company_Name_mapping.keys())
model_Name_list = list(Model_Name_mapping.keys())
Front_Camera_list = list(Front_Camera_mapping.keys())
Back_Camera_list = list(Back_Camera_mapping.keys())
Processor_list = list(Processor_mapping.keys())

# Streamlit Input Fields
Company_Name = st.selectbox("Select your mobile Company Name:", Company_Name_list)
Model_Name = st.selectbox("Select your model name:", model_Name_list)
Mobile_Weight = st.number_input("How heavy is the mobile? (grams)", min_value=50.0, format="%.2f")
RAM = st.number_input("Enter RAM (GB):", min_value=1.0, format="%.2f")
Front_Camera = st.selectbox("Front Camera (MP):", Front_Camera_list)
Back_Camera = st.selectbox("Back Camera (MP):", Back_Camera_list)
Processor = st.selectbox("Processor:", Processor_list)
Battery_Capacity = st.number_input("Battery Capacity (mAh):", min_value=1000.0, format="%.2f")
Screen_Size = st.number_input("Screen Size (inches):", min_value=4.0, format="%.2f")
Launched_Year = st.selectbox("Launched Year:", [2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025])

# Predict Button for All Regions
if st.button("Predict Price for All Regions"):
    company_enc = Company_Name_mapping.get(Company_Name, -1)
    model_enc = Model_Name_mapping.get(Model_Name, -1)
    front_camera_enc = Front_Camera_mapping.get(Front_Camera, -1)
    back_camera_enc = Back_Camera_mapping.get(Back_Camera, -1)
    processor_enc = Processor_mapping.get(Processor, -1)

    # Create Feature Array
    features = np.array([[company_enc, model_enc, Mobile_Weight, RAM, front_camera_enc, back_camera_enc, processor_enc, Battery_Capacity, Screen_Size, Launched_Year]], dtype=object)

    # Dictionary for currency symbols
    currency_symbols = {
        "India": "₹",
        "Pakistan": "PKR",
        "Dubai": "AED",
        "USA": "$",
        "China": "¥"
    }

    # Predict Prices for All Regions
    results = []
    for country, model in loaded_models.items():
        prediction = float(model.predict(features)[0])
        results.append(f"{country}: {currency_symbols [country]}{prediction:.2f}\n")

    # Display Results
    st.success("\n".join(results))
