# visualization/scatter_plot.py

import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np

def create_scatter_plot(df):
    fig, ax = plt.subplots(figsize=(6, 4))  # Méret beállítása másfélszer nagyobbra
    
    # Szóráspontok kirajzolása
    ax.scatter(df['Termelés'], df['Fogyasztás'], color='red', label='Fogyasztás vs Termelés')
    
    # Lineáris regresszió illesztése
    X = df['Termelés'].values.reshape(-1, 1)
    y = df['Fogyasztás'].values
    model = LinearRegression()
    model.fit(X, y)
    y_pred = model.predict(X)

    # Regressziós egyenes kirajzolása
    ax.plot(df['Termelés'], y_pred, color='blue', label='Lineáris regressziós egyenes')
    
    # Diagram beállítása
    ax.set_title('Pontdiagram: Termelés és Fogyasztás (Lineáris Regresszióval)')
    ax.set_xlabel('Termelés')
    ax.set_ylabel('Fogyasztás')
    ax.legend()

    return fig
