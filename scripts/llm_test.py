import pandas as pd
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

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

# Fixed: use attributes of ChatResponse correctly
# Assuming generate_analysis returns a dict with:
#   - 'narrative' as a string (from response.text)
#   - 'chart_path' as a string path to the chart image

print(result['narrative'])      # narrative text from LLM
print("Chart saved at:", result['chart_path'])