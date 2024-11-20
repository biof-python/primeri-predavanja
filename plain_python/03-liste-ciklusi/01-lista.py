vrste:list[str] = ["Homo sapiens", "Pan troglodytes", "Gorilla gorilla"]

print("Lista koja sadrzi vrste:")
print(vrste)
b_vr:int = len(vrste)
print( str(b_vr) + " clanova")
print("Prvi clan:" + str(vrste[0]))

velicine:list[int] = [24, 56, 132, 10, 100]

print("Lista koja sadri velicine:")
print(velicine)
b_vl:int = len(velicine)
print( str(b_vl) + " clanova")

print("Prvi clan:" + str(velicine[0]))
print("Treci clan:" + str(velicine[2]))

print("Poslednji clan:" + str(velicine[-1]))
print("Poslednji clan:" + str(velicine[len(velicine)-1]))

print("Pretposlednji clan:" + str(velicine[-2]))

# dodavanje elementa 48 na kraj liste velicina
velicine.append(48)
print(velicine)

# dodavanje elementa 49 na poziciju 3 u listi velicina
velicine.insert(2, 49)
print(velicine)

# nalazenje pozicije broja 100 u listi velicina
poz_100:int = velicine.index(100)
print("Broj 100 se nalazi na poziciji " + str(poz_100) 
            + " u listi " + str(velicine))

# pre nalazenja pozicije treba proveriti da li se elemenat uopste nalazi u listi 
#poz_101:int = velicine.index(101)
#print("Broj 101 se nalazi na poziciji " + str(poz_101) + " u listi " + str(velicine))

x:int = 101
if x in velicine:
    print("Broj " + str(x) + "s e nalazi u listi.")
    ind_x:int = velicine.index(x)
    print("Pozicija, tj. indeks je " + str(ind_x))
else:
    print("Broj " + str(x) + " se ne nalazi u listi.")
    