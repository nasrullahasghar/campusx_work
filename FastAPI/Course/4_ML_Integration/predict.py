import joblib
import numpy as np
from typing import List


save_model = joblib.load("model.joblib")
print("Loaded the model")

def make_prediction(data:dict) -> float:
    features = np.array([
        [
            data["longitude"],
            data["latitude"],
            data["housing_median_age"],
            data["total_rooms"],
            data["total_bedrooms"],
            data["population"],
            data["households"],
            data["median_income"],
        ]
    ])
    prediction = save_model.predict(features)
    return float(prediction[0])

def make_batch_predictions(data: List[dict]) -> np.ndarray:
    X = np.array(
        [
            [
                d["longitude"],
                d["latitude"],
                d["housing_median_age"],
                d["total_rooms"],
                d["total_bedrooms"],
                d["population"],
                d["households"],
                d["median_income"],
            ]
            for d in data
        ]
    )
    return save_model.predict(X)