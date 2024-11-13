# visualization/line_plot.py

import matplotlib.pyplot as plt

def create_line_plot(df):
    fig, ax = plt.subplots(figsize=(6, 4))  # Nagyobb méret beállítása
    
    # Vonaldiagram létrehozása az évszámok használatával az x tengelyen
    ax.plot(df['Év'], df['Termelés'], label='Termelés', color='blue')   # Kék vonal a Termelés adatokhoz
    ax.plot(df['Év'], df['Fogyasztás'], label='Fogyasztás', color='red')  # Piros vonal a Fogyasztás adatokhoz
    
    # Y tengely beállítása az alsó értéktől indulva
    min_y = min(df['Termelés'].min(), df['Fogyasztás'].min())
    max_y = max(df['Termelés'].max(), df['Fogyasztás'].max())
    ax.set_ylim([min_y - 5, max_y + 5])  # Kis eltérés hozzáadása a tisztább megjelenítéshez
    
    # Diagram beállítása
    ax.set_title('Vonaldiagram: Termelés és Fogyasztás')
    ax.set_xlabel('Év')
    ax.set_ylabel('Mennyiség (millió liter)')
    ax.legend()

    return fig
