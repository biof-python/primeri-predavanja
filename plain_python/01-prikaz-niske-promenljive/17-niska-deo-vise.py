genetski_kod:str = "AGTTCGTAAGATGTGTCCAGTCGAA"
print(genetski_kod)

# trazimo podnisku sa elementima od sedmog do dvanaestog
od_7_do_12:str = genetski_kod[6:11]
print(od_7_do_12)

# trazimo podnisku sa elementima od petog do kraja niske
od_5_do_kraja:str = genetski_kod[4:len(genetski_kod)]
print(od_5_do_kraja)

# trazimo podnisku sa elementima od desetog do kraja niske
od_10_do_kraja:str = genetski_kod[11:]
print(od_10_do_kraja)

# trazimo podnisku sa elementima iz druge polovine niske
duzina:int = len(genetski_kod)
pola:int = int(duzina/2)
druga_polovina:str = genetski_kod[pola+1:duzina]
print(druga_polovina)