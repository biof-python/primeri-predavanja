n:int = int(input("Unesite broj "))
rezultat:float = 1
brojac:int = n
while brojac >= 1:
    rezultat *= brojac 
    brojac -= 2
print(str(n) + "!!" + " = " + str(rezultat) )