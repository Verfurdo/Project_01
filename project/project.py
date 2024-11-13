# project.py

import streamlit as st
from streamlit_module import get_visualizations

def main():
    st.title("Fogyasztás és Termelés Elemzése")

    # Vizualizációk lekérése
    line_plot, scatter_plot = get_visualizations()

    # Két oszlop Streamlit-ben
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("(Vonaldiagram)")
        st.pyplot(line_plot)
    
    with col2:
        st.subheader("(Pontdiagram)")
        st.pyplot(scatter_plot)

if __name__ == "__main__":
    main()
