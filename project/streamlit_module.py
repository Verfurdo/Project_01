# streamlit_module.py - Vizualizációk és elemzések modul Streamlit alkalmazáshoz

# Szükséges könyvtárak importálása
import numpy as np  #  Numerikus műveletek és tömbkezelés
import streamlit as st  # Streamlit komponensek megjelenítéséhez
from analysis.data_analysis import load_and_prepare_data  # Adatok betöltése és előkészítése
from analysis.statistical_analysis import save_statistical_analysis  # Statisztikai elemzés mentése
from visualization.line_plot import create_line_plot  # Vonaldiagram létrehozása
from visualization.scatter_plot import create_scatter_plot  # Pontdiagram létrehozása

# Fő függvény a vizualizációk létrehozására és az elemzések elvégzésére
def get_visualizations():
    
    # Adatok betöltése és előkészítése a data_analysis modulból
    try:
        df = load_and_prepare_data()
    except FileNotFoundError:
        # Hibaüzenet megjelenítése, ha a fájl nem található
        st.error("A szükséges CSV fájl nem található. Helyezd a fájlt a 'data' mappába, és próbáld újra.")
        st.stop()  # Streamlit futásának megszakítása

    # Statisztikai elemzések elvégzése és eredmények mentése CSV fájlba
    save_statistical_analysis(df)

    # Vonaldiagram és pontdiagram létrehozása a megadott adatok alapján
    line_plot = create_line_plot(df)  # Vonaldiagram készítése az adatok alapján
    scatter_plot = create_scatter_plot(df)  # Pontdiagram készítése az adatok alapján

    # A kész diagramok visszaadása a fő alkalmazás számára
    return line_plot, scatter_plot
