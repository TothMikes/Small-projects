import random

rszam = 0
jelen = 100
tet = 0
tovabb = True
piros = [32, 19, 21, 25, 34, 27, 36, 30, 23, 5, 16, 1, 14, 9, 18, 7, 12, 3]
fekete = [15, 4, 2, 17, 6, 13, 11, 8, 10, 24, 33, 20, 31, 22, 29, 28, 35, 26]
szam = 0
szinvalasz = "valami"
szamvalasz = 37
jatekforma = 0
jo = False
akar = "igen"

while tovabb and jelen > 0:
    rszam = random.randint(1, 37)
    # 1=piros 2=fekete 3=zöld
    if rszam <= 18:
        rszam = 1
        szam = random.choice(piros)
    elif rszam > 18 and rszam <= 36:
        rszam = 2
        szam = random.choice(fekete)
    else:
        rszam = 3
    print("Jelenleg", jelen, "pénzed van.")
    jatekforma = int(input("Mire szeretnél fogadni?: (1=szín 2=szám): "))

    if jatekforma == 1:

        szinvalasz = input("Válassz egy színt! (piros, fekete vagy zöld?): ")
        if szinvalasz == "piros":
            szinvalasz = 1
        elif szinvalasz == "fekete":
            szinvalasz = 2
        elif szinvalasz == "zöld":
            szinvalasz = 3

        jo = False
        while not jo:
            tet = int(input("Tegyél fel egy tétet! "))
            if tet <= jelen and tet > 0:
                jo = True
            elif tet > jelen:
                print("Nincs ennyi pénzed.")

        if szinvalasz == rszam:
            if szinvalasz == 3:
                jelen = jelen + (tet * 35)
            else:
                jelen += tet
            print("Gratulálok győztél! Most már", jelen, "pénzed van.")
            akar = input("Szeretnéd folytatni a játékot? (igen vagy nem): ")
            if akar == "nem":
                tovabb = False
        else:
            jelen -= tet
            print("Sajnálom nem nyert.", jelen, "pénzed maradt.")

            if rszam == 1:
                rszam = "piros"
            elif rszam == 2:
                rszam = "fekete"
            else:
                rszam = "zöld"

            print("Kipörgetett szín a", rszam, "volt.")

            if jelen > 0:
                akar = input("Szeretnéd folytatni a játékot? (igen vagy nem): ")
                if akar == "nem":
                    tovabb = False

    elif jatekforma == 2:

        szamvalasz = input("Adj megy egy számot amire fogadsz (1-től 36-ig): ")

        jo = False
        while not jo:
            tet = int(input("Tegyél fel egy tétet! "))
            if tet <= jelen and tet > 0:
                jo = True
            elif tet > jelen:
                print("Nincs ennyi pénzed.")

        if szamvalasz == szam:
            jelen = jelen + (tet * 35)
            print("Gratulálok győztél! Most már", jelen, "pénzed van.")
            akar = input("Szeretnéd folytatni a játékot? (igen vagy nem): ")
            if akar == "nem":
                tovabb = False
        else:
            jelen -= tet
            print("Sajnálom nem nyert.", jelen, "pénzed maradt.")
            print("A kipörgetett szám a", szam, "volt.")
            if jelen > 0:
                akar = input("Szeretnéd folytatni a játékot? (igen vagy nem): ")
                if akar == "nem":
                    tovabb = False


print("A játék véget ért.")
print(jelen, "pénzed maradt.")
