sah:list[str] = ["kralj", "kraljica", "top", "laufer", "skakac", "pion"]
print(sah)

donji_red:list[str] = sah[0:5]
print(donji_red)

kraljevski_par:list[str] = sah[0:2]
print(kraljevski_par)

napadaju_ukoso:list[str] = []
napadaju_ukoso.append(sah[0])
napadaju_ukoso.append(sah[1])
napadaju_ukoso.append(sah[3])
napadaju_ukoso.append(sah[5])
print(napadaju_ukoso)


