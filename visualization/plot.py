# visualization/plot.py

# Szükséges könyvtárak importálása
import matplotlib.pyplot as plt  # Grafikonok és ábrák készítéséhez szükséges könyvtár
import numpy as np   # Numerikus műveletek és tömbkezelés

# Függvény a logaritmikus adatokat megjelenítő grafikon létrehozására, reziduálisokkal
def create_plot(x_log, y_log, y_pred_log, mse, r2):
    # Biztosítjuk, hogy x_log és y_log NumPy tömbökké legyenek konvertálva
    x_log = np.array(x_log)
    y_log = np.array(y_log)
    y_pred_log = np.array(y_pred_log)
    
    # Létrehozunk egy új ábrát és tengelyeket, 9x9-es méretben
    fig, ax = plt.subplots(figsize=(9, 9))
    
    # Az eredeti adatpontok megjelenítése (szétszórt pontokként)
    ax.scatter(x_log, y_log, s=60, alpha=0.7, edgecolors="k", c='green', label="Adatpontok")  # Pontok mérete, színe, átlátszósága, körvonala
    
    # Az adatpontokat összekötő vonal megjelenítése
    ax.plot(x_log, y_log, linestyle='-', color='blue', linewidth=1.5, label="Adatpontok közötti vonal")
    
    # Regressziós egyenes megjelenítése
    ax.plot(x_log, y_pred_log, color="red", lw=2.5, label="Regressziós egyenes")
    
    # Reziduálisok megjelenítése: fekete színű, szaggatott vonalak az adatpontok és a regressziós egyenes között
    for i in range(len(x_log)):
        ax.plot([x_log[i], x_log[i]], [y_log[i], y_pred_log[i]], color='black', linestyle='--', lw=1, label="Reziduálisok" if i == 0 else "")
    
    # MSE és R² értékek kiírása a grafikonon
    ax.text(0.05, 0.95, f'MSE: {mse:.4f}\nR²: {r2:.4f}', transform=ax.transAxes, 
            fontsize=12, verticalalignment='top', bbox=dict(facecolor='white', alpha=0.8))

    # Cím és tengelyfeliratok beállítása
    ax.set_title('Hazai Sörfogyasztás összesen (logaritmikus skálán)')  # Grafikon cím
    ax.set_xlabel('Termelés (log millió liter)')  # X tengely felirata
    ax.set_ylabel('Fogyasztás (log millió liter)')  # Y tengely felirata
    
    # Rácsvonalak hozzáadása a jobb átláthatóság érdekében
    ax.grid(True)

    # Jelmagyarázat hozzáadása
    ax.legend()

    # Az elkészült grafikon (fig) visszaadása a Streamlit alkalmazás számára
    return fig
