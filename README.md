# Automatikus Letöltés Rendszerező

Ez egy háttérben futó Python automatizációs eszköz, amely tisztán tartja a Windows Letöltések mappáját. A program figyeli a megadott útvonalat, és kiterjesztés alapján kategóriákba (Képek, Dokumentumok, Zene, Egyéb) rendezi a fájlokat.

# Funkciók
 **Automatikus rendszerezés:** 2 óránként (beállítható) átvizsgálja a mappát.
 **Windows integráció:** Feladatütemezővel beállítható az automatikus láthatatlan indítás.

# Telepítés és használat
1. Másold le a `rendszerezo.py` fájlt.
2. Módosítsd a `folder_path` változót a saját felhasználói útvonaladra.
3. Futtasd a terminálban: `python rendszerezo.py`
4. (Opcionális) Állítsd be a Windows Feladatütemezőben a folyamatos, láthatatlan futáshoz.
