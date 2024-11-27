n:int = int(input("Unesite broj "))
rezultat:float = 1
for brojac in range(n, 0, -1):
    rezultat *= brojac 
print(str(n) + "!" + " = " + str(rezultat) )