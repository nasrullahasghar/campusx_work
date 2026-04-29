from fastapi.testclient import TestClient
from unittest.mock import patch
from main import app
import numpy as np

client = TestClient(app)

def test_predict_with_mock():
    with patch("main.model.predict") as mock_predict:
        mock_predict.return_value = [99]

        response = client.post(
            "/predict",
            json={
                "sepal_length": 5.5,
                "sepal_width": 2.1,
                "petal_length": 4.3,
                "petal_width": 1.25
            }
        )

        assert response.status_code == 200
        assert response.json() == {"Prediction": 99}