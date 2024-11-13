import pandas as pd
import numpy as np
import os

def save_statistical_analysis(df, output_dir='data'):
    # Ellenőrizzük, hogy a 'data' mappa létezik-e, és ha nem, létrehozzuk
    full_output_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', output_dir)
    os.makedirs(full_output_dir, exist_ok=True)

    # Lista az összes statisztikai adat tárolására külön sorokban
    rows = []
    for column in df.columns:
        if pd.api.types.is_numeric_dtype(df[column]):
            # Minden statisztikai mutatót külön sorban tárolunk
            rows.append({'Oszlop': column, 'Metrika': 'Átlag', 'Érték': np.mean(df[column])})
            rows.append({'Oszlop': column, 'Metrika': 'Medián', 'Érték': np.median(df[column])})
            rows.append({'Oszlop': column, 'Metrika': 'Szórás', 'Érték': np.std(df[column])})
            rows.append({'Oszlop': column, 'Metrika': 'Variancia', 'Érték': np.var(df[column])})
            rows.append({'Oszlop': column, 'Metrika': 'Minimum', 'Érték': np.min(df[column])})
            rows.append({'Oszlop': column, 'Metrika': 'Maximum', 'Érték': np.max(df[column])})

    # DataFrame létrehozása az összes statisztikai mutatóval
    stats_df = pd.DataFrame(rows)

    # Eredmények mentése egyetlen CSV fájlba, soronkénti elrendezéssel
    output_path = os.path.join(full_output_dir, 'statistical_analysis.csv')
    stats_df.to_csv(output_path, index=False, encoding='utf-8-sig')
    print(f"Statisztikai elemzés mentve a következő fájlba: {output_path}")
