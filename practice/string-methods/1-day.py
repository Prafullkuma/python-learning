
# strip

txt = " banana  "


txt2= ",,,,,......posps.....banan.......ssslss"

txt3= ",,,,,allkas.....banana.......ssslss"

txt4= "ppps.....helow...qqqqqqq"

# strip()
print(txt.strip())
print(txt2.strip(",alks."))
print(txt3.strip(",alks."))
print(txt4.strip("psq."))


# lstrip()
print(txt.lstrip()) # output - banana   
print(txt2.lstrip()) #output - ,,,,,......posps.....banan.......ssslss
print(txt2.lstrip(",.pos")) # output - banan.......ssslss
print(txt3.lstrip(",.")) # output - allkas.....banana.......ssslss
print(txt4.lstrip("ps.")) #output -  helow...qqqqqqq



# rstrip()
print(txt.rstrip()) # output -    banana
print(txt2.rstrip()) #output - ,,,,,......posps.....banan.......ssslss
print(txt2.rstrip(",.pos")) # output - ,,,,,......posps.....banan.......sssl
print(txt3.rstrip(",.sl")) # output - ,,,,,allkas.....banana
print(txt4.rstrip("ps.q")) #output -  ppps.....helow

