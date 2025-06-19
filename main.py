from fastapi import FastAPI
from pydantic import BaseModel
from predictor import predict_risk
import pickle
import numpy as np
nest_asyncio.apply()

"""# Load the trained model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)"""

app = FastAPI(
    title = "Pregnancy Risk API"
)

# Define the request body format
class InputData(BaseModel):
    age: int
    SystolicBP: float
    DiastolicBP: float
    BS: float
    BodyTemp: float
    heart_rate: int

@app.get("/")
def read_root():
    return {"message": "Welcome to the Pregnancy Risk Prediction API"}

@app.post("/predict")
def predict(data: InputData):
    # Convert input to the model's expected format
    input_array = """Age: {}
    SystolicBP: {}
    DiastolicBP: {}
    BS: {}
    BodyTemp: {}
    HeartRate: {}
    Predict the Risk Level.""".format(data.age, data.SystolicBP, data.DiastolicBP, data.BS, data.BodyTemp, data.heart_rate)
    # Make prediction
    #prediction = sampler.chat(input_array)
    print(" /predict endpoint was triggered!")
    try:
        result = predict_risk(data.dict())
        return {"risk_level": result}
    except Exception as e:
        print(f"Error in /predict: {e}")
        return {"error": str(e)}

    return {"prediction": prediction}


    '''
    # gemma model
    def predict(data: InputData):
    # Convert input to the model's expected format
    input_array = """Age: {}
    SystolicBP: {}
    DiastolicBP: {}
    BS: {}
    BodyTemp: {}
    HeartRate: {}
    Predict the Risk Level.""".format(data.age, data.SystolicBP, data.DiastolicBP, data.BS, data.BodyTemp, data.heart_rate)
    # Make prediction
    #prediction = sampler.chat(input_array)
    print(" /predict endpoint was triggered!")
    try:
        result = predict_data(data.dict())
        return {"risk_level": result}
    except Exception as e:
        print(f"Error in /predict: {e}")
        return {"error": str(e)}

    return {"prediction": prediction}'''
