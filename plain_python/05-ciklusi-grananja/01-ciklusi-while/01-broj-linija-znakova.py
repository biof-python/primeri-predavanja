putanja_ulaz:str = "dna1.txt"
ulaz = open(putanja_ulaz)

broj_znakova:int = 0
broj_linija:int = 0
linija = ulaz.readline()
while linija != "":
    # uvecava se na adekvatan nacin broj znakova i broj linija
    broj_znakova += len(linija)
    broj_linija += 1
    # procitaj sledecu liniju datoteke
    linija = ulaz.readline()
print("Broj znakova: " + str(broj_znakova))
print("Broj linija:  " + str(broj_linija))
