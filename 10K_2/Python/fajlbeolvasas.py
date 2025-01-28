#Lorem szavak megszámlálása

f = open("lorem.txt")
count = 0

for x in f:
    if("lorem" in x.lower()):
        count += 1
        
print(count)
f.close()