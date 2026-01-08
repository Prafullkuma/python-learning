sentence = 'I\'m back at work!\t hey \n \n Good moring located'
fimga = "I am figma"

print(" ------- String methods special character ---------- ")

print(sentence.upper()," UPPPER")
print(sentence.lower(),"LOWER")
print(sentence.title(),"TITLE")
print(sentence.replace("back", "not back"))

print(fimga.replace("figma","figma again dasdasdasd"),"HLLLEEEOOOO")

print(len(sentence))  # consider spaces also




print(" ------- remove spaces ---------- ")



multiline1 = ''' data adasdasd     dasdasd  '''

print(len(multiline1.strip()))
print(len(multiline1.lstrip()))
print(len(multiline1.rstrip()))

print("")
print("")

print(" ------- aligning text ---------- ")

title = "memu"

print(title)
print(title.center(12,"-"))
print("Lust".ljust(21,"@"))
print("Lust Want".rjust(21,"@"))

print("")
print("")
print("")
print("")




print(" ------- eg: aligning text ---------- ")

print("==== my bill=====")

mybill = "bill"

print(mybill.center(24,"="))
print("Dosa".ljust(20,".") + "40₹".rjust(4))
print("Tea".ljust(20,".") + "60₹".rjust(4))
print("Total bill".center(24, "-"))
print("100".rjust(24))

print("")
print("")
print("")

print(" ------- String index values ---------- ")

myName = "Prafull"

myName1 = "Revan"


print(myName[1]) 
print(myName[-1]) # get the last letter 
print(myName[1:-1]) # when we -1 it leave the last element and prints it 
print(myName[1:])  # stating from index 1 to till end of the word


# return boolean values


print(myName.startswith("21")) # false
print(myName.endswith("ll")) # True
print(myName1.endswith("ll")) # True


