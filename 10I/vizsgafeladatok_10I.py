import math

# P1

def osszead(szam1, szam2):
    """ A függvény két számot kap és 
        visszatér a két szám összegével.
    """
    return szam1 + szam2

assert osszead(14, -8) == 6

def kisebb(szam1, szam2):
    """ A függvény két számot kap és 
        visszatér a kisebbel.
    """
    if (szam1 > szam2):
        return szam2
    else:
        return szam1

assert kisebb(10, -7) == -7
assert kisebb(-10, 7) == -10

def nagyobb(szam1, szam2):
    """ A függvény két számot kap és 
        visszatér a nagyobbal.
    """
    if (szam1 < szam2):
        return szam2
    else:
        return szam1

assert nagyobb(12, -8) == 12
assert nagyobb(-12, -8) == -8

def szamtani_kozep(szam1, szam2):
    """ A függvény két számot kap és 
        visszatér a számtani középpel.
    """
    return (szam1 + szam2) / 2

assert szamtani_kozep(3, 5) == 4.0

def negyzet_kerulet(oldal):
    """ A függvény egy négyzet oldalhosszát kapja bemenetként és 
        visszatér a négyzet kerületével.
    """
    return oldal * 4

assert negyzet_kerulet(5.1) == 20.4

def negyzet_terulet(oldal):
    """ A függvény egy négyzet oldalhosszát kapja bemenetként és 
        visszatér a négyzet területével.
    """    
    return oldal * oldal

assert negyzet_terulet(5.0) == 25.0

def teglalap_kerulet(oldal1, oldal2):
    """ A függvény egy téglalap oldalhosszait kapja bemenetként és 
        visszatér a téglalap kerületével.
    """
    return oldal1 * 2 + oldal2 * 2

assert teglalap_kerulet(5, 6) == 22

def teglalap_terulet(oldal1, oldal2):
    """ A függvény egy téglalap oldalhosszait kapja bemenetként és 
        visszatér a téglalap területével.
    """
    return oldal1 * oldal2

assert teglalap_terulet(5, 6) == 30

def kulonbseg(szam1, szam2):
    """ A függvény két számot kap bemenetként és 
        visszatér a két szám különbségével.
    """    
    return szam1 - szam2

assert kulonbseg(5, 6) == -1

def maradek(szam1, szam2):
    """ A függvény két számot kap bemenetként és 
        visszatér a két szám osztásának maradékával.
    """    
    return szam1 % szam2

assert maradek(9, 4) == 1
assert maradek(8, 4) == 0

def paros(szam):
    """ A függvény egy számot kap bemenetként, 
        majd True-val tér vissza, ha a szám páros és 
        False-al ha a szám páratlan.
    """    
    if(szam % 2 == 0):
        return True
    else:
        return False

assert paros(9) == False
assert paros(8) == True

def kettovel_oszthato(szam):
    """ A függvény egy számot kap bemenetként és 
        True-val tér vissza, ha a szám kettővel osztható és 
        False-al ha nem.
    """    
    if(szam % 2 == 0):
        return True
    else:
        return False

assert kettovel_oszthato(12) == True
assert kettovel_oszthato(13) == False

def harommal_oszthato(szam):
    """ A függvény egy számot kap bemenetként és 
        True-val tér vissza, ha a szám hárommal osztható és 
        False-al ha nem.
    """    
    if(szam % 3 == 0):
        return True
    else:
        return False

assert harommal_oszthato(15) == True
assert harommal_oszthato(16) == False

def hettel_oszthato(szam):
    """ A függvény egy számot kap bemenetként és 
        True-val tér vissza, ha a szám héttel osztható és 
        False-al ha nem.
    """    
    if(szam % 7 == 0):
        return True
    else:
        return False

assert hettel_oszthato(21) == True
assert hettel_oszthato(22) == False

def kocka_terfogat(oldal):
    """ A függvény bemenetként megkapja a kocka oldal hosszúságát és 
        a kocka térfogatával tér vissza.
    """    
    return oldal * oldal * oldal

assert kocka_terfogat(2) == 8
assert kocka_terfogat(3) == 27

def teglatest_terfogat(a, b, c):
    """ A függvény bemenetként megkapja a téglatest oldalainak hosszúságát és 
        a téglatest térfogatával tér vissza.
    """    
    return a * b * c

assert teglatest_terfogat(2, 3, 4) == 24

def derekszogu_haromszog_terulet(befogo1, befogo2):
    """ A függvény bemenetként megkapja a befogók hosszát és 
        a háromszög területével tér vissza.
    """    
    return befogo1 * befogo2 / 2

assert derekszogu_haromszog_terulet(3, 4) == 6

def derekszogu_haromszog_atfogo(befogo1, befogo2):
    """ A függvény bemenetként megkapja a befogók hosszát és 
        az átló hosszával tér vissza.
    """    
    return math.sqrt(befogo1 * befogo1 + befogo2 * befogo2)

assert derekszogu_haromszog_atfogo(3, 4), 5.0

def negyzet_atloja(oldal):
    """ A függvény bemenetként megkapja a négyzet oldalának hosszát és 
        az átló hosszával tér vissza.
    """    
    return math.sqrt(oldal * oldal + oldal * oldal)

assert round(negyzet_atloja(10),5) == round(14.142135623730951,5)

def teglalap_atloja(a, b):
    """ A függvény bemenetként megkapja az oldalak hosszát és 
        az átló hosszával tér vissza.
    """    
    return (a * a + b * b) ** 0.5

assert teglalap_atloja(3, 4) == 5.0
assert teglalap_atloja(6, 8) == 10.0

def abszolut(szam):
    """ A függvény a bemenő paraméterként kapott szám 
        abszolút értékével tér vissza.
    """    
    if (szam < 0):
        return -szam
    else:
        return szam
    
assert abszolut(-7) == 7
assert abszolut( 0) == 0




# P1 vége




def elso_karakter(string):
    """ Visszatér a string első karakterével.
    """
    return string[0]

assert elso_karakter("Hello") == "H"

def utolso_karakter(string):
    """ Visszatér az adott string utolso karakterével.
    """
    return string[-1]

assert utolso_karakter("Hello") == "o"

def legkisebb(lista):
    """ Visszatér egy számokat tartalmazó lista legkisebb számával.
    """
    legkisebbszam = 0#Elmentjuk a legkisebb számot
    for x in lista:#Végigmegyünk a listán
        if(x < legkisebbszam):#A jelenleg vizsgált szám kisebb-e mint ami el van tárolva
            legkisebbszam = x#Ha igen, akkor legyen az a szám
            #(Ha nem akkor jön a következő szám.)
    return legkisebbszam#Válasz visszatérítése

assert legkisebb( [7, 4, 9, -4, -8, 3]) == -8

def osszeg(lista):
    """ Visszatér egy számokat tartalmazó lista számainak összegével.
    """
    osszeg = 0#Osszeg elmentése
    for x in lista:#Végiglépkedés a kapott listán
        osszeg = osszeg + x#Hozzáadjuk az összeghez a jelenlegi számot.
        
    return osszeg#Válasz visszatérítése

assert osszeg( [1, 2, 3, 4, 5, 6] ) == 21

    
def halmazok_metszete(halmaz1, halmaz2):
    valasz = set()#Üres halmaz létrehozása
    for i in halmaz1:#Első halmazon végiglépkedés
        for j in halmaz2:#Második halmazon végiglépkedés
            if (i == j):
                valasz.add(i)
    #Ezzel a megoldással a két egymásba ágyazott ciklus                 
    return valasz

assert halmazok_metszete({1, 2, 3, 4, 5, 6, 7}, {4, 5, 6, 7, 8, 9}) == {4, 5, 6, 7}

def halmazok_unioja(halmaz1, halmaz2):
    valasz = set()
    for x in halmaz1:#Végiglépkedés a halmaz1-en
        valasz.add(x)#Hozzáadás a halmazhoz (az összes elemet)
        
    for x in halmaz2:#Végigmegyek a másik halmazon
        if(x not in halmaz1):
            valasz.add(x)
    return valasz

assert halmazok_unioja({1, 2, 3, 4, 5, 6, 7}, {4, 5, 6, 7, 8, 9}) == {1, 2, 3, 4, 5, 6, 7, 8, 9}

def faktorialis(n):
    valasz = 1
    for i in range(1, n+1):
        valasz *= i
        
    return valasz    
        

assert  faktorialis(0) == 1
assert  faktorialis(1) == 1
assert  faktorialis(2) == 1 * 2
assert  faktorialis(5) == 1 * 2 * 3 * 4 * 5

def karakterek_szama(fname):
    f = open("lorem.txt", "r")
    szoveg = f.read()
    f.close()
    return len(szoveg.strip())

assert karakterek_szama("lorem.txt") == 18047

def szavak_szama(fname):
    f = open(fname, "r")#Fájl megnyitása
    szoveg = f.read().strip()#Fájlban lévő szöveg beolvasása(f.read())
    return len(szoveg.split())

assert szavak_szama("lorem.txt") == 2304

class Teglalap:   
    def __init__(self, oldal1, oldal2):
        self.oldal1 = oldal1
        self.oldal2 = oldal2

    def kerulet(self):
        return self.oldal1 * 2 + self.oldal2 * 2
    
    def terulet(self):
        return self.oldal1 * self.oldal2

assert Teglalap(3, 4).oldal1 == 3
assert Teglalap(3, 4).oldal2 == 4
assert Teglalap(3, 4).kerulet() == 14
assert Teglalap(3, 4).terulet() == 12