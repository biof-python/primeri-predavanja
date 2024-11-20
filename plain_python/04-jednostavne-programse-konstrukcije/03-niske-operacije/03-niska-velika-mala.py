z:str = "Zdravo"
s:str = "lepi svete"
z_velika = z.upper()
z_mala = z.lower()
print( z_velika + "," + z_mala + ", " + z + "\n" + s)
d = len(z_velika)
# ovo dovodi do greske AttributeError: 'int' object has no attribute 'lower' 
# print( d.lower())