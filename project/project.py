# project.py - Főprogram a Streamlit alkalmazáshoz

# Szükséges modulok importálása
import streamlit as st  # Streamlit és a modulok importálása a megjelenítéshez
from streamlit_module import get_visualizations  # Importálás a vizualizációs funkciókhoz

def main():
    # Az alkalmazás címének beállítása
    st.title("Fogyasztás és Termelés Elemzése")

    # Vizualizációk lekérése a streamlit_module-ból
    line_plot, scatter_plot = get_visualizations()

    # Két grafikon létrehozása a vizualizációkhoz
    col1, col2 = st.columns(2)
    
    # Vonaldiagram megjelenítése az első grafikonon
    with col1:
        st.subheader("Vonaldiagram")
        st.pyplot(line_plot)
    
    # Pontdiagram megjelenítése a második grafikonon
    with col2:
        st.subheader("Pontdiagram")
        st.pyplot(scatter_plot)

# Csak akkor futtatja a main() függvényt, ha ez a fájl a főprogram
if __name__ == "__main__":  # Ha a fájlt közvetlenül futtatjuk akkor nem fut le a main() függvény
    main()  # Ebben az esetben elindítja a main() függvényt