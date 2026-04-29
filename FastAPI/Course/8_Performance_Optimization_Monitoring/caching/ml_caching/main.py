import redis
import hashlib
import joblib
import json
import logging
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import cast
from redis.exceptions import ConnectionError


app = FastAPI()

# Logging Setup
logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s (line %(lineno)d) - %(levelname)s - %(message)s]",
    datefmt="%m-%d-%Y %H:%M:%S"
)

# Redis Setup
try:
    redis_client = redis.Redis(
        host='localhost',
        port=6379,
        db=0,
        decode_responses=True
    )
    redis_client.ping()
    logging.info("Connected to Redis")
except ConnectionError:
    logging.error("Redis connection failed")
    redis_client = None

# Load Model
try:
    model = joblib.load("model.joblib")
    logging.info("Model loaded successfully")
except Exception as e:
    logging.error(f"Model loading failed: {e}")
    model = None

# Schema
class IrisFlower(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

    def to_list(self):
        return [
            self.sepal_length,
            self.sepal_width,
            self.petal_length,
            self.petal_width
        ]

    def cache_key(self):
        raw = json.dumps(self.model_dump(), sort_keys=True)
        return f"predict:{hashlib.sha256(raw.encode()).hexdigest()}"

# Endpoint
@app.post('/predict')
async def predict(data: IrisFlower):
    if model is None:
        raise HTTPException(status_code=500, detail="Model not loaded")

    key = data.cache_key()

    # Check Cache
    if redis_client:
        cached_result = redis_client.get(key)
    else:
        cached_result = None

    if cached_result:
        logging.info("Cache HIT")
        return json.loads(cast(str, cached_result))

    logging.info("Cache MISS - Running Model")

    prediction = model.predict([data.to_list()])[0]
    result = {'prediction': int(prediction)}

    # Store in Cache
    if redis_client:
        redis_client.set(key, json.dumps(result), ex=3600)

    return result

