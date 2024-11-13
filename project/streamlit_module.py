# streamlit_module.py

import numpy as np  # NumPy importálása az elemzéshez, ha szükséges
from analysis.data_analysis import load_and_prepare_data, save_statistical_analysis  # Pontosított import
from visualization.line_plot import create_line_plot
from visualization.scatter_plot import create_scatter_plot

def get_visualizations():
    df = load_and_prepare_data()

    # Statisztikai elemzés és mentés CSV-be
    save_statistical_analysis(df)

    # Vonaldiagram és pontdiagram létrehozása a nyers adatokkal
    line_plot = create_line_plot(df)
    scatter_plot = create_scatter_plot(df)  # A pontdiagram a nyers adatokkal dolgozik

    return line_plot, scatter_plot
