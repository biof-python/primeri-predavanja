putanja_ulaz:str = "dna1.txt"
ulaz = open(putanja_ulaz)

linija = ulaz.readline()
while linija != "":
    # procitana je neparna linija i ona se ignorise
    # procitaj sledecu liniju koja je parna
    linija = ulaz.readline()
    # prikaz parne linije
    linija = linija.rstrip().lstrip()
    print(linija, sep=None)
    # procitaj sledecu liniju koja ce biti neparna
    linija = ulaz.readline()
