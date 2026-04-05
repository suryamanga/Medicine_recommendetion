import pandas as pd

interaction_df = pd.read_csv("data/drug_interactions.csv")

def check_interaction(drugs):
    warnings = []
    
    for i in range(len(drugs)):
        for j in range(i+1, len(drugs)):
            d1, d2 = drugs[i], drugs[j]
            
            check = interaction_df[
                ((interaction_df['drug1'] == d1) & (interaction_df['drug2'] == d2)) |
                ((interaction_df['drug1'] == d2) & (interaction_df['drug2'] == d1))
            ]
            
            if not check.empty:
                warnings.append(f"{d1} + {d2} → Interaction")
    
    return warnings