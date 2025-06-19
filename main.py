from fastapi import FastAPI
from pydantic import BaseModel
from pred import predict_risk  # Your own prediction function

app = FastAPI(
    title="Pregnancy Risk API"
)

# Define the expected input features
class InputData(BaseModel):
    age: int
    SystolicBP: float
    DiastolicBP: float
    BS: float
    BodyTemp: float
    HeartRate: int

@app.get("/")
def read_root():
    return {"message": "Welcome to the Pregnancy Risk Prediction API"}

@app.post("/predict")
def predict(data: InputData):
    try:
        result = predict_risk(data.dict())
        return {"risk_level": result}
    except Exception as e:
        return {"error": str(e)}
