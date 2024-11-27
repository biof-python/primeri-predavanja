putanja_ulaz:str = "dna1.txt"
ulaz = open(putanja_ulaz)

linija = ulaz.readline()
while linija != "":
    # procitana je neparna linija
    linija = linija.rstrip().lstrip()
    print(linija, sep=None)
    # procitaj sledecu liniju koja nece biti prikazana
    linija = ulaz.readline()
    # procitaj sledecu liniju koja ce biti prikazana
    linija = ulaz.readline()
