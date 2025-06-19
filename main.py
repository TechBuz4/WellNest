from fastapi import FastAPI
from pydantic import BaseModel
from pred import predict_risk  # Your own prediction function
from epds import print_epds_results, epds_assessment, list_answers
from typing import List

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


class EPDSInput(BaseModel):
    responses: List[int]

@app.post("/epds")
def epds_score(data: EPDSInput):
    try:
        epds_score, q3, q4, q5, q10 = list_answers(data)
        result = print_epds_results(epds_assessment(epds_score=1, q3=2, q4=1, q5=0, q10=1))
        return result
    except ValueError as e:
        return {"error": str(e)}

