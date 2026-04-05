import pandas as pd
import numpy as np
import pickle
from sklearn.ensemble import RandomForestClassifier

# Load dataset
df = pd.read_csv("data/dataset.csv")

# 🔥 Convert symptoms (text → list)
symptom_cols = df.columns[1:]  # skip Disease

# Create empty dataframe
all_symptoms = set()

# Collect all symptoms
for col in symptom_cols:
    all_symptoms.update(df[col].dropna().values)

all_symptoms = list(all_symptoms)

# Create new binary dataframe
new_df = pd.DataFrame(0, index=np.arange(len(df)), columns=all_symptoms)
new_df["Disease"] = df["Disease"]

# Fill 1s
for i in range(len(df)):
    for col in symptom_cols:
        symptom = df.loc[i, col]
        if pd.notna(symptom):
            new_df.at[i, symptom] = 1

# Split
X = new_df.drop("Disease", axis=1)
y = new_df["Disease"]

# Train
model = RandomForestClassifier()
model.fit(X, y)

# Save model + columns
pickle.dump(model, open("model/model.pkl", "wb"))
pickle.dump(X.columns.tolist(), open("model/symptoms.pkl", "wb"))

print("✅ Model trained successfully!")