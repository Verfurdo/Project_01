# Szükséges modulok importálása
import streamlit as st  # Webalkalmazás készítéséhez, adatvizualizációhoz
from analysis import regression_analysis  # Adatok elemzése
from visualization import plot  # Grafikon megjelenítése

# Streamlit alkalmazás futtatásáért felelős függvény
def streamlit_futtatasa():
    # Alkalmazás címének beállítása
    st.title("Fogyasztás és Termelés Elemzése")
    
    # Adat betöltésére és elemzésére szolgáló függvény meghívása
    result = regression_analysis.adatok_betoltese_elemzese()
    if result is None:
        st.error("A szükséges CSV fájl nem található. Helyezd a fájlt a 'data' mappába, és próbáld újra.")
        return  # Megszakítja a végrehajtást, ha a fájl nem található
    
    # Elemzési eredmények megjelenítése
    x_log, y_log, mse, r2 = result
    
    # Regressziós egyenes illesztése függvény meghívása
    y_pred_log = regression_analysis.regresszios_egyenes_illesztese(x_log, y_log)
    
    # Grafikon létrehozása függvény meghívása
    fig = plot.grafikon_keszitese(x_log, y_log, y_pred_log, mse, r2)
    st.pyplot(fig)
