n:int = int(input("Unesite broj "))
rezultat:float = 1
brojac:int = 1
while brojac <= n:
    rezultat *= brojac 
    brojac += 1
print(str(n) + "!" + " = " + str(rezultat) )