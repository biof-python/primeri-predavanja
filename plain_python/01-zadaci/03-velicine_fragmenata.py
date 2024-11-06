kod:str = "ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT" 
print("Kod:      " + kod)
trazi_se:str = "GAATTC"
print("Trazi se: " + trazi_se)
poz:int = kod.find(trazi_se)
poz += 1 # mesto razdvajanja je iza prvog simbola u trazi_se
print("Pozicija razdvajanja: " + str(poz) )
splajs_1:str = kod[:poz] # kod[0:poz]
splajs_2:str = kod[poz:] # kod[poz:len(kod)]
print("Rezultat: " + splajs_1 + "*" + splajs_2)