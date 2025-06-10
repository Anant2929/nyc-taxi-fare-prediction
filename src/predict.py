import pickle
import pandas as pd
from .preprocess import preprocess_data, input_cols

def load_model(model_path='src/model.pkl'):
    with open(model_path, 'rb') as f:
        model = pickle.load(f)
    return model

def predict_fare(pickup_lon, pickup_lat, dropoff_lon, dropoff_lat, passenger_count, pickup_datetime):
    model = load_model()
    input_data = {
        'pickup_longitude': pickup_lon,
        'pickup_latitude': pickup_lat,
        'dropoff_longitude': dropoff_lon,
        'dropoff_latitude': dropoff_lat,
        'passenger_count': passenger_count,
        'pickup_datetime': pd.to_datetime(pickup_datetime)
    }
    input_df = pd.DataFrame([input_data])
    input_df = preprocess_data(input_df, is_training=False)
    input_df = input_df[input_cols]
    fare = model.predict(input_df)[0]
    return max(fare, 2.5)  # Minimum fare