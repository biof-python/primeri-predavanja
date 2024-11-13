putanja:str = "dna3.txt"
datoteka = open("dna3.txt", "w")

sadrzaj:str = "AGTAGT"
# upisuje AGTAGT
datoteka.write(sadrzaj)

# upisuje CGTCGT u nastavku
sadrzaj = "CGTCGT"
datoteka.write(sadrzaj)

# upisuje abcdef u nastavku
datoteka.write("abc" + "def")

# upisuje 8 u nastavku
datoteka.write(str(len('AGTGCTAG')))

# upisuje 6 u nastavku
datoteka.write(str(len(sadrzaj)))

# upisuje TTGC u nastavku
datoteka.write("ATGC".replace('A', 'T'))

# upisuje atgc u nastavku
datoteka.write("ATGC".lower())

#datoteka.write("\n")

datoteka.close()