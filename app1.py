import streamlit as st
import pickle
import numpy as np
from mappings import (Company_Name_mapping, Model_Name_mapping,Front_Camera_mapping,Back_Camera_mapping,Processor_mapping)

# Load Models
with open("indianmodel.pkl", "rb") as p:
    indian_model = pickle.load(p)

with open("pakistanmodel.pkl","rb") as p:
    pakistan_model=pickle.load(p)

with open("Dubaimodel.pkl","rb") as p:
    Dubai_model=pickle.load(p)


with open("USAmodel.pkl","rb") as p:
    USA_model=pickle.load(p)


with open("Chinamodel.pkl","rb") as p:
    China_model=pickle.load(p)

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
Company_Name = st.selectbox("Select your mobile Company Name:",Company_Name_list)
Model_Name = st.selectbox("Select your model name:",model_Name_list)
Mobile_Weight = st.number_input("How heavy is the mobile? (grams)", min_value=50.0, format="%.2f")
RAM = st.number_input("Enter RAM (GB):", min_value=1.0, format="%.2f")
Front_Camera = st.selectbox("Front Camera (MP):",Front_Camera_list)
Back_Camera = st.selectbox("Back Camera (MP):",Back_Camera_list)
Processor = st.selectbox("Processor:", Processor_list)
Battery_Capacity = st.number_input("Battery Capacity (mAh):", min_value=1000.0, format="%.2f")
Screen_Size = st.number_input("Screen Size (inches):", min_value=4.0, format="%.2f")
Launched_Year = st.selectbox("Launched Year:", [2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025])

# Predict Button
if st.button("Predict Price for India"):
    company_enc = Company_Name_mapping.get(Company_Name, -1)
    model_enc = Model_Name_mapping.get(Model_Name, -1)
    front_camera_enc = Front_Camera_mapping.get(Front_Camera, -1)   
    back_camera_enc = Back_Camera_mapping.get(Back_Camera, -1)
    processor_enc = Processor_mapping.get(Processor, -1)

    # Create Feature Array
    features = np.array([[company_enc,model_enc, Mobile_Weight, RAM, front_camera_enc, back_camera_enc,processor_enc,Battery_Capacity, Screen_Size, Launched_Year]], dtype=object)

    # Predict
    prediction = float(indian_model.predict(features)[0])
    st.success(f"Predicted Price: ₹{prediction:.2f}")
# Predict Button
if st.button("Predict Price for Pakistan"):
    company_enc = Company_Name_mapping.get(Company_Name, -1)
    model_enc = Model_Name_mapping.get(Model_Name, -1)
    front_camera_enc = Front_Camera_mapping.get(Front_Camera, -1)   
    back_camera_enc = Back_Camera_mapping.get(Back_Camera, -1)
    processor_enc = Processor_mapping.get(Processor, -1)

    # Create Feature Array
    features = np.array([[company_enc,model_enc, Mobile_Weight, RAM, front_camera_enc, back_camera_enc,processor_enc,Battery_Capacity, Screen_Size, Launched_Year]], dtype=object)

    prediction = float(pakistan_model.predict(features)[0])
    st.success(f"Predicted Price: PKR {prediction:.2f}")   
# Predict Button
if st.button("Predict Price for Dubai"):
    company_enc = Company_Name_mapping.get(Company_Name, -1)
    model_enc = Model_Name_mapping.get(Model_Name, -1)
    front_camera_enc = Front_Camera_mapping.get(Front_Camera, -1)   
    back_camera_enc = Back_Camera_mapping.get(Back_Camera, -1)
    processor_enc = Processor_mapping.get(Processor, -1)

    # Create Feature Array
    features = np.array([[company_enc,model_enc, Mobile_Weight, RAM, front_camera_enc, back_camera_enc,processor_enc,Battery_Capacity, Screen_Size, Launched_Year]], dtype=object)

    prediction = float(Dubai_model.predict(features)[0])
    st.success(f"Predicted Price: AED {prediction:.2f}") 
# Predict Button
if st.button("Predict Price for USA"):
    company_enc = Company_Name_mapping.get(Company_Name, -1)
    model_enc = Model_Name_mapping.get(Model_Name, -1)
    front_camera_enc = Front_Camera_mapping.get(Front_Camera, -1)   
    back_camera_enc = Back_Camera_mapping.get(Back_Camera, -1)
    processor_enc = Processor_mapping.get(Processor, -1)

    # Create Feature Array
    features = np.array([[company_enc,model_enc, Mobile_Weight, RAM, front_camera_enc, back_camera_enc,processor_enc,Battery_Capacity, Screen_Size, Launched_Year]], dtype=object)

    prediction = float(USA_model.predict(features)[0])
    st.success(f"Predicted Price: $ {prediction:.2f}") 

# Predict Button
if st.button("Predict Price for China"):
    company_enc = Company_Name_mapping.get(Company_Name, -1)
    model_enc = Model_Name_mapping.get(Model_Name, -1)
    front_camera_enc = Front_Camera_mapping.get(Front_Camera, -1)   
    back_camera_enc = Back_Camera_mapping.get(Back_Camera, -1)
    processor_enc = Processor_mapping.get(Processor, -1)

    # Create Feature Array
    features = np.array([[company_enc,model_enc, Mobile_Weight, RAM, front_camera_enc, back_camera_enc,processor_enc,Battery_Capacity, Screen_Size, Launched_Year]], dtype=object)
    
    prediction = float(China_model.predict(features)[0])
    st.success(f"Predicted Price: ¥{prediction:.2f}")