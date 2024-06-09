import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
import joblib
from transformer import DataFrameSelector

# Load the model and scaler
model = joblib.load('model.pkl')
scaler = joblib.load('scaler.pkl')

# Define the web page
st.title('House Price Predictor')

# Define inputs
bedrooms = st.number_input('Number of Bedrooms', min_value=1, max_value=10, value=3)
bathrooms = st.number_input('Number of Bathrooms', min_value=1, max_value=10, value=2)
sqft_living = st.number_input('Square footage of the apartments interior living space', min_value=500, max_value=10000,
                              value=2000)
sqft_lot = st.number_input('Square footage of the land space', min_value=500, max_value=10000, value=5000)
floors = st.number_input('Number of floors', min_value=1, max_value=5, value=1)
waterfront = st.radio('Waterfront', ['Yes', 'No'])
# view dropdown
view = st.selectbox('View', ['Bad', 'Average', 'Good', 'Very good', 'Excellent'])
condition = st.selectbox('Condition', ['Bad', 'Average', 'Good', 'Very good', 'Excellent'])
longevity = st.selectbox('Longevity', ['old', 'middle', 'new'])
grade = st.number_input('Grade', min_value=1, max_value=13, value=7)
sqft_above = st.number_input('Square footage of house apart from basement', min_value=500, max_value=10000, value=1500)
sqft_basement = st.number_input('Square footage of the basement', min_value=0, max_value=5000, value=500)
renovated = st.radio('Renovated', ['Yes', 'No'])
long_cat = st.radio('Longitude', ['East', 'West'])
lat_cat = st.radio('Latitude', ['North', 'South'])
lat = 47.5
long = -122.2
sqft_living15 = 2000
sqft_life15_cat = 'medium'
sqft_lot15 = 5000
sqft_lot15_cat = 'medium'
month = 5
year = 2014

# Preprocess the data
if waterfront == 'Yes':
    waterfront = 1
else:
    waterfront = 0

if renovated == 'Yes':
    renovated = 'renovated'
    yr_renovated = 2014
else:
    renovated = 'not renovated'
    yr_renovated = 0

if sqft_basement > 0:
    basement = 'has basement'
else:
    basement = 'no basement'

if lat_cat == 'North':
    lat_cat = 'north'
else:
    lat_cat = 'south'

if long_cat == 'East':
    long_cat = 'east'
else:
    long_cat = 'west'

if view == 'Bad':
    view = 0
elif view == 'Average':
    view = 1
elif view == 'Good':
    view = 2
elif view == 'Very good':
    view = 3
else:
    view = 4

if condition == 'Bad':
    condition = 1
elif condition == 'Average':
    condition = 2
elif condition == 'Good':
    condition = 3
elif condition == 'Very good':
    condition = 4
else:
    condition = 5

if sqft_living < 1500:
    sqft_living_cat = 'small'
elif sqft_living < 2500:
    sqft_living_cat = 'medium'
elif sqft_living < 3500:
    sqft_living_cat = 'big'
else:
    sqft_living_cat = 'very big'

if sqft_lot < 5000:
    sqft_lot_cat = 'small'
elif sqft_lot < 10000:
    sqft_lot_cat = 'medium'
elif sqft_lot < 15000:
    sqft_lot_cat = 'big'
else:
    sqft_lot_cat = 'very big'

if sqft_above < 1500:
    sqft_above_cat = 'small'
elif sqft_above < 2500:
    sqft_above_cat = 'medium'
elif sqft_above < 3500:
    sqft_above_cat = 'big'
else:
    sqft_above_cat = 'very big'

if sqft_basement < 500:
    sqft_basement_cat = 'small'
elif sqft_basement < 1000:
    sqft_basement_cat = 'medium'
elif sqft_basement < 1500:
    sqft_basement_cat = 'big'
else:
    sqft_basement_cat = 'very big'

if longevity == 'old':
    yr_built = 1900
    built_cat = 'old'
elif longevity == 'middle':
    yr_built = 2000
    built_cat = 'middle'
else:
    yr_built = 2014
    built_cat = 'new'

data = [{'bedrooms': bedrooms, 'bathrooms': bathrooms, 'sqft_living': sqft_living, 'sqft_lot': sqft_lot, 'floors': floors, 'waterfront': waterfront, 'view': view, 'condition': condition, 'grade': grade, 'sqft_above': sqft_above, 'sqft_basement': sqft_basement, 'renovated_cat': renovated, 'basement_cat': basement, 'lat_cat': lat_cat, 'long_cat': long_cat, 'lat': lat, 'long': long, 'sqft_living15': sqft_living15, 'sqft_living15_cat': sqft_life15_cat, 'sqft_lot15': sqft_lot15, 'sqft_lot15_cat': sqft_lot15_cat, 'month': month, 'year': year, 'yr_built': yr_built, 'yr_renovated': yr_renovated, 'built_cat': built_cat, 'sqft_living_cat': sqft_living_cat, 'sqft_lot_cat': sqft_lot_cat, 'sqft_above_cat': sqft_above_cat, 'sqft_basement_cat': sqft_basement_cat}]

input_df = pd.DataFrame(data)

# Predict the output
if st.button('Predict'):
    output = model.predict(input_df)
    st.write(f'The predicted price is ${output[0]}')
