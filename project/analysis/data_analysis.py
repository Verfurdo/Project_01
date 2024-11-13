# data_analysis.py

import os
import pandas as pd

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
