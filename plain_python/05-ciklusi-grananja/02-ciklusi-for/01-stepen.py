a:float = float(input("Unesite osnovu "))
b:int = int(input("Unesite izlozilac "))
rezultat:float = 1
for brojac in range(1,b+1):
    rezultat *= a 
print("Stepen je \n" + str(a) + "^" + str(b) + " = " + str(rezultat) )