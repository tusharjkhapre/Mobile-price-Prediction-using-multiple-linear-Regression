import streamlit as st
import pickle
import numpy as np
from mappings import mappings


with open("indianmodel.pkl","rb") as p:
    indianmodel=pickle.load(p)

with open("pakistanmodel.pkl","rb") as p:
    pakistanmodel=pickle.load(p)

with open("Dubaimodel.pkl","rb") as p:
    Dubaimodel=pickle.load(p)


with open("USAmodel.pkl","rb") as p:
    USAmodel=pickle.load(p)


with open("Chinamodel.pkl","rb") as p:
    Chinamodel=pickle.load(p)

st.title("Mobile price prediction")
st.write("please enter the required values to predict the price of your Mobile")

model_list=list(set(mappings.keys()))

Company_Name=st.selectbox("Select your mobile Company Name:",model_list)
Model_Name=st.selectbox("select your model name:",min_value=0.0, format="%.2f")
Mobile_Weight=st.number_input("how heavy:",min_value=0.0, format="%.2f")
RAM=st.number_input("Tell the Ram of your Mobile:",min_value=0.0, format="%.2f")
Front_Camera=st.selectbox("front camera:",min_value=0.0, format="%.2f")
Back_Camera=st.selectbox("Back_Camera",min_value=0.0, format="%.2f")
Battery_Capacity=st.number_input("Battery_Capacity:",min_value=0.0, format="%.2f")
Screen_Size=st.number_input("Screen_Size:",min_value=0.0, format="%.2f")
Launched_Year=st.selectbox("Launched Year:",min_value=0.0, format="%.2f")


if st.button("Predict the price of india"):
    model_name=mappings[indianmodel]
    features=np.array([[model_name,Company_Name,Model_Name,Mobile_Weight,RAM,Front_Camera,Back_Camera,Battery_Capacity,Screen_Size,Launched_Year]])
    predictions=indianmodel.predict(features)[0]
    st.success(f"Predicted Sales: {predictions:.2f}")

