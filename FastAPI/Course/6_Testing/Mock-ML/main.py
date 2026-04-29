from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
from model import model
import numpy as np

app = FastAPI()

class IrisFlower(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float


@app.post("/predict")
def predict(data: IrisFlower):
    features = np.array([
        [
            data.sepal_length,
            data.sepal_width,
            data.petal_length,
            data.petal_width
        ]
    ])
    prediction = model.predict(features)
    return {"Prediction":int(prediction[0])}