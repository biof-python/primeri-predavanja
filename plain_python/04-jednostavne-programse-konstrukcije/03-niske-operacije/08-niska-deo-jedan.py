genetski_kod:str = "AGTTCGTAAGATGTGTCC"
print(genetski_kod)

# trazimo treci, peti i petnaesti znak
treci:str = genetski_kod[2]
peti:str = genetski_kod[4]
petnaesti:str = genetski_kod[14]
print(treci + peti + petnaesti)

# ovo dovodi do izuzetka
#znak_25:str = genetski_kod[24]
#print(znak_25) 

# trazimo treci od pozadi
znak_3p:str = genetski_kod[-3]
print(znak_3p)
