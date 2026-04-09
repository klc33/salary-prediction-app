import pandas as pd
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.db.save_results import save_prediction

from src.llm.analyze import generate_analysis
from scripts.call_api import get_salary_prediction

# Example: 3 jobs
jobs = [
    {"job_title": "Data Scientist", "experience_level": "SE", "employment_type": "FT",
     "employee_residence": "US", "company_size": "M", "remote_ratio": 50},
    {"job_title": "ML Engineer", "experience_level": "MI", "employment_type": "FT",
     "employee_residence": "US", "company_size": "L", "remote_ratio": 20},
    {"job_title": "Data Analyst", "experience_level": "EN", "employment_type": "FT",
     "employee_residence": "US", "company_size": "S", "remote_ratio": 0},
    {"job_title": "Big Data Engineer", "experience_level": "SE", "employment_type": "FT",
     "employee_residence": "GB", "company_size": "M", "remote_ratio": 50},
    {"job_title": "Product Data Analyst", "experience_level": "MI", "employment_type": "FT",
     "employee_residence": "HN", "company_size": "S", "remote_ratio": 0},
    {"job_title": "Lead Data Scientist", "experience_level": "SE", "employment_type": "FT",
     "employee_residence": "US", "company_size": "S", "remote_ratio": 100},
    {"job_title": "Business Data Analyst", "experience_level": "MI", "employment_type": "FT",
     "employee_residence": "US", "company_size": "L", "remote_ratio":100},
    {"job_title": "Lead Data Engineer", "experience_level": "SE", "employment_type": "FT",
     "employee_residence": "NZ", "company_size": "S", "remote_ratio": 50},
]

# Call API for each job and collect results
data = []
for job in jobs:
    salary = get_salary_prediction(**job)
    job['predicted_salary'] = salary
    data.append(job)

df = pd.DataFrame(data)

# Generate LLM analysis
result = generate_analysis(df)

for _, row in df.iterrows():
    save_prediction({
        "job_title": row["job_title"],
        "experience_level": row["experience_level"],
        "employment_type": row["employment_type"],
        "employee_residence": row["employee_residence"],
        "company_size": row["company_size"],
        "remote_ratio": row["remote_ratio"],
        "predicted_salary": row["predicted_salary"],
        "analysis": result["narrative"],
        "chart_path": result["chart_path"]
    })

print(result['narrative'])      # narrative text from LLM
print("Chart saved at:", result['chart_path'])