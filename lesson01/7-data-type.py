# strings type 

firstName = "Revan"
lastName = str("Bhendwade")

print(type(firstName))
print(isinstance(lastName, str))


# Boolean data type 
print("")
print("")
print("")
print("")

myvalue = True 
x = bool(False) # False 
x = bool(myvalue) # True 
y = bool(myvalue) # True 

print(x) # return true first x will be updated with second x
print(y) # r true


print(type(x))
print(type(x) == bool)
print(isinstance(y, bool))


# number 

best = 100
best_price = int(12032)

print(type(best))
print(isinstance(best_price, int))


# Float type 


gpa = 2.2
best_gpa = float(2.323423)

print(type(gpa))
print(isinstance(gpa, float))

# complex type real + imagenery (append j or J to imagenery part of the number)

complexType = 2j
complexType1 = complex(2,23423)
complexType2 = 2j

# complexType2 = 2+j  # NameErroor J is not defined 
# print(complexType2)
# Do not support < or > <= or >=  gives type error 
# it should not contain any spaces 
# values must valid complex number

print(type(complexType))
print(complexType1) # 2+23423j

print(isinstance(complexType1, complex))

print(complexType == complexType2)
print(complexType != complexType1)
print(complexType.real) # return in float values
print(complexType1.imag) # return in float values



print("----- squence type ------")


