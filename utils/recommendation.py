import pandas as pd
import os

# Load dataset safely
if os.path.exists("data/drug_review.csv"):
    drug_df = pd.read_csv("data/drug_review.csv")
else:
    drug_df = pd.DataFrame()

# Rule-based fallback
medicine_map = {
    'Fungal infection': ['Fluconazole', 'Clotrimazole', 'Terbinafine'],
    'Allergy': ['Cetirizine', 'Loratadine', 'Diphenhydramine'],
    'Diabetes': ['Metformin', 'Insulin', 'Glibenclamide'],
    'Hypertension': ['Amlodipine', 'Enalapril', 'Losartan'],
    'Migraine': ['Sumatriptan', 'Ibuprofen', 'Paracetamol'],
    'Malaria': ['Chloroquine', 'Artemether', 'Primaquine'],
    'Typhoid': ['Ciprofloxacin', 'Azithromycin', 'Ceftriaxone'],
    'Hepatitis E': ['Rest', 'IV fluids', 'Supportive care'],
     'Hepatitis A'                             : ['Rest', 'IV fluids', 'Supportive care'],
    'Hepatitis B'                             : ['Tenofovir', 'Entecavir', 'Interferon'],
    'Hepatitis C'                             : ['Sofosbuvir', 'Ribavirin', 'Daclatasvir'],
    'Hepatitis D'                             : ['Interferon alpha', 'Supportive care'],
    'Hepatitis E'                             : ['Rest', 'IV fluids', 'Supportive care'],
    'Alcoholic hepatitis'                     : ['Corticosteroids', 'Pentoxifylline', 'Vitamin B'],
    'Tuberculosis'                            : ['Isoniazid', 'Rifampicin', 'Pyrazinamide'],
    'Common Cold'                             : ['Paracetamol', 'Cetirizine', 'Vitamin C'],
    'Pneumonia'                               : ['Amoxicillin', 'Azithromycin', 'Levofloxacin'],
    'Dimorphic hemmorhoids(piles)'            : ['Sitz bath', 'Hydrocortisone cream', 'Fiber supplements'],
    'Heart attack'                            : ['Aspirin', 'Nitroglycerin', 'Clopidogrel'],
    'Varicose veins'                          : ['Compression stockings', 'Sclerotherapy'],
    'Hypothyroidism'                          : ['Levothyroxine'],
    'Hyperthyroidism'                         : ['Carbimazole', 'Propylthiouracil', 'Beta-blockers'],
    'Hypoglycemia'                            : ['Glucose tablets', 'Dextrose IV', 'Glucagon'],
    'Osteoarthristis'                         : ['Ibuprofen', 'Paracetamol', 'Glucosamine'],
    'Arthritis'                               : ['Methotrexate', 'Ibuprofen', 'Hydroxychloroquine'],
    '(vertigo) Paroymsal  Positional Vertigo' : ['Epley maneuver', 'Meclizine', 'Betahistine'],
    'Acne'                                    : ['Benzoyl peroxide', 'Clindamycin gel', 'Adapalene'],
    'Urinary tract infection'                 : ['Nitrofurantoin', 'Ciprofloxacin', 'Trimethoprim'],
    'Psoriasis'                               : ['Methotrexate', 'Cyclosporine', 'Betamethasone'],
    'Impetigo'                                : ['Mupirocin', 'Amoxicillin', 'Cephalexin'],
}


def recommend_medicine(disease):

    # ✅ Step 1: Try dataset (if available)
    if not drug_df.empty:
        result = drug_df[
            drug_df['condition'].str.lower().str.contains(disease.lower())
        ]
        
        result = result.sort_values(by='rating', ascending=False)
        
        if not result.empty:
            return result[['drugName']].head(5)['drugName'].tolist()

    # ✅ Step 2: Fallback to rule-based
    return medicine_map.get(disease, ["Consult doctor"])