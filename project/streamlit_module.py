# streamlit_module.py - Elemzések és diagramok modul függvények a főprogramnak

from analysis.data_analysis import adatok_betoltese_elokeszitese  # Adatok betöltése és előkészítése függvény meghívása
from analysis.data_analysis import statisztikai_elemzes_mentese  # Statisztikai elemzés mentése függvény meghívása
from visualization.line_plot import vonaldiagram_letrehozasa  # Vonaldiagram létrehozása függvény meghívása
from visualization.scatter_plot import pontdiagram_letrehozasa  # Pontdiagram létrehozása függvény meghívása

def adatok_elemzese():
    """Betölti és elemzi az adatokat / statisztikai számításokat mentése"""   
    df = adatok_betoltese_elokeszitese()  # Adatok betöltése
    statisztikai_elemzes_mentese(df)  # Statisztikai számítások mentése
    return df  

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
