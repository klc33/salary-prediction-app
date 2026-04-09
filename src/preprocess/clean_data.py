import pandas as pd

# --- Load raw data ---
df = pd.read_csv("data/raw.csv")
print("Initial shape:", df.shape)

# --- Drop unnecessary columns ---
df = df.drop(columns=["salary", "salary_currency"])

# --- Handle missing values ---
df = df.dropna()

# --- Remove duplicates ---
df = df.drop_duplicates()

# --- Save cleaned dataset ---
df.to_csv("data/cleaned.csv", index=False)
print("Cleaned dataset saved to data/cleaned.csv")
print("Cleaned shape:", df.shape)