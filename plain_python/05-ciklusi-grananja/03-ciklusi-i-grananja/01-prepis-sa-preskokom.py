# ulaz je dat relativnom adresom 
putanja_ulaz:str = "dna1.txt"

ulaz = open(putanja_ulaz)
n:int = int(input("Unesite poziciju koja se preskace"))

linija:str = ulaz.readline()
while linija != "":
    za_prikaz:str = ""
    for i in range(len(linija)):
        if (i+1) % n != 0:
            za_prikaz += linija[i]
    print(za_prikaz.rstrip().lstrip())
    linija = ulaz.readline()

ulaz.close()
