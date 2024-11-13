# ulaz i izlaz su dati relativnim adresama 
putanja_ulaz:str = "dna1.txt"
putanja_izlaz:str = "statistika.txt"

ulaz = open(putanja_ulaz)
izlaz = open(putanja_izlaz, "w")
izlaz.write("A T G C \n")

linija:str = ulaz.readline()
linija = ulaz.readline()
while linija != "":
    broj_A = linija.count("A")
    broj_T = linija.count("T")
    broj_G = linija.count("G")
    broj_C = linija.count("C")
    izlaz.write(str(broj_A) + " " + str(broj_T) + " " 
                + str(broj_C) + " " + str(broj_G) + "\n")
    linija = ulaz.readline()

ulaz.close()
izlaz.close()