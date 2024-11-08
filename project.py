# streamlit_app nevű modult importálunk
import streamlit_app

# Fő függvény definiálása
def main():
    # Meghívjuk a Streamlit alkalmazás futtatásáért felelős függvényt
    streamlit_app.run_streamlit_app()

# Ellenőrizzük, hogy a fájlt közvetlenül futtatjuk-e
if __name__ == "__main__":
    main()
