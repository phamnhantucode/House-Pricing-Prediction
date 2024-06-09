import pandas as pd

from flask import Flask, request, jsonify
from sklearn.model_selection import train_test_split

app = Flask(__name__)


def preprocess(data):
    if (data['lat_cat'] == 'north'):
        data['lat'] = 47.75
    else:
        data['lat'] = 47.25

    if (data['long_cat'] == 'east'):
        data['long'] = -122.25
    else:
        data['long'] = -122.75

    if (data['sqft_living'] < 1500):
        data['sqft_living_cat'] = 'small'
    elif (data['sqft_living'] < 2500):
        data['sqft_living_cat'] = 'medium'
    elif (data['sqft_living'] < 3500):
        data['sqft_living_cat'] = 'big'
    else:
        data['sqft_living_cat'] = 'very big'

    if (data['sqft_lot'] < 5000):
        data['sqft_lot_cat'] = 'small'
    elif (data['sqft_lot'] < 10000):
        data['sqft_lot_cat'] = 'medium'
    elif (data['sqft_lot'] < 15000):
        data['sqft_lot_cat'] = 'big'
    else:
        data['sqft_lot_cat'] = 'very big'

    if (data['sqft_above'] < 1500):
        data['sqft_above_cat'] = 'small'
    elif (data['sqft_above'] < 2500):
        data['sqft_above_cat'] = 'medium'
    elif (data['sqft_above'] < 3500):
        data['sqft_above_cat'] = 'big'
    else:
        data['sqft_above_cat'] = 'very big'

    if (data['sqft_basement'] < 500):
        data['sqft_basement_cat'] = 'small'
    elif (data['sqft_basement'] < 1000):
        data['sqft_basement_cat'] = 'medium'
    elif (data['sqft_basement'] < 1500):
        data['sqft_basement_cat'] = 'big'
    else:
        data['sqft_basement_cat'] = 'very big'

    data['year'] = 2014
    data['month'] = 5
    data['sqft_living15'] = 2000
    data['sqft_lot15'] = 5000
    data['yr_built'] = 2000
    data['yr_renovated'] = 0
    data['built_cat'] = 'middle'
    data['sqft_living15_cat'] = 'medium'
    data['sqft_lot15_cat'] = 'medium'

    return data


@app.route('/predict', methods=['POST', 'GET'])
def predict():
    data = {
        'bedrooms': 4,
        'bathrooms': 2,
        'sqft_living': 20000,
        'sqft_lot': 5000,
        'floors': 1,
        'waterfront': 0,
        'view': 0,
        'condition': 3,
        'grade': 7,
        'sqft_above': 1500,
        'sqft_basement': 500,
        'renovated_cat': 'not renovated',
        'basement_cat': 'has basement',
        'lat_cat': 'north',
        'long_cat': 'east'
    }
    # data = request.get_json(force=True)
    data = preprocess(data)
    print(data)
    data = pd.DataFrame([data])
    return jsonify({'prediction': predict_price(data)})


# write new rote index return hello world
@app.route('/')
def index():
    return "Hello World"


def predict_price(data):
    # Load the model
    import joblib
    model = joblib.load('model.pkl')

    # Make prediction
    prediction = model.predict(data)
    return prediction[0]


if __name__ == '__main__':
    app.run(port=5794, debug=True)
