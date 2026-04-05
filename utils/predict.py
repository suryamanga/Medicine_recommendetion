import pickle
import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

model = pickle.load(open(os.path.join(BASE_DIR, "model/model.pkl"), "rb"))
symptoms_list = pickle.load(open(os.path.join(BASE_DIR, "model/symptoms.pkl"), "rb"))

def predict_disease(symptoms):
    input_vector = [0] * len(symptoms_list)

    for s in symptoms:
        if s in symptoms_list:
            input_vector[symptoms_list.index(s)] = 1

    input_df = pd.DataFrame([input_vector], columns=symptoms_list)

    return model.predict(input_df)[0]