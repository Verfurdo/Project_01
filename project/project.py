# importáljuk a streamlit_module.py fájlt
import streamlit_module

# Fő függvény definiálása
def main():
    # Meghívja a streamlit_futtatasa függvényt a streamlit_module fájlból
    streamlit_module.streamlit_futtatasa() 

# Ellenőrizzük, hogy a fájlt közvetlenül futtatjuk-e
if __name__ == "__main__":  # Ha a fájlt közvetlenül futtatjuk, akkor a __name__ értéke "__main__"
    main()  # Ebben az esetben meghívjuk a main() függvényt
    