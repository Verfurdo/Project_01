# line_plot.py - Vonaldiagram létrehozása a megadott adatok alapján

# Szükséges modulok importálása
import matplotlib.pyplot as plt  # Grafikonok és ábrák készítéséhez szükséges könyvtár

def vonaldiagram_letrehozasa(df):
    # Grafikon alapbeállítása
    fig, ax = plt.subplots(figsize=(6, 4))  # 6x4 méretű grafikon
    
    # Vonaldiagram kirajzolása 'Termelés' és 'Fogyasztás' adatok alapján
    ax.plot(df['Év'], df['Termelés'], label='Termelés', color='blue')   # Kék vonal a 'Termelés' adatokhoz
    ax.plot(df['Év'], df['Fogyasztás'], label='Fogyasztás', color='red')  # Piros vonal a 'Fogyasztás' adatokhoz
    
    # Y-tengely határainak beállítása az adatok alapján
    min_y = min(df['Termelés'].min(), df['Fogyasztás'].min())
    max_y = max(df['Termelés'].max(), df['Fogyasztás'].max())
    ax.set_ylim([min_y - 5, max_y + 5])  # Kis távolság hozzáadása az adatok fölé és alá a tisztább megjelenítéshez

    # Diagram címek és jelmagyarázat beállítása
    ax.set_title('Termelés és Fogyasztás')  # Grafikon cím
    ax.set_xlabel('Év')  # X tengely felirata
    ax.set_ylabel('Mennyiség (millió liter)')  # Y tengely felirata
    ax.legend()  # Jelmagyarázat hozzáadása

    # Rácsvonalak és jelmagyarázat bekapcsolása
    plt.grid(True)
    plt.legend()
    
    # Az elkészült grafikon visszaadása a Streamlit alkalmazás számára
    return fig  