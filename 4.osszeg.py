# Kérj be egy számot, majd számold ki a számjegyeinek összegét.

szam=input("Kérek egy számot: ")
ossz=0

for i in range(len(szam)):
    ossz = ossz + int(szam[i])
print(f"A számjegyek összege: {ossz}")
