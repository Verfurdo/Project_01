# Szükséges könyvtárak importálása
import os
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from scipy import stats

# Adat betöltésére és elemzésére szolgáló függvény
def load_and_analyze_data():
    
    # Adatok betöltése egy CSV fájlból
    src_data = os.path.join("data", "stadat-nep0013-22.1.1.13-hu.csv")  # A CSV fájl elérési útjának meghatározása
    
    # Fájl létezésének ellenőrzése
    if not os.path.exists(src_data):
        print("A fájl nem létezik, kérlek ellenőrizd, vagy helyezd a fájlt a 'data' mappába!")
        return None
    
    # Adatok beolvasása, ha a fájl létezik
    df = pd.read_csv(               # a CSV fájl adatainak betöltése dataframe-be
        src_data,                   # A CSV fájl elérése
        sep=";",                    # Adatok elválasztója (pontosvessző)
        encoding="ISO-8859-1",      # Karakterkódolás, hogy speciális karaktereket is olvasson
        skipinitialspace=True,      # Szóközök eltávolítása az értékek körül
        skiprows=[0])                # Az első sor kihagyása (fejléccel van ellátva)
               
    # Tisztítás és átalakítás: a felesleges szóközök és vesszők cseréje
    df = df.replace(" ", "", regex=True)  # Szóközök eltávolítása
    df = df.replace(',', '.', regex=True)  # Vesszők cseréje pontokra, hogy a számok float típusúak lehessenek
    x = df.iloc[2:, 1].astype(float)  # X tengely adatainak kiválasztása és float típusra alakítása
    y = df.iloc[2:, 7].astype(float)  # Y tengely adatainak kiválasztása és float típusra alakítása
    
    # Logaritmikus transzformáció lineáris regresszió pontosabb illesztésére
    x_log = np.log(x)
    y_log = np.log(y)
    
    # Lineáris regresszió illesztése a logaritmikus adatokra
    model = LinearRegression()
    x_log_reshaped = x_log.values.reshape(-1, 1)  # Átalakítás a modell számára
    model.fit(x_log_reshaped, y_log)  # Modell illesztése
    y_pred_log = model.predict(x_log_reshaped)  # Előrejelzések készítése

    # Metrikák kiszámítása az illeszkedés minőségének értékeléséhez
    mse = mean_squared_error(y_log, y_pred_log)  # Négyzetes hibák átlaga (MSE)
    r2 = r2_score(y_log, y_pred_log)  # R² mutató, amely a modell magyarázóképességét méri

    return x_log, y_log, mse, r2  # Eredmények visszaadása

# Regressziós egyenes illesztésére szolgáló függvény
def get_regression_line(x_log, y_log):
    # Lineáris regresszió ismételt illesztése, hogy a regressziós egyenest előállítsuk
    model = LinearRegression()
    x_log_reshaped = x_log.values.reshape(-1, 1)
    model.fit(x_log_reshaped, y_log)
    return model.predict(x_log_reshaped)  # Az egyenes pontjainak visszaadása
