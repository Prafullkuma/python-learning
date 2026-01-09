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

print("----- LIST type (Array)  ------")

myList = ["One", "two", 213, False, 213.22]


print(myList[2]) # return single number 
print(myList[1:5]) # return new list 
print(myList[:]) # copying everything or in JS ... spread operator)

myList1 = myList # just copy the reference if change one list it will affect to other to 

myList1[0] = "Figma"
myList1.append(4) # add at last
 
print(myList1, myList,"changes in the both")

# creating (shollow copy)
myList3 = myList[:]  # this will create a new list 

print(myList3)


print(myList3 * 3)
print([myList3] * 3) # create 2 dimentional array [[1,3,2,2],[2,2,2,2]]


print("----- Tuples type (immutable)  ------")
# basically use for fixed data like ,coordinates, db records (tuple are faster and memory efficient)
empty_tuple = ()

coordinates = (10,20,30)


coordinates2= 10.2,30.3,20

mixed_tuple =(2,"Prafull", "HELLOE", False)

fileName="Image.pgn"
if fileName.endswith((".pgn",".gif")):
    print("I am working")
else:
    print("I am not working")

print(empty_tuple, coordinates, coordinates2)

# Tuples can be use in the dictionary 
location_dict = {("New york","DATA"):"Big Apple"}
print(location_dict[("New york","DATA")])

a, b = 10, 20
a, b = b, a
print(a,b) 
