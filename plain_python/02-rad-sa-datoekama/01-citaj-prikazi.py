putanja:str = "dna.txt"
file_objekat = open(putanja)
# Ovo nam najcesece nije orisna informacija
# print(file_objekat)
sadrzina:str = file_objekat.read()
print("Sadrzaj datoteke '" + putanja + "'>>>")
print(sadrzina)

