from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)

    # Extract parameters from the POST request body
    param1 = data.get('param1')
    param2 = data.get('param2')
    # Add more parameters as needed

    # Call your prediction function
    prediction = predict_price(param1, param2)  # Replace with your function

    # Return the prediction as JSON
    return jsonify({'prediction': prediction})

# write new rote index return hello world
@app.route('/')
def index():
    return "Hello World"

def predict_price(param1, param2):
    return param1 + param2

if __name__ == '__main__':
    app.run(port=5484, debug=True)