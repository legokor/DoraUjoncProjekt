from Test import Test

'''
Kedves újoncok!

Az újonc feladatok python kódok írása.

Feladat 1:
- Nézzetek utána az mqtt kommunikációs formának: https://mqtt.org
- Nézzetek utána a python mqtt könyvtárainak: paho.mqtt.client

Feladat 2:
- Kaptatok egy docker file-t. Ezt másoljátok be ide a főkönyvtárba(Ha nincs docker a gépeteken, akkor szerezzetek be egy docker alkalmazást)
    https://drive.google.com/drive/folders/1WlgWY0pLLByLrFKyRD1WrZR5hbhq7z3S?usp=sharing
- Van két shell script (.sh, linuxra és mac-re, windowsra a .bat file-ok kellenek ám ezeket nem tudtam tesztelni) 
    ezeket sorban loadDocker, majd startDocker indítsátok el.
    (Az első betölti a docker file-t, itt nézzétek meg a docker file elérési útját, hogy stimmejen
    A második elindítja a dockert)
- Írjatok egy kódot, ami a standart kimenetre írja ki a tesztprogram által kiírt számokat.
- Számokat 'python/ujonc' topic-ra fogtok kapni
- Csatlakozni az 'ujonc_csatlakozas.json' file-ban talált adatokkal tudtok.

Feladat 3:
- Írjatok egy GUI-t (tkinter + matplotlib)
- Rajzoljátok ki egy grafikonra a kapott adatokat
'''

class App:
    def __init__(self, new_name="Dora"):
        self.name = new_name
        self.introduction()

    def introduction(self):
        print(self.name)


if __name__ == '__main__':

    feladat2 = False    # Ezt állítsd  True-ra és akkor elindul az mqtt küldés

    if feladat2:
        Test().runTest()

    App()
