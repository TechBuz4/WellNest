import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier, VotingClassifier
from sklearn.tree import DecisionTreeClassifier
from lightgbm import LGBMClassifier
import os

FEATURE_ORDER = ['age', 'SystolicBP', 'DiastolicBP', 'HeartRate', 'BS', 'BodyTemp']

import joblib

def load_model():
    """
    Loads the trained model and scaler from disk.
    Returns:
        - model: trained classifier (e.g., RandomForestClassifier)
        - scaler: fitted StandardScaler
    """
    model_path = "ensemble_model.pkl"
    scaler_path = "scaler.pkl"

    if not os.path.exists(model_path) or not os.path.exists(scaler_path):
        raise FileNotFoundError("Model or scaler file not found. Make sure both are saved in the same directory.")

    model = joblib.load(model_path)
    scaler = joblib.load(scaler_path)

    return model, scaler

def predict_risk(instance: dict) -> str:
    """
    Accepts a dict of features, scales the input, and predicts risk level.
    """
    model, fitted_scaler = load_model()

    try:
        x_input = np.array([[instance[feat] for feat in FEATURE_ORDER]])
    except KeyError as e:
        raise ValueError(f"Missing expected feature in input: {e}")

    x_scaled = fitted_scaler.transform(x_input)
    pred_class = model.predict(x_scaled)[0]

    label_map = {0: "low risk", 1: "medium risk", 2: "high risk"}
    return label_map.get(pred_class, "unknown risk")
