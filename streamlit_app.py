# Szükséges modulok importálása
import streamlit as st
from analysis import regression_analysis  # Adatok elemzése
from visualization import plot  # Grafikon megjelenítése

# Streamlit alkalmazás futtatásáért felelős függvény
def run_streamlit_app():
    # Alkalmazás címének beállítása
    st.title("Hazai Fogyasztás és Termelés Elemzése")

    # Adatok betöltése és elemzése a regression_analysis modul segítségével
    x_log, y_log, mse, r2 = regression_analysis.load_and_analyze_data()

    # Elemzési eredmények megjelenítése grafikonon
    fig = plot.create_plot(x_log, y_log, regression_analysis.get_regression_line(x_log, y_log))
    st.pyplot(fig)

    # Kiírjuk a fontosabb metrikákat, például az MSE-t és az R2-t
    st.write(f"Mean Squared Error (MSE): {mse}")
    st.write(f"R-squared (R2): {r2}")
