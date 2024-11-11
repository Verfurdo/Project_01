# Lineáris Regresszió

Ez a projekt a hazai sörfogyasztás és termelés adatainak lineáris regressziós elemzését végzi logaritmikus transzformáció alkalmazásával. A stadat-nep0013-22.1.1.13-hu.csv adatfájl alapján elemzi a kapcsolatot a termelés és a fogyasztás között, és grafikusan megjeleníti az eredményeket beleértve a lineáris regresszió egyenesét is.

A statisztika eszköztárában a lineáris regresszió egy olyan paraméteres regressziós modell, 
mely feltételezi a magyarázó- (X) és a magyarázott változó közti lineáris kapcsolatot. 
Ez azt jelenti, hogy lineáris regresszió becslése során a mintavételi adatok 
pontjaira egy egyenest illeszt rá.


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
    scipy
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

    install_modules.py: Függőségek telepítéséhez használt python script.
    start_project.py: A program indításához használt python script.
    project.py: A Streamlit alkalmazás indítófájlja, amely a streamlit_module.py modult használja a webes megjelenítéshez.
    streamlit_module.py: A Streamlit alkalmazás alapvető funkcióit tartalmazza, és a regression_analysis.py 
                         és plot.py modulokat használja az adatelemzéshez és a grafikus megjelenítéshez.
    regression_analysis.py: Az adatok tisztításához, elemzéséhez a logaritmikus transzformáció elvégzéséhez szükséges függvényeket tartalmazza.
    plot.py: Az adatok grafikus ábrázolásáért felelős.

Kimenet

    Metrikák:
        Mean Squared Error (MSE): A regressziós modell hibáját méri. A négyzetes hibák átlaga, akkor a legjobb, ha az értéke minél közelebb van a 0-hoz. 
        R-squared (R2): A modell illeszkedésének pontosságát mutatja 1.0 a tökéletes illeszkedés.

    Grafikon:
        Egy logaritmizált skálán ábrázolt diagram jelenik meg, amelyen a termelés és fogyasztás 
        kapcsolatát látjuk, beleértve a lineáris regressziós egyenest is.

Forrás

    Az adatok a Központi Statisztikai Hivatal (KSH) adatbázisából származnak, amely itt érhető el: https://www.ksh.hu/stadat.

Ez a README.md útmutatást nyújt a projekt telepítéséhez, használatához, valamint áttekintést ad az egyes fájlok szerepéről.

