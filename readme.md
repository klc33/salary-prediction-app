# 💼 Salary Prediction Application

An end-to-end application that predicts salaries for data science jobs, generates insights via a local LLM, stores results in Supabase, and displays everything on a Streamlit dashboard.

---

## **Project Structure**


salary-prediction-app/
│
├── data/ # Raw + cleaned datasets
├── notebooks/ # EDA and preprocessing exploration
├── src/
│ ├── preprocessing/ # Data cleaning scripts
│ ├── model/ # Training + saving Random Forest model
│ ├── api/ # FastAPI app for predictions
│ ├── llm/ # LLM analysis (Ollama)
│ └── db/ # Supabase client + insertion logic
│
├── scripts/ # Scripts calling API and LLM
├── app/ # Streamlit dashboard
├── charts/ # Generated charts from LLM analysis
├── models/ # Saved model (.pkl)
├── .env # Environment variables (Supabase URL, key)
├── requirements.txt # Python dependencies
└── README.md



---

## **Features / Workflow**

1. **Data Cleaning & Preparation**
   - Raw Kaggle dataset: [Data Science Job Salaries](https://www.kaggle.com/datasets/ruchi798/data-science-job-salaries)
   - Preprocessing scripts in `src/preprocessing/`
   - Cleaned data saved for model training

2. **Model Training**
   - Random Forest model trained in `src/model/train.py`
   - Saved as `.pkl` in `models/`
   - Evaluated with metrics: MAE, MSE, R²

3. **API for Predictions**
   - FastAPI app in `src/api/app.py`
   - Validates all inputs
   - Returns predicted salary for given job details

4. **Script to Call API**
   - `scripts/call_api.py` calls API safely
   - Handles errors and different input combinations
   - Returns predicted salary

5. **LLM-Powered Analysis**
   - `src/llm/analyze.py` uses **Ollama local LLM**
   - Generates:
     - Narrative insights
     - Charts saved in `charts/` folder
   - Charts are unique per run (timestamped)

6. **Database Layer**
   - Supabase used to store:
     - Input features
     - Predicted salary
     - LLM analysis
     - Chart path
   - Tables defined in Supabase:
     - `predictions` with columns: id, job_title, experience_level, employment_type, employee_residence, company_size, remote_ratio, predicted_salary, analysis, chart_path, created_at

7. **Streamlit Dashboard**
   - `app/main.py` reads only from Supabase
   - Displays:
     - Predictions table
     - LLM insights
     - Charts
   - Filters by job title
   - Handles missing data gracefully

---

## **Setup & Installation**

1. **Clone the repository**

```bash
git clone <your-repo-url>
cd salary-prediction-app

## **Create virtual environment & install dependencies**

python -m venv .venv
source .venv/bin/activate   # macOS/Linux
.venv\Scripts\activate      # Windows

pip install -r requirements.txt


## **Setup the .env file**
SUPABASE_URL=your_supabase_url
SUPABASE_KEY=your_supabase_key

## **Start Ollama locally**
#Make sure Ollama app is open before running any LLM analysis.


#Usage#

##1 **Run the API**
uvicorn src.api.app:app --reload

**2 Run the test script (calls API + LLM + saves to DB)**

python scripts/llm_test.py

##
#Generates predictions
#Calls LLM for insights
#Saves chart in charts/
#Inserts results into Supabase
##

**3. Run Streamlit Dashboard from cmd **
streamlit run app/main.py

##
#Displays table of predictions
#Shows LLM insights
#Displays corresponding charts
#Allows filtering by job title
##


#Dependencies#
#Python 3.10+
#pandas
#matplotlib
#seaborn
#scikit-learn
#fastapi
#requests
#supabase
#streamlit
#python-dotenv
#ollama (local LLM client)
##

#Key Points#
#End-to-end pipeline:
#Data → Model → API → Script → LLM → Supabase → Streamlit
#Charts are saved uniquely in charts/ to avoid overwriting
#LLM generates narrative insights for storytelling
#Dashboard only consumes Supabase data (no API or LLM calls)
##