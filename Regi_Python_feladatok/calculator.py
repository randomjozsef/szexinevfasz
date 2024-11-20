# Összeadás  
def osszeadas(a, b):  
    return a + b  

# Kivonás  
def kivonas(a, b):  
    return a - b  

# Fő program  
print("Egyszerű számológép")  
a = float(input("Kérlek, add meg az első számot: "))  
b = float(input("Kérlek, add meg a második számot: "))  

print("Válassz egy műveletet:")  
print("1 - Összeadás")  
print("2 - Kivonás")  

valasztas = input("Kérlek, írd be a választott művelet számát (1 vagy 2): ")  

if valasztas == '1':  
    eredmeny = osszeadas(a, b)  
    print(f"Az eredmény: {eredmeny}")  
elif valasztas == '2':  
    eredmeny = kivonas(a, b)  
    print(f"Az eredmény: {eredmeny}")  
else:  
    print("Érvénytelen választás.") 
     

