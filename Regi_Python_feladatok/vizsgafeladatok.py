#1. feladat
def osszead(szam1, szam2):
    """ A függvény két számot kap és 
        visszatér a két szám összegével.
    """
    
    return szam1+szam2

assert osszead(14, -8) == 6

#2. feladat
def kisebb(szam1, szam2):
    """ A függvény két számot kap és 
        visszatér a kisebbel.
    """
    if(szam1<szam2):
        return szam1
    else:
        return szam2

assert kisebb(10, -7) == -7
assert kisebb(-10, 7) == -10

#3. feladat
def nagyobb(szam1, szam2):
    """ A függvény két számot kap és 
        visszatér a nagyobbal.
    """
    if(szam1>szam2):
        return szam1
    else:
        return szam2

assert nagyobb(12, -8) == 12
assert nagyobb(-12, -8) == -8

#4. feladat
def szamtani_kozep(szam1, szam2):
    """ A függvény két számot kap és 
        visszatér a számtani középpel.
    """
    return (szam1 + szam2) / 2

assert szamtani_kozep(3, 5) == 4.0

#5. feladat
def negyzet_kerulet(oldal):
    """ A függvény egy négyzet oldalhosszát kapja bemenetként és 
        visszatér a négyzet kerületével.
    """
    return oldal * 4

assert negyzet_kerulet(5.1) == 20.4

#Maradékos osztás
def maradek(szam1, szam2):
    """ A függvény két számot kap bemenetként és 
        visszatér a két szám osztásának maradékával.
    """
    return szam1 % szam2

assert maradek(9, 4) == 1
assert maradek(8, 4) == 0

#Páros szám
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

#Kocka térfogat
def kocka_terfogat(oldal):
    """ A függvény bemenetként megkapja a kocka oldal hosszúságát és 
        a kocka térfogatával tér vissza.
    """    
    return oldal**3

assert kocka_terfogat(2) == 8
assert kocka_terfogat(3) == 27

#Abszolút érték
def abszolut(szam):
    """ A függvény a bemenő paraméterként kapott szám 
        abszolút értékével tér vissza.
    """    
    return abs(szam)

assert abszolut(-7) == 7
assert abszolut( 0) == 0


#p2

#Első karakter
def elso_karakter(string):
    """ Visszatér a string első karakterével.
    """
    return string[0]

assert elso_karakter("Hello") == "H"

#Utolsó karakter
def utolso_karakter(string):
    """ Visszatér az adott string utolso karakterével.
    """
    return string[-1]

assert utolso_karakter("Hello") == "o"


#Legkisebb szám

def legkisebb(lista):
    """ Visszatér egy számokat tartalmazó lista legkisebb számával.
    """
    legkisebb = 0
    
    for i in lista:
        if(i < legkisebb):
            legkisebb = i  
        
    return legkisebb
assert legkisebb( [7, 4, 9, -4, -8, 3]) == -8

#Listában lévő számok összege
def osszeg(lista):
    """ Visszatér egy számokat tartalmazó lista számainak összegével.
    """
    osszeg = 0
    for x in lista:
        osszeg += x
        
    return osszeg
    
assert osszeg( [1, 2, 3, 4, 5, 6] ) == 21

#Listában lévő számok szorzata
def szorzat(lista):
    """ Visszatér egy számokat tartalmazó lista számainak szorzatával.
    """
    osszeg = 1
    for x in lista:
        osszeg = osszeg * x
        
    return osszeg

assert szorzat( [1, 2, 3, 4, 5] )  == 120

def parosok_szama(lista):
    """ Visszatér egy számokat tartalmazó lista páros számainak számával
    """
    parosokszama = 0
    for x in lista:
        if(x % 2 == 0):
            parosokszama+=1
            
    return parosokszama

assert parosok_szama( [7, 4, 9, -4, -8, 3, 1] ) == 3

def paratlanok_szama(lista):
    """ Visszatér egy számokat tartalmazó lista páros számainak számával.
    """
    paratlanokszama = 0
    for x in lista:
        if(x % 2 != 0):
            paratlanokszama+=1
            
    return paratlanokszama


assert paratlanok_szama( [7, 4, 9, -4, -8, 3, 1]) == 4

def pozitivok_szama(lista):
    """ visszatér egy számokat tartalmazó lista pozitív számainak számával.
    """
    pozitivak = 0#Páratlan számok száma
    for x in lista:#Végiglépkedés a számokon
        if(x > 0):#Ha nagyobb mint 0 (Pozitív szám)
            pozitivak +=1#Páratlanok száma + 1
            
    return pozitivak#Páratlan számok száma visszatérítése
assert pozitivok_szama( [-7, -4, 9, -4, -8, 3, 1, 0]) == 3

def negativok_szama(lista):
    """ Visszatér egy számokat tartalmazó lista negativ számainak számával.
    """
    pozitivak = 0#Páratlan számok száma
    for x in lista:#Végiglépkedés a számokon
        if(x < 0):#Ha nagyobb mint 0 (Pozitív szám)
            pozitivak +=1#Páratlanok száma + 1
            
    return pozitivak

assert negativok_szama( [-7, -4, 9, -4, -8, 3, 1, 0]) == 4

def benne_van_a_listaban(lista, szam):
    for x in lista:
        if(x == szam):
            return True

    return False
assert benne_van_a_listaban([-7, -4, 9, -4, -8, 3, 1, 0], 2) == False
assert benne_van_a_listaban([-7, -4, 9, -4, -8, 3, 1, 0], 9) == True

def hanyadik_a_stringben(string, betu):
    index = 0#Ciklusban jelenleg ellenőrzött betű
    for x in string:#Végiglépkedés a szövegen
        if(x == betu):#Ha megvan a keresett betű
            return index#Dobd vissza az indexét
        index += 1#Ha megvan a betű, ha nincs, növeld eggyel


assert hanyadik_a_stringben("abrakadabra", "a") == 0
assert hanyadik_a_stringben("abrakadabra", "k") == 4