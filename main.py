import numpy as np
import pandas as pd

# -------------------------------------------------------------
# STEP 1: Create a Sample Dataset (For Demonstration Purposes)
# -------------------------------------------------------------
raw_data = {
    "Patient_ID":,
    "Age": [45, 29, np.nan, 61, 53, 29, 72, 41],
    "Gender": ["Female", "Male", "Female", "Male", "Female", "Male", np.nan, "Female"],
    "Disease": ["Diabetes", "Flu", "Hypertension", "Diabetes", "Asthma", "Flu", "Hypertension", "Diabetes"],
    "Medication": ["Metformin", "Oseltamivir", "Lisinopril", "Metformin", "Albuterol", "Oseltamivir", "Amlodipine", "Metformin"],
    "Dosage": ["500mg", "75mg", "10mg", "1000mg", "2 puffs", "75mg", "5mg", "500mg"]
}

df = pd.DataFrame(raw_data)
print("=== Initial Raw Dataset ===")
print(df, "\n")

# -------------------------------------------------------------
# STEP 2: Explore Dataset & Identify Column Types
# -------------------------------------------------------------
print("=== Column Data Types ===")
print(df.dtypes, "\n")

# -------------------------------------------------------------
# STEP 3: Data Cleaning (Handling Duplicates & Missing Values)
# -------------------------------------------------------------
duplicate_count = df.duplicated().sum()
df = df.drop_duplicates()
print(f"Removed {duplicate_count} duplicate row(s).\n")

median_age = df["Age"].median()
df["Age"] = df["Age"].fillna(median_age)
df["Gender"] = df["Gender"].fillna("Unknown")

print("=== Cleaned Dataset ===")
print(df, "\n")

# -------------------------------------------------------------
# STEP 4: Basic Data Analysis
# -------------------------------------------------------------
total_patients = df["Patient_ID"].nunique()
disease_counts = df["Disease"].value_counts()
common_disease = disease_counts.index[0]
common_disease_count = disease_counts.iloc[0]
average_age = df["Age"].mean()

print("=== Analysis Results ===")
print(f"Total Unique Patients: {total_patients}")
print(f"Average Patient Age:   {average_age:.1f} years old")
print(f"Most Common Disease:   {common_disease} ({common_disease_count} cases)")
