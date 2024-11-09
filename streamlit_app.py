# Szükséges modulok importálása
import streamlit as st
from analysis import regression_analysis  # Adatok elemzése
from visualization import plot  # Grafikon megjelenítése

# Streamlit alkalmazás futtatásáért felelős függvény
def run_streamlit_app():
    # Alkalmazás címének beállítása
    st.title("Fogyasztás és Termelés Elemzése")
    
    # Adatok betöltése és ellenőrzés
    result = regression_analysis.load_and_analyze_data()
    if result is None:
        st.error("A szükséges CSV fájl nem található. Helyezd a fájlt a 'data' mappába, és próbáld újra.")
        return  # Megszakítja a végrehajtást, ha a fájl nem található
    
    # Elemzési eredmények megjelenítése
    x_log, y_log, mse, r2 = result
    
    # Adatok betöltése és elemzése a regression_analysis modul segítségével
    y_pred_log = regression_analysis.get_regression_line(x_log, y_log)
    
    # Grafikon létrehozása az összes szükséges paraméterrel kiírjuk a fontosabb metrikákat az MSE-t és az R2-t
    fig = plot.create_plot(x_log, y_log, y_pred_log, mse, r2)
    st.pyplot(fig)
