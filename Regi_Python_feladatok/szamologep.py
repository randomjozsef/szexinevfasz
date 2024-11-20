print ("kérem az első számot")
sam1 = int(input())
print ("kérem a másoik számot")
sam2 = int(input())

print ("kérem a műveleti jelet +-*/")
muvjel = input()

if(muvjel=="+"):
    print(sam1+sam2)
elif(muvjel=="-"):
    print(sam1-sam2)
elif(muvjel=="*"):
    print(sam1*sam2)
elif(muvjel=="/"):
    print(sam1/sam2)
else:
    print("nincs ilyen muveleti jel")
    
    