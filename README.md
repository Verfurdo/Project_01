# Project_01

Ez a projekt a hazai fogyasztás és termelés adatainak lineáris regressziós elemzését végzi logaritmikus transzformáció alkalmazásával. A sormerleg.csv adatfájl alapján elemzi a kapcsolatot a termelés és a fogyasztás között, és grafikusan megjeleníti az eredményeket logaritmikus skálán, beleértve a lineáris trendet is.

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

    Könyvtárak telepítése
    Minden szükséges modult telepíthetsz a következő paranccsal:
    pip install -r requirements.txt

    Alternatív megoldásként futtathatod az install_modules.py fájlt, amely automatikusan telepíti a függőségeket:
    python install_modules.py


Adatfájl 

    Data mappában található a sormerleg.csv fájl az elemzések ezt a fájlt használják forrásként. 
    Az adatok a KSH statisztikai adatbázisából származnak.

Használat

    Streamlit alapú megjelenítés
    Futtasd a project.py fájlt a Streamlit segítségével:

    streamlit run project.py

    Ez megnyit egy webes felületet, ahol interaktívan megjelennek az eredmények.

Fájlok magyarázata

    install_modules.py: Függőségek telepítéséhez használt script.
    project.py: A Streamlit alkalmazás indítófájlja, amely a streamlit_app.py modult használja a webes megjelenítéshez.
    streamlit_app.py: A Streamlit alkalmazás alapvető funkcióit tartalmazza, és a regression_analysis.py 
                      és plot.py modulokat használja az adatelemzéshez és a vizualizációhoz.
    regression_analysis.py: Az adatok elemzéséhez, tisztításához és a logaritmikus transzformáció 
                            elvégzéséhez szükséges függvényeket tartalmazza.
    plot.py: A logaritmikus transzformált adatok grafikus ábrázolásáért felelős.

Kimenet

    Metrikák a konzolban:
        Mean Squared Error (MSE): A regressziós modell hibáját méri.
        R-squared (R2): A modell illeszkedésének pontosságát mutatja.

    Grafikon:
        Egy logaritmizált skálán ábrázolt diagram jelenik meg, amelyen a termelés és fogyasztás 
        kapcsolatát látjuk, beleértve a lineáris regressziós egyenest is.

Forrás

    Az adatok a Központi Statisztikai Hivatal (KSH) adatbázisából származnak, amely itt érhető el: https://www.ksh.hu/stadat.

Ez a README.md útmutatást nyújt a projekt telepítéséhez, használatához, valamint áttekintést ad az egyes fájlok szerepéről.

