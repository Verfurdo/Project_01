# scatter_plot.py - Pontdiagram készítése lineáris regressziós illesztéssel

# Szükséges könyvtárak importálása
import matplotlib.pyplot as plt  # Grafikonok és ábrák készítéséhez szükséges könyvtár
from sklearn.linear_model import LinearRegression  # Lineáris regressziós modell importálása
from sklearn.metrics import r2_score # Modell értékeléséhez szükséges metrika
import numpy as np  # Numerikus műveletek és tömbkezelés

def pontdiagram_letrehozasa(df):
    # Grafikon létrehozása
    fig, ax = plt.subplots(figsize=(6, 4))  # 6x4 méretű grafikon
    
    # Szóráspontok kirajzolása az 'Termelés' és 'Fogyasztás' adatok alapján
    ax.scatter(df['Termelés'], df['Fogyasztás'], color='red', label='Fogyasztás vs Termelés')
    
    # Lineáris regressziós modell létrehozása és illesztése az adatokhoz
    X = df['Termelés'].values.reshape(-1, 1)  # Átalakítás a modell számára
    y = df['Fogyasztás'].values
    model = LinearRegression()
    model.fit(X, y)  # Modell illesztése
    y_pred = model.predict(X)  # Előrejelzett értékek kiszámítása

    # Regressziós egyenes illesztése
    ax.plot(df['Termelés'], y_pred, color='blue', label='Lineáris regressziós egyenes')

    # Reziduálisok kirajzolása: pontok és az illesztett egyenes közötti szagatott vonalak
    for xi, yi, yfi in zip(df['Termelés'], y, y_pred):
        ax.vlines(xi, ymin=min(yi, yfi), ymax=max(yi, yfi), color='green', linestyle='dotted', label='Reziduálisok' if xi == df['Termelés'].iloc[0] else "")

    # R² érték kiszámítása és megjelenítése
    r2 = r2_score(y, y_pred)  # R² mutató, amely a modell illeszkedésének pontosságát méri, 1.0 a tökéletes illeszkedés
    metrics_text = f'R² = {r2:.2f}'
    ax.text(0.95, 0.05, metrics_text, transform=ax.transAxes, fontsize=10,
            verticalalignment='bottom', horizontalalignment='right',
            bbox=dict(facecolor='white', alpha=0.8, edgecolor='gray'))

    # Diagram címek, tengelyfeliratok és jelmagyarázat beállítása
    ax.set_title('Termelés és Fogyasztás')  # Grafikon cím
    ax.set_xlabel('Termelés')  # X tengely felirata
    ax.set_ylabel('Fogyasztás')  # Y tengely felirata
    ax.legend()  # Jelmagyarázat hozzáadása

    plt.grid(True)  # Rácsvonalak bekapcsolása
    
    # Az elkészült grafikon visszaadása a Streamlit alkalmazás számára
    return fig  
