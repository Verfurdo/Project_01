# streamlit_module nevű modult importálunk
import streamlit_module

# Fő függvény definiálása
def main():
    # Meghívjuk a Streamlit alkalmazás futtatásáért felelős függvényt
    streamlit_module.run_streamlit_app()

# Ellenőrizzük, hogy a fájlt közvetlenül futtatjuk-e
if __name__ == "__main__":  # Ha a fájlt közvetlenül futtatjuk, akkor a __name__ értéke "__main__"
    main()  # Ebben az esetben meghívjuk a main() függvényt

