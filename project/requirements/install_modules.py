# Szükséges modulok és könyvtárak telepítése
import subprocess  # Alrendszeri parancsok futtatására szolgáló modul

# Függvény a moduluk telepítéséhez
def install(module):
    # A pip telepítési parancs futtatása a modul telepítésére
    subprocess.check_call(['pip', 'install', module])
    # Visszajelzés a felhasználónak, hogy a modul sikeresen telepítve lett
    print(f"A szükséges modul(ok) {module} telepítve")

# Az alkalmazás futtatásához szükséges modulok telepítése
install('scikit-learn')  # Gépitanulási könyvtár (lineáris regresszió)
install('numpy')         # Numerikus számítási könyvtár
install('pandas')        # Adatkezelési és -elemzési könyvtár
install('matplotlib')    # Grafikonok és ábrák készítéséhez
install('streamlit')     # Webalkalmazás készítéséhez, adatvizualizációhoz
install('scipy')         # Tudományos számítási könyvtár
install('openpyxl')      # Excel fájlok létrehozására és betöltésére könyvtár
