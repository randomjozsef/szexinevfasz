#A feladat egy ATM letrehozása, ami tárol egy egyenleget, és lehet pénzt felvenni/befizetni.
#Elsősorban egy menüt kell mutasson a program, amiben 3 lehetőség van:
#1. Pénzfelvétel
#2. Pénzbefizetés
#3. Kilépés
#Ez után a felhasználó választ, és ha tranzakció történik, akkor kérje el a PIN kódot.
#Helyes PIN kód beütésnél kér egy összeget amit levon/hozzáad az egyenleghez és aztán kiírja azt.
#A kilépés lehetőségen kívül újra mutassa a menüt a tranzakció végbemenetele után.
PIN = "1234"
kilepett = False
egyenleg = 10000

def menukiir():
    print("1. Pénzfelvétel\n2. Pénzbefizetés\n3. Kilépés\n")#Menü kiírása
    
def pinkodbeker():
    valasz = input("Kérem a PIN kódot: ")#Válasz vált.-ban eltároljuk a felh. bemenetet
    if(valasz == PIN):#Ha egyenlő a válasz a PIN kóddal, akkor igaz, ha nem, hamis
        return True
    else:
        return False

while (not kilepett):#Amíg a felh. nem lépett ki
    menukiir()#Menü kiírása
    
    valasz = input()#Válasz bekérése
    
    if(valasz == "3"):#Ha kilép, köszönj el és leállás
        print("Cső")
        break
    
    if(valasz != "1" and valasz != "2"):#Ha nem tranzakció, akkor újra
        continue
    
    if(pinkodbeker() != True):#Ha nem jó a PIN kód
        print("Nem jó a PIN kód!")
        continue
    
    if(valasz == "1"):#Ha pénzfelvétel
        osszeg = int(input("Kérem a levonni kívánt összeget: "))#Összeg bekérés
        egyenleg -= osszeg#Tranz. végrehajtása
        print(f"Fennmaradó egyenleg: {egyenleg} Ft")#Egyenleg kiírása
        
    if(valasz == "2"):
        osszeg = int(input("Kérem a befizetni kívánt összeget: "))#Összeg bekérés
        egyenleg += osszeg#Tranz. végrehajtása
        print(f"Fennmaradó egyenleg: {egyenleg} Ft")#Egyenleg kiírása