a:float = float(input("Unesite osnovu "))
b:int = int(input("Unesite izlozilac "))
rezultat:float = 1
brojac:int = 1
while brojac <= b:
    rezultat *= a # isto kao: rezultat = rezultat * a
    brojac += 1
print("Stepen je \n" + str(a) + "^" + str(b) + " = " + str(rezultat) )