# streamlit_module.py - Vizualizációk és elemzések modul Streamlit alkalmazáshoz

import streamlit as st  # Streamlit komponensek megjelenítéséhez
from analysis.data_analysis import adatok_betoltese_elokeszitese  # Adatok betöltése és előkészítése
from analysis.statistical_analysis import statisztikai_elemzes_mentese  # Statisztikai elemzés mentése
from visualization.line_plot import vonaldiagram_letrehozasa  # Vonaldiagram létrehozása
from visualization.scatter_plot import pontdiagram_letrehozasa  # Pontdiagram létrehozása

def adatok_elemzese():
    """Betölti és elemzi az adatokat, és statisztikai eredményt elmenti"""
    try:
        df = adatok_betoltese_elokeszitese()  # Adatok betöltése
    except FileNotFoundError:
        st.error("A szükséges CSV fájl nem található. Helyezd a fájlt a 'data' mappába, és próbáld újra.")
        st.stop()  # Streamlit futásának megszakítása, ha a fájl hiányzik
    
    statisztikai_elemzes_mentese(df)  # Statisztikai elemzés mentése
    return df  # Előkészített adatkeret visszaadása

def diagramok_letrehozasa(df):
    """Létrehozza a vonal- és pontdiagramot az előkészített adatokból."""
    vonaldiagram = vonaldiagram_letrehozasa(df)  # Vonaldiagram létrehozása
    pontdiagram = pontdiagram_letrehozasa(df)  # Pontdiagram létrehozása
    return vonaldiagram, pontdiagram  # Diagramok visszaadása

def foprogramnak_vissza():
    """Elvégzi az elemzést és a vizualizációkat, és visszaadja azokat főprogramnak."""
    df = adatok_elemzese()  # Adatok elemzése
    vonaldiagram, pontdiagram = diagramok_letrehozasa(df)  # Diagramok létrehozása
    return vonaldiagram, pontdiagram  # Diagramok visszaadása a fő alkalmazáshoz
