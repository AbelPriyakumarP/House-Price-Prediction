#number of bedrooms', 'number of bathrooms', 'living area', 'condition of the house', 'Number of schools nearby

import streamlit as st
import joblib
import numpy as np
import pandas as pd

model = joblib.load('model.pkl')


st.title('House Price Prtediction App')

st.divider()

st.write('This app uses Machine Learning for Predicting house price with given features of the house. For using this app you can enter the inputs from this UI and then use predict button.')

st.divider()

bedrooms = st.number_input('Number of bedrooms', min_value=0, value=0)
bathrooms = st.number_input('Number of bathrooms', min_value=0, value=0)
living_area = st.number_input('Number of living area', min_value=0, value=2000)
condition = st.number_input('Number of condition', min_value=0, value=3)
numberofschools = st.number_input('Number of schools nearby', min_value=0, value=0)

st.divider() 

X = [[bedrooms, bathrooms,living_area,condition,numberofschools]]
predictbutton = st.button('Predict')

if predictbutton:
    st.snow()
    X_array = np.array(X)
    prediction = model.predict(X_array)[0]
    st.write(f'Price Prediction is {prediction:,.2f}')
else:
    st.write('Please use predict button after entering values')
    
    