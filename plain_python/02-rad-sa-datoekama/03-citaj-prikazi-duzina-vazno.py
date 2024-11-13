# otvaranje datoteke
putanja:str = "dna2.txt"
file_objekat = open(putanja, "r")

# citanje i prikaz svih znakova datoteke
sadrzina:str = file_objekat.read()
print("Sadrzaj datoteke '" + putanja + "'>>>")
print(sadrzina)
print(">>>")
print("Datoteka sadrzi " + str(len(sadrzina)) + " znakova.")

# odredjivanje i prikaz znakova bez belina sa kraja
vazno:str = sadrzina.rstrip()
print("Sadrzaj datoteke (bez belina sa kraja) '" + putanja + "'>>>")
print(vazno)
print(">>>")
print("Datoteka sadrzi " + str(len(vazno)) + " znakova (bez belina sa kraja).")