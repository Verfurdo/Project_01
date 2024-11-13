# Hazai Sörfogyasztás és Termelés Adatelemző Alkalmazás


Ez a projekt a hazai sörfogyasztás elemzését végzi a `stadat-nep0013-22.1.1.13-hu.csv` adatfájl alapján. A cél a termelés és a fogyasztás közötti kapcsolat elemzése, grafikus megjelenítése és statisztikai elemzés elvégzése. Az elemzés eredményei vizuálisan, interaktív Streamlit alkalmazásban jelennek meg, illetve a statisztikai adatok CSV fájlba mentésével statisztikai adatokhoz juthatunk.

Tartalom

    Előfeltételek
    Telepítés
    Adatfájl
    Használat
    Fájlok magyarázata
    Kimenet
    Forrás

Előfeltételek

    A projekt az alábbi Python könyvtárakat használja:

    numpy
    pandas
    matplotlib
    scikit-learn
    streamlit 

Telepítés

    Könyvtárak telepítése requirements mappában található
    Minden szükséges modult telepíthetsz a következő paranccsal:
        pip install -r requirements.txt
    Vagy futtathatod az install_modules.py fájlt, amely automatikusan telepíti a függőségeket:
        python install_modules.py


Adatfájl 

    Data mappában található a stadat-nep0013-22.1.1.13-hu.csv fájl az elemzések ezt a fájlt használják forrásként. 
    Az adatok a KSH statisztikai adatbázisából származnak.

Használat

    Streamlit alapú megjelenítés
    Futtasd a project.py fájlt a Streamlit segítségével: 
        streamlit run project.py 
    Vagy futtasd a start_project.py fájlt az elindításhoz:
        python start_project.py
 
    Ez megnyit egy webes felületet, ahol interaktívan megjelennek az eredmények.
    A Streamlit egy nyílt forráskódú Python keretrendszer, amely lehetővé teszi hogy interaktív 
    adat alkalmazásokat készítsenek ezzel a Python szkripteket gyorsan és egyszerűen, webalkalmazásokká alakíthatunk.

Fájlok magyarázata

    install_modules.py: A projekt függőségeinek telepítésére szolgáló szkript.
    start_project.py: A projekt indítását végző segédfájl.
    project.py: A fő Streamlit alkalmazásindító fájl, amely a streamlit_module.py modult használja a megjelenítéshez.
    streamlit_module.py: A Streamlit alkalmazás alapvető funkcióit, adatbetöltést, elemzést és vizualizációkat tartalmazó modul.
    data_analysis.py: Az adatok betöltésére és előkészítésére szolgáló modul.
    statistical_analysis.py: A statisztikai mutatók kiszámítását és a mentést végző modul.
    line_plot.py: A termelési és fogyasztási adatok vonaldiagramjának létrehozását végző modul.
    scatter_plot.py: A termelés és fogyasztás közötti kapcsolat pontdiagramjának és a regressziós elemzésnek a megjelenítéséért felelős modul.

Kimenet

    Grafikonok:
        Egy vonal és pont diagram jelenik meg, amelyen a termelés és fogyasztás 
        kapcsolatát látjuk, beleértve a lineáris regressziós egyenest is.
        
    Metrikák:
        R-squared (R2): A modell illeszkedésének pontosságát mutatja 1.0 a tökéletes illeszkedés.

    Statisztika mentése:
        A program a data mappába menti a statisztikai fájlt el.

    

Forrás

    Az adatok a Központi Statisztikai Hivatal (KSH) adatbázisából származnak, amely itt érhető el: https://www.ksh.hu/stadat.

Ez a README.md útmutatást nyújt a projekt telepítéséhez, használatához, valamint áttekintést ad az egyes fájlok szerepéről.

