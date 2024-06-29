#Final
import pandas as pd
import numpy as np
import joblib
from fastapi import FastAPI 
from sklearn.preprocessing import PowerTransformer,StandardScaler

# Load the pre-trained machine learning model
scaler= PowerTransformer()
model = joblib.load(r"linear_regression_model.joblib")

app = FastAPI()

@app.get("/Fat_Prediction")
async def get_input(
    Age: int,
    Neck: float,
    Weight : float,
    Height: float,
    Knee: float, 
    Ankle: float,
    Biceps: float,
    Forearm: float,
    Wrist: float,
    Chest: float,
    Abdomen: float,
    Hip: float,
    Thigh: float
): 
   # Calculate BMI
    bmi = Weight / (Height ** 2)

    # Calculate ACratio
    ACratio = Abdomen / Chest
    
    # Calculate HTratio
    HTratio = Hip / Thigh

    # Create a dictionary with input values
    input_data = {
        "Age": Age,
        'Knee': Knee, 
        'Ankle': Ankle, 
        "Biceps": Biceps, 
        'Forearm' : Forearm,
        "Wrist":Wrist,
        "BMI": bmi,
        "ACratio": ACratio,
        "HTratio": HTratio 
    }

    # Convert input data to DataFrame
    input_df = pd.DataFrame([input_data])

    # Apply PowerTransformer scaling
    #input_scaled = scaler.transform(input_df)


    # Make prediction using the loaded model
    prediction = model.predict(input_df)

    # Format the prediction result
    result = {"predicted_fat_percentage": prediction[0]}

    return result
# Sample input data for testing
sample_input_data = {
    "Age": 30,
    "Knee": 35.0,
    "Ankle":40,
    "Biceps": 30.0,
    "Forearm":60,
    "Wrist":40.0,
    "BMI": 23.0,
    "ACratio": 85.0,
    "HTratio": 90.0
}


# Convert sample input data to DataFrame
sample_input_df = pd.DataFrame([sample_input_data])
sample_prediction = model.predict(sample_input_df )
sample_input_df['predicted_fat_percentage']=sample_prediction
print(sample_input_df)
#uvicorn api:app --reload
#To run the above url/docs#