# project.py - Főprogram a Streamlit alkalmazáshoz

# Szükséges modulok importálása
import streamlit as st  # Streamlit és a modulok importálása a megjelenítéshez
import pandas as pd
import os
import matplotlib.pyplot as plt
from streamlit_module import foprogramnak_vissza  

def foprogram():
    # Az alkalmazás címének beállítása
    st.title("Termelés és Fogyasztás Elemzése")

    # Lekérések a streamlit_module-ból
    vonaldiagram, pontdiagram = foprogramnak_vissza()
    
    # Két grafikon létrehozása 
    grafikon1, grafikon2 = st.columns(2)
    
    # Vonaldiagram megjelenítése az első grafikonon
    with grafikon1:
        st.subheader("Vonaldiagram")
        st.pyplot(vonaldiagram)
    
    # Pontdiagram megjelenítése a második grafikonon
    with grafikon2:
        st.subheader("Pontdiagram")
        st.pyplot(pontdiagram)
        
    # Excel fájl betöltése és megjelenítése
    # st.write("### Excel Fájl Betöltése és Megjelenítése")
    
    # Dinamikus elérési út meghatározása
    script_dir = os.path.dirname(os.path.abspath(__file__))
    xls_path = os.path.join(script_dir, 'data', 'statistical_analysis.xls')

    # Ellenőrzés futtatás előtt
    if not os.path.exists(xls_path):
        st.error(f"Az Excel fájl nem található: {xls_path}")
        st.stop()

    try:
        # Excel fájl beolvasása
        df = pd.read_excel(xls_path)
        # st.success("Az Excel fájl sikeresen betöltve!")
        
        # Oszlopnevek módosítása a megfelelő elnevezésekre
        df.columns = ['Oszlop', 'Metrika', 'Érték']  # Az oszlopokat átnevezzük
        
        # Statisztikai adatok táblázatos megjelenítése
        st.write("### Statisztikai Adatok")
        st.dataframe(df, use_container_width=True)
        
        # # Egy további grafikon készítése az Excel adatokból
        # st.write("### Átlagok Grafikonja")
        # if 'Metrika' in df.columns:
        #     df_avg = df[df['Metrika'] == 'Átlag']  # Csak az 'Átlag' metrikát használjuk
        #     st.write("Átlag adatok:", df_avg)

        #     fig, ax = plt.subplots(figsize=(10, 6))
        #     ax.bar(df_avg['Oszlop'], df_avg['Érték'], color='blue')
        #     ax.set_title('Átlagok oszloponként')
        #     ax.set_ylabel('Érték')
        #     ax.set_xlabel('Oszlop')
        #     st.pyplot(fig)
        # else:
        #     st.error("A 'Metrika' oszlop nem található az Excel fájlban.")
        #     st.stop()
    
    except Exception as e:
        st.error(f"Hiba történt az Excel fájl feldolgozása során: {str(e)}")
        st.stop()

# Csak akkor futtatja a foprogram() függvényt, ha ez a fájl a főprogram
if __name__ == "__main__":  # Ha a fájlt közvetlenül futtatjuk akkor nem fut le a foprogram() függvény
    foprogram()  # Ebben az esetben elindítja a foprogram() függvényt