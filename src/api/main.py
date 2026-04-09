from fastapi import FastAPI
import pandas as pd
import pickle

# Create FastAPI app
app = FastAPI(title="Salary Prediction API")

# Load Random Forest model
with open("models/model.pkl", "rb") as f:
    model = pickle.load(f)

# Save model feature names
model_features = model.feature_names_in_

@app.get("/predict")
def predict(
    experience_level: str,
    employment_type: str,
    job_title: str,
    employee_residence: str,
    company_size: str,
    remote_ratio: float
):
    # Step 1: Create DataFrame
    input_df = pd.DataFrame([{
        "experience_level": experience_level,
        "employment_type": employment_type,
        "job_title": job_title,
        "employee_residence": employee_residence,
        "company_size": company_size,
        "remote_ratio": remote_ratio
    }])

    # Step 2: One-Hot Encode categorical features
    input_df = pd.get_dummies(input_df)

    # Step 3: Align with training columns
    for col in model_features:
        if col not in input_df.columns:
            input_df[col] = 0
    input_df = input_df[model_features]

    # Step 4: Predict
    prediction = model.predict(input_df)[0]

    # Step 5: RETURN AS JSON CORRECTLY
    return {"predicted_salary": float(prediction)}