# Szükséges könyvtárak importálása
import matplotlib.pyplot as plt
import numpy as np

# Függvény a logaritmikus adatokat megjelenítő grafikon létrehozására
def create_plot(x_log, y_log, y_pred_log):
    # Létrehozunk egy új ábrát és tengelyeket, 9x9-es méretben
    fig, ax = plt.subplots(figsize=(9, 9))
    
    # Az eredeti adatpontok megjelenítése (szétszórt pontokként)
    ax.scatter(x_log, y_log, s=60, alpha=0.7, edgecolors="k")  # Pontok mérete, átlátszósága, körvonala
    
    # Az adatpontokat összekötő vonal megjelenítése
    ax.plot(x_log, y_log, linestyle='-', color='blue', linewidth=1.5)  # Kék vonal
    
    # Regressziós egyenes megjelenítése, amelyet a modell illesztett az adatokra
    ax.plot(x_log, y_pred_log, color="k", lw=2.5)  # Fekete vonal vastagabb vonalvastagsággal
    
    # Cím és tengelyfeliratok beállítása
    ax.set_title('Hazai fogyasztás összesen (logaritmikus skálán)')  # Grafikon cím
    ax.set_xlabel('Termelés (millió liter)')  # X tengely felirata
    ax.set_ylabel('Fogyasztás (millió liter)')  # Y tengely felirata
    
    # Rácsvonalak hozzáadása a jobb átláthatóság érdekében
    ax.grid(True)
    
    # Az elkészült grafikon (fig) visszaadása a Streamlit alkalmazás számára
    return fig
