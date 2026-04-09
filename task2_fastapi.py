import joblib
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel


class PassengerData(BaseModel):
    age: float
    fare: float
    embarked: str
    sex: str


app = FastAPI(title="Titanic Survival Predictor")

try:
    model = joblib.load('model_pipeline.joblib')
except:
    model = None
    print("Внимание: Файл модели не найден!")


@app.get("/")
def read_root():
    return {"status": "online", "model_loaded": model is not None}


@app.post("/predict")
def predict(data: PassengerData):
    if model is None:
        return {"error": "Модель не загружена"}

    input_df = pd.DataFrame([data.model_dump()])

    prediction = model.predict(input_df)
    probability = model.predict_proba(input_df).max()
    result = "Survived" if prediction[0] == 1 else "Not Survived"

    return {
        "prediction": result,
        "probability": f"{probability:.2%}"
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)
