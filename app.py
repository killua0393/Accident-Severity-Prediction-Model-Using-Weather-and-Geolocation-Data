from flask import Flask, render_template, request, jsonify
import joblib
import pandas as pd
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)

rf_model = joblib.load('rf_model.pkl')
le = joblib.load('label_encoder.pkl')
scaler = joblib.load('scaler.pkl')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        start_lat = data.get('Start_Lat')
        start_lng = data.get('Start_Lng')
        weather_condition = data.get('Weather_Condition')
        wind_speed = data.get('Wind_Speed')

        if None in (start_lat, start_lng, weather_condition, wind_speed):
            return jsonify({'error': 'Missing one or more required input fields.'}), 400

        new_data = pd.DataFrame({
            'Start_Lat': [start_lat],
            'Start_Lng': [start_lng],
            'Weather_Condition': [weather_condition],
            'Wind_Speed(mph)': [wind_speed]
        })

        try:
            new_data['Weather_Condition'] = le.transform(new_data['Weather_Condition'])
        except ValueError:
            return jsonify({'error': f"Invalid weather condition: '{weather_condition}'."}), 400

        numeric_cols = ['Start_Lat', 'Start_Lng', 'Wind_Speed(mph)']
        new_data[numeric_cols] = scaler.transform(new_data[numeric_cols])

        prediction = rf_model.predict(new_data)

        return jsonify({'predicted_severity': int(prediction[0])})

    except Exception as e:
        return jsonify({'error': f'An error occurred during prediction: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True)
