genetski_kod:str = "AGTTCGTAAGATGTGTCCAGTCGAA"
print("Original:   " + genetski_kod)
s1=genetski_kod.replace("T", "a")
s2=s1.replace("A", "t")
s3=s2.replace("G", "c")
s4=s3.replace("C", "g")
s5=s4.upper()
print("Komplement: "+ s5)

#malo krace
print("---")
s:str = "AGTTCGTAAGATGTGTCCAGTCGAA"
print("Original:   " + s)
s = s.replace("T", "a")
s = s.replace('A', 't')
s = s.replace('C', 'g')
s = s.replace('G', 'c').upper()
print("Komplement: "+ s5)

#jos krace
print("---")
so:str = "AGTTCGTAAGATGTGTCCAGTCGAA"
print("Original:   " + so)
sk:str = so.replace("T", "a").replace('A', 't').replace('C', 'g').replace('G', 'c').upper()
print("Komplement: "+ sk)

