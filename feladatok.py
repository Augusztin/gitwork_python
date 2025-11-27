# print("Feladat 1:")
# szam1 = float(input("Add meg egy számot! "))
# szam2 = float(input("Add meg egy másik számot! "))
# print(f"A két szám összege: ", {szam1+szam2})

# print("Feladat 2:")
# szam_parose = int(input("Adj meg egy egész számot! "))
# if szam_parose != 0:
#     if szam_parose % 2 == 0:
#         print("Ez a szám páros")
#     else:
#         print("Ez a szám páratlan")
# else:
#     print("Nullát ne!")


# print("Fealadat 3a:")
# szamok = []
# szamok.append(float(input("Kérem az első számot: ")))
# legnagyobb = szamok[0]
# szamok.append(float(input("Kérem a második számot: ")))
# szamok.append(float(input("Kérem a harmadik számot: ")))

# for i in szamok:
#     if i >= legnagyobb:
#         legnagyobb = i
# print(f"A legnagyobb szám a ", {legnagyobb})

# print("Feladat 3b a tábláról:")
# tomb = [] 
# for i in range(3):
#     tomb.append(int(input(f"Kérem {i}. számot:")))

# max = tomb[0]
# id = 0

# for i in range(3):
#     if tomb[i] > max:
#         max = tomb[i]
#         id = i

# print(f"A legnagyob eleme a {max} ami a {id+1}. helyen van.")

# print("Kérj be egy N értéket, majd írd ki 1-től N-ig a számokat egy ciklussal.")
# szam = int(input("Kérem N értékét: "))

# for i in range(1, szam + 1):
#     print(f"{i}",end=" ")


# szam = int(input("Kérem N értékét: "))
# ossz = 0
# for i in range(1, szam + 1):
#     ossz = ossz + i

# print(f"A számok összege: {ossz}")

# print("Kérj be 5 darab számot, tedd őket listába, majd számold ki az átlagukat.")

# tm = []
# for i in range(5):
#     tm.append(int(input(f"Kérem a {i+1}. számot: ")))

# ossz = 0
# for i in range(5):
#     ossz += tm[i]
# print (f"A lista elemeinek az átlaga: {ossz/len(tm)}")

# print("6. feladat")
# lista = [4,6,8,201,4,5,6]
# max = lista[0]
# for i in range(len(lista)):
#     if lista [i] > max:
#         max = lista[i]
# print(f"A legnagyobb elem a {max}")

# min = lista[0]
# for i in range(len(lista)):
#     if lista [i] > min:
#         max = lista[i]
# print(f"A legkisebb elem a {min}")

#Kérj be egy számot és döntsd el, hogy benne van-e az előre adott listában.
lista