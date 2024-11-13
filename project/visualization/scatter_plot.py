import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
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

    # Reziduálisok ábrázolása (függőleges szaggatott vonalak az eredeti pontok és az illesztett egyenes között)
    for xi, yi, yfi in zip(df['Termelés'], y, y_pred):
        ax.vlines(xi, ymin=min(yi, yfi), ymax=max(yi, yfi), color='green', linestyle='dotted', label='Reziduálisok' if xi == df['Termelés'].iloc[0] else "")

    # R² érték kiszámítása
    r2 = r2_score(y, y_pred)

    # R² érték kiírása a grafikon jobb alsó sarkában fehér háttérrel
    metrics_text = f'R² = {r2:.2f}'
    ax.text(0.95, 0.05, metrics_text, transform=ax.transAxes, fontsize=10,
            verticalalignment='bottom', horizontalalignment='right',
            bbox=dict(facecolor='white', alpha=0.8, edgecolor='gray'))

    # Diagram beállítása
    ax.set_title('Pontdiagram: Termelés és Fogyasztás')
    ax.set_xlabel('Termelés')
    ax.set_ylabel('Fogyasztás')
    ax.legend()  # Jelmagyarázat bekapcsolása a tengelyekhez kötve

    plt.grid(True)  # Rácsvonalak bekapcsolása

    return fig
