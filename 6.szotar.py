emberek={}
lista=[]
for i in range(2):
    nev=input("kérem a nevet: ")
    kor=input("Kérem az életkortát: ")
    lista.append(kor)
    hajszin=input("Kérem a haja színét: ")
    lista.append(hajszin)
    emberek[nev]=lista

max=0
i=0
for x in emberek:
    if int(emberek[x][0]) > int(max):
        max=int(emberek[x][0])
        i=x

print(f"A legidősebb ember neve {i}")

#nem jó még mindig

