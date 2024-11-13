# ulaz i izlaz su dati relativnim adresama 
#putanja_ulaz:str = "dna.txt"
#putanja_izlaz:str = "dna99.txt"

# ulaz i izlaz su dati apsolutnim adresama 
putanja_ulaz:str = "/home/nastavnik/Biologija/primeri-predavanja/plain_python/02-rad-sa-datoekama/dna.txt"
putanja_izlaz:str = "/home/nastavnik/Biologija/primeri-predavanja/plain_python/02-rad-sa-datoekama/dna99.txt"


ulaz = open(putanja_ulaz)
sadrzaj = ulaz.read()

izlaz = open(putanja_izlaz, "w")
izlaz.write(sadrzaj)

ulaz.close()
izlaz.close()