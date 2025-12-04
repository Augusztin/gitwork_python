#Kérj be egy számot, és számold ki a faktoriálisát iterációval.
print(==faktoriális számítás==)
szam=int(input("Mondj egy egyész számot: "))

fakt=1
for i in range(1,szam+1):
    fakt=fakt*i
print(f"{szam} faktoriálisa {fakt}")
