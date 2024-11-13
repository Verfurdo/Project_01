# statistical_analysis.py - Statisztikai mutatók számítása és mentése CSV fájlba

# Szükséges modulok importálása
import pandas as pd  # Adatok beolvasása és átalakítása DataFrame-ek segítségével
import numpy as np  # Numerikus műveletek és tömbkezelés
import os  # Operációs rendszerrel kapcsolatos műveletekhez (fájlok elérési útjának kezelése)

def statisztikai_elemzes_mentese(df, output_dir='data'):
    # Ellenőrizzük, hogy a 'data' mappa létezik-e
    full_output_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', output_dir)
    os.makedirs(full_output_dir, exist_ok=True)

    # Lista az összes statisztikai adat tárolására
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

    # Eredmények mentése egyetlen CSV fájlba
    output_path = os.path.join(full_output_dir, 'statistical_analysis.csv')
    stats_df.to_csv(output_path, index=False, encoding='utf-8-sig')
    print(f"Statisztikai elemzés mentve a következő fájlba: {output_path}")
