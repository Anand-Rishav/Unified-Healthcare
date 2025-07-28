from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd, joblib
from pathlib import Path

# Auto-load latest model
MODEL_PATH = sorted(Path('.').glob('models/best_pipe_*.joblib'))[-1]
MODEL = joblib.load(MODEL_PATH)
app = FastAPI(title='Blood Donation Prediction API')

# Define the input features based on the training data columns
class InputFeatures(BaseModel):
    Recency: int
    Frequency: int
    Time: int
    # Note: We do not include Monetary as it was dropped.

@app.post('/predict')
def predict(p: InputFeatures):
    # Create a DataFrame from the input
    df = pd.DataFrame([p.dict()])

    # Feature Engineering: Must match the training process
    df['Donation_Frequency_per_Month'] = df['Frequency'] / df['Time']
    df['Time_Between_Donations'] = df['Time'] / df['Frequency']

    # Ensure column order matches the model's expectation if necessary
    # In this pipeline, ColumnTransformer handles it by name, so order is not critical.

    # Get probability and prediction
    prob = MODEL.predict_proba(df)[0, 1]
    pred = MODEL.predict(df)[0]

    return {'prediction': int(pred), 'probability': float(prob)}
