# project.py - Főprogram a Streamlit alkalmazáshoz

# Szükséges modulok importálása
import streamlit as st  # Streamlit és a modulok importálása a megjelenítéshez
from streamlit_module import foprogramnak_vissza  

def foprogram():
    # Az alkalmazás címének beállítása
    st.title("Fogyasztás és Termelés Elemzése")

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

# Csak akkor futtatja a foprogram() függvényt, ha ez a fájl a főprogram
if __name__ == "__main__":  # Ha a fájlt közvetlenül futtatjuk akkor nem fut le a foprogram() függvény
    foprogram()  # Ebben az esetben elindítja a foprogram() függvényt