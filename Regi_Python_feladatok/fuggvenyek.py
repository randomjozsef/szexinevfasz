#A függvények programozói szemmel egyáltalán nem ugyanolyanok
#mint a matematikában, onnan ismerhetitek őket.

#Egy függvény létrehozása a következő:
#def név():
#A függvényt úgy kell elképzelni, mint egy tárolót.
#A függvény tartalma a neve után az egy tabulátorral beljebb levő sorok.
szam = 1
def fuggveny():
    #A következő print-et tartalmazó sor a függvény része.
    print(szam)
#Az alábbi print sor már nem.
print(szam)
szam += 1
szam += 1
#A függvényben lévő dolgok nem futnak le, csak akkor ha a függvény meg van hívva.
#Következőképpen lehet függvényt meghívni:
fuggveny()
#Így, hogy ki van kommentelve a fuggveny() (16-os) sor, nem fut le a függvény.
#Ha kitörlitek a #-et előle és futtatjátok a fájlt az F5 megnyomásával, akkor látjátok azt ami leírtam.