# analysis/regression_analysis.py  -  Adatok elemzése modul

# Szükséges könyvtárak importálása
import os      # Operációs rendszerrel kapcsolatos műveletekhez (fájlok elérési útjának kezelése)
import pandas as pd  # Adatok beolvasása és átalakítása DataFrame-ek segítségével
import numpy as np  # Numerikus műveletek és tömbkezelés
from sklearn.linear_model import LinearRegression  # Lineáris regressziós modell importálása
from sklearn.metrics import mean_squared_error, r2_score  # Modell értékeléséhez szükséges metrikák
from scipy import stats  # Statisztikai műveletekhez (kiugró értékek szűrésére)

# Adat betöltésére és elemzésére szolgáló függvény
def adatok_betoltese_elemzese():
    
    # Abszolút elérési út meghatározása majd az adatok betöltése a CSV fájlból
    script_dir = os.path.dirname(os.path.abspath(__file__))  # Megadja az aktuális fájl könyvtárát
    src_data = os.path.join(script_dir, '..', 'data', 'stadat-nep0013-22.1.1.13-hu.csv')  # A CSV fájl elérési útja  
    
    # Fájl létezésének ellenőrzése
    if not os.path.exists(src_data):
        print("A fájl nem létezik, kérlek ellenőrizd, vagy helyezd a fájlt a 'data' mappába!")
        return None
    
    # Adatok beolvasása ha a fájl megtalálható
    df = pd.read_csv(               # a CSV fájl adatainak betöltése DataFrame-be
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
    
    # Kiugró értékek szűrése a Z-score alapján
    x_z_scores = np.abs(stats.zscore(x))
    y_z_scores = np.abs(stats.zscore(y))
    threshold = 3  # Kiugró érték küszöbe

    # Csak azokat az adatokat tartjuk meg, ahol mindkét Z-score érték kisebb a küszöbnél
    mask = (x_z_scores < threshold) & (y_z_scores < threshold)
    x_filtered = x[mask]
    y_filtered = y[mask]
    
    # Logaritmikus transzformáció alkalmazása a lineáris regresszió pontosabb illesztésére
    x_log = np.log(x_filtered)
    y_log = np.log(y_filtered)
    
    # Lineáris regresszió illesztése
    model = LinearRegression()
    x_log_reshaped = x_log.values.reshape(-1, 1)  # Átalakítás a modell számára
    model.fit(x_log_reshaped, y_log)  # Modell illesztése
    y_pred_log = model.predict(x_log_reshaped)  # Előrejelzések készítése

    # Metrikák kiszámítása az illeszkedés minőségének értékeléséhez
    mse = mean_squared_error(y_log, y_pred_log)  # Négyzetes hibák átlaga (MSE), akkor a legjobb, ha az értéke minél közelebb van a 0-hoz. 
    r2 = r2_score(y_log, y_pred_log)  # R² mutató, amely a modell illeszkedésének pontosságát méri, 1.0 a tökéletes illeszkedés

    return x_log, y_log, mse, r2  # Eredmények visszaadása

#  Lineáris regresszió ismételt illesztése egy külön függvényben a későbbi meghívásra
def regresszios_egyenes_illesztese(x_log, y_log):
    model = LinearRegression()
    x_log_reshaped = x_log.values.reshape(-1, 1)  # Átalakítás a modell számára
    model.fit(x_log_reshaped, y_log)  # Modell illesztése
    return model.predict(x_log_reshaped)  # Az egyenes pontjainak visszaadása
