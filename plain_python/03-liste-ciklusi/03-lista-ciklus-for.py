vrste:list[str] = ["Homo sapiens", "Pan troglodytes", "Gorilla gorilla"]

# kolekcijski ciklus
for v in vrste:
    print( v + " je jedna vrsta.")
    
# brojacki ciklus
for i in range(len(vrste)):
    v:str = vrste[i]
    print( v + " je jedna vrsta.")