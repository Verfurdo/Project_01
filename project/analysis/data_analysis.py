# data_analysis.py - Adatbetöltés és előkészítés a regressziós és statisztikai elemzéshez

# Szükséges modulok importálása
import os  # Operációs rendszerrel kapcsolatos műveletekhez (fájlok elérési útjának kezelése)
import pandas as pd  # Adatok beolvasása és átalakítása DataFrame-ek segítségével

def adatok_betoltese_elokeszitese():
    # Adatok elérési útjának meghatározása
    script_dir = os.path.dirname(os.path.abspath(__file__))  # Megadja az aktuális fájl könyvtárát
    data_path = os.path.join(script_dir, '..', 'data', 'stadat-nep0013-22.1.1.13-hu.csv')  # A CSV fájl elérési útja

    # Fájl létezésének ellenőrzése
    if not os.path.exists(data_path):
        raise FileNotFoundError(f"A fájl nem létezik, kérlek ellenőrizd, vagy helyezd a fájlt a 'data' mappába! {data_path}")

    # Adatok betöltése és előkészítése
    df = pd.read_csv(data_path,  # a CSV fájl adatainak betöltése DataFrame-be
        sep=";",   # Adatok elválasztója (pontosvessző)
        encoding="ISO-8859-1") # Karakterkódolás, hogy speciális karaktereket is olvasson
    
    # Tisztítás és átalakítás: a felesleges szóközök és vesszők cseréje
    df = df.replace(" ", "", regex=True)  # Szóközök eltávolítása
    df = df.replace(',', '.', regex=True)  # Vesszők cseréje pontokra, hogy a számok float típusúak lehessenek
    df['Termelés'] = pd.to_numeric(df['Termelés'], errors='coerce')  # 'Termelés' oszlop átalakítása numerikus típussá, hibás értékeket NaN-né alakítva
    df['Fogyasztás'] = pd.to_numeric(df['Fogyasztás'], errors='coerce')  # 'Fogyasztás' oszlop átalakítása numerikus típussá, hibás értékeket NaN-né alakítva


    return df  # Előkészített adatok visszaadása
