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


print("Fealadat 3:")
szamok = []
szamok.append(float(input("Kérem az első számot")))
legnagyobb = szamok[0]
szamok.append(float(input("Kérem a második számot")))
szamok.append(float(input("Kérem a harmadik számot")))

for i in szamok:
    if i >= legnagyobb:
        legnagyobb = i
print(f"A lergnagyobb száma a ", {legnagyobb})
