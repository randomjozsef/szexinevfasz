# Bemeneti adatok
konyvek = [
    {"cím": "Az arany ember", "szerző": "Jókai Mór", "kölcsönzések_száma": 12, "elérhető": True},
    {"cím": "Egri csillagok", "szerző": "Gárdonyi Géza", "kölcsönzések_száma": 18, "elérhető": False},
    {"cím": "A kőszívű ember fiai", "szerző": "Jókai Mór", "kölcsönzések_száma": 7, "elérhető": True},
    {"cím": "Pál utcai fiúk", "szerző": "Molnár Ferenc", "kölcsönzések_száma": 25, "elérhető": False},
    {"cím": "Tüskevár", "szerző": "Fekete István", "kölcsönzések_száma": 15, "elérhető": True},
]

# Lista hozzáférés példa
def lista_hozzaferes(konyvek):
    for i in konyvek:
        print(i['szerző'])# A kettőspont előtti névvel lehet hozzáférni az értékekhez. (cím, szerző, kölcsönzések_száma, elérhető)
        # Így lehet hozzáférni az eltárolt értékekhez.

# Összegzés tétele
def osszes_kolcsonzes(konyvek):
    osszeg = 0
    for i in konyvek:
        osszeg += i['kölcsönzések_száma']
    return osszeg

# Megszámlálás tétele
def elerheto_konyvek_szama(konyvek):
    return konyvek

# Minimumkiválasztás tétele
def legkevesebb_kolcsonzes(konyvek):
    return konyvek

# Maximumkiválasztás tétele
def legtobb_kolcsonzes(konyvek):
    return konyvek

# Eldöntés tétele
def van_e_gardonyi_konyv(konyvek):
    return konyvek
    
lista_hozzaferes(konyvek)

# Assert-ek (tesztellenőrzések)
assert osszes_kolcsonzes(konyvek) == 77, "Az összes kölcsönzés hibás!"
assert elerheto_konyvek_szama(konyvek) == 3, "Az elérhető könyvek számítása hibás!"
assert legkevesebb_kolcsonzes(konyvek)["cím"] == "A kőszívű ember fiai", "A legkevesebb kölcsönzés hibás!"
assert legtobb_kolcsonzes(konyvek)["cím"] == "Pál utcai fiúk", "A legtöbb kölcsönzés hibás!"
assert van_e_gardonyi_konyv(konyvek) == True, "A Gárdonyi Géza könyv eldöntése hibás!"

print("Minden teszt sikeresen lefutott!")

