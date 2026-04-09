import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import pickle



# Load data
df = pd.read_csv("data/cleaned.csv")

# Features and target
y = df['salary_in_usd']
X = df[['experience_level', 'employment_type', 'job_title', 
        'employee_residence', 'company_size', 'remote_ratio']]

# One-Hot Encode categorical features
X = pd.get_dummies(X, columns=['experience_level', 'employment_type', 
                               'job_title', 'employee_residence', 'company_size'],
                   drop_first=True)

print("Shape after encoding:", X.shape)


X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


rf_model = RandomForestRegressor(n_estimators=200, max_depth=15, random_state=42)
rf_model.fit(X_train, y_train)

y_pred_rf = rf_model.predict(X_test)

mae_rf = mean_absolute_error(y_test, y_pred_rf)
r2_rf = r2_score(y_test, y_pred_rf)

print(f"Random Forest MAE: {mae_rf:.2f}, R2: {r2_rf:.2f}")

with open("models/model.pkl", "wb") as f:
    pickle.dump(rf_model, f)  # or rf_model if you use Random Forest