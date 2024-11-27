# ulaz i izlaz su dati relativnim adresama 
putanja_ulaz:str = "elefas-maximus.fasta"

ulaz = open(putanja_ulaz)

linija:str = ulaz.readline()
while linija != "":
    prvi_znak:str = linija[0]
    if  prvi_znak == ";":
        # radi se o liniji sa komentarom koja se ignorise
        pass
    elif prvi_znak == ">":
        # radi se o zaglavlju
        zaglavlje:str = linija[1:]
        opis_gi:str = ""
        opis_gb:str = ""
        opis_t:str = ""
        delovi:list[str] = zaglavlje.split("|")
        i:int = 0
        while i < len(delovi):
            if delovi[i]=='gb':
                opis_gb = delovi[i+1]
                i += 2
            elif delovi[i]=='gi':
                opis_gi = delovi[i+1]
                i += 2
            else:
                opis_t = delovi[i].rstrip().lstrip()
                i += 1
        print("Opis text:" + opis_t)
        print("Opis genbank:" + opis_gb)
        print("Opis geninfo:" + opis_gi)        
    else:
        # radi se o genetskom zapisu za koji racunamo pojavu slova po linijama
        broj_C = linija.count("C")
        broj_G = linija.count("G")
        broj_L = linija.count("L")
        broj_Y = linija.count("Y")
        broj_T = linija.count("T")
        broj_H = linija.count("H")
        print("C:" + str(broj_C) + " G:" + str(broj_G) + " L:" + str(broj_L) 
                + " T:" + str(broj_T) + " H:" + str(broj_H))        
    linija = ulaz.readline()

ulaz.close()
