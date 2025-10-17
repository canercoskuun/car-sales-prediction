from flask import Flask, request, jsonify
from prophet.serialize import model_from_json
import json
import pandas as pd
import numpy as np 

# Load the saved model
with open('serialized_model.json', 'r') as fin:
    loaded_model = model_from_json(json.load(fin))

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict_sales():
    data = request.get_json(force=True)
    future_date = pd.DataFrame({'ds': [pd.to_datetime(data['date'])]})
    
    # Make a prediction
    forecast = loaded_model.predict(future_date)
    
    # Get the prediction, round it, and convert to an integer
    prediction = int(np.round(forecast['yhat'].iloc[0]))

    return jsonify({'prediction': prediction})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)