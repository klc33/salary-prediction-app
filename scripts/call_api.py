import requests

API_URL = "http://127.0.0.1:8000/predict"

def get_salary_prediction(experience_level, employment_type, job_title,
                          employee_residence, company_size, remote_ratio):
    params = {
        "experience_level": experience_level,
        "employment_type": employment_type,
        "job_title": job_title,
        "employee_residence": employee_residence,
        "company_size": company_size,
        "remote_ratio": remote_ratio
    }

    try:
        response = requests.get(API_URL, params=params)
        response.raise_for_status()
        data = response.json()
        if "predicted_salary" in data:
            return data["predicted_salary"]
        else:
            return f"Error from API: {data}"
    except requests.exceptions.RequestException as e:
        return f"Request failed: {e}"

# --- MAIN ---
if __name__ == "__main__":
    salary = get_salary_prediction(
        experience_level="SE",
        employment_type="FT",
        job_title="Data Scientist",
        employee_residence="US",
        company_size="M",
        remote_ratio=50
    )

    if isinstance(salary, float):
        print(f"Predicted Salary: ${salary:.2f}")
    else:
        print(salary)