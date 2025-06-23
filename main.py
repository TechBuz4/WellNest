from fastapi import FastAPI
from pydantic import BaseModel
from pred import predict_risk  # Your own prediction function
from epds_score import print_epds_results, epds_assessment, list_answers
from typing import List
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Pregnancy Risk API"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Or specify your frontend domain(s)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
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
        # Extract data from request
        epds_score_val, q3, q4, q5, q10 = list_answers(data.responses)

        # Perform full assessment
        result = epds_assessment(epds_score_val, q3, q4, q5, q10)

        return result

    except ValueError as e:
        return {"error": str(e)}
