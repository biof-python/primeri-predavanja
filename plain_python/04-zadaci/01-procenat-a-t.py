# odrediti procenat A, procenat T i procenat AT u genetskom kodu
genetski_kod:str = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCATGG"
print("Genetski kod: '" + genetski_kod + "'")

procenat_a:float = genetski_kod.count("A")/len(genetski_kod) * 100
print("Procenat 'A': " + str(procenat_a) + "%")

procenat_t:float = genetski_kod.count("T")/len(genetski_kod) * 100
print("Procenat 'T': " + str(procenat_t) + "%")

procenat_at:float = genetski_kod.count("AT")/len(genetski_kod) * 100
print("Procenat 'AT': " + str(procenat_at) + "%")

procenat_ta:float = genetski_kod.count("TA")/len(genetski_kod) * 100
print("Procenat 'TA': " + str(procenat_at) + "%")
