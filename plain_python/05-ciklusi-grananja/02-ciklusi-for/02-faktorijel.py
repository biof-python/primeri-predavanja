n:int = int(input("Unesite broj "))
rezultat:float = 1
for brojac in range(1, n+1):
    rezultat *= brojac 
print(str(n) + "!" + " = " + str(rezultat) )