# analysis/data_analysis.py

import os
import pandas as pd
import numpy as np

def load_and_prepare_data():
    # CSV fájl betöltése
    script_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(script_dir, '..', 'data', 'stadat-nep0013-22.1.1.13-hu.csv')

    if not os.path.exists(data_path):
        raise FileNotFoundError(f"A fájl nem található: {data_path}")

    # Adatok betöltése és tisztítása
    df = pd.read_csv(data_path, sep=";", encoding="ISO-8859-1")
    df = df.replace(" ", "", regex=True)
    df = df.replace(',', '.', regex=True)
    df['Termelés'] = pd.to_numeric(df['Termelés'], errors='coerce')
    df['Fogyasztás'] = pd.to_numeric(df['Fogyasztás'], errors='coerce')

    return df

def save_statistical_analysis(df):
    # Statisztikai mutatók kiszámítása
    stat_analysis = {
        'Termelés_átlag': [df['Termelés'].mean()],
        'Termelés_szórás': [df['Termelés'].std()],
        'Fogyasztás_átlag': [df['Fogyasztás'].mean()],
        'Fogyasztás_szórás': [df['Fogyasztás'].std()]
    }

    stat_df = pd.DataFrame(stat_analysis)

    # Eredmények mentése a data mappába
    stat_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'statistical_analysis.csv')
    stat_df.to_csv(stat_path, index=False, encoding="utf-8")
    print(f"Statisztikai elemzés mentve a {stat_path} fájlba.")
