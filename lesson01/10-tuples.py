#Tuples are same like a list, but they are immuatables 
# Data will not change or order also will not changes 
# defined with ()
# can be 29,232,2,23,23


myTuple = tuple(("Dave",2,232,True)) #packing a tuple 

anthorTuple = (1,2,3,4)


print(myTuple)
print(anthorTuple)
print(type(myTuple))


newList = list(myTuple) # we can able to update tuple but need to use list

newList.append("SSS")

newTuple = tuple(newList)

# newTuple.append("SSS") throws an error 
print(newTuple)

(one, two, *hey) = anthorTuple #destructuring
(one, *two, hey) = anthorTuple #destructuring


print(one,"ONE")
print(two,"two")
print(hey,"hey")


mynewTuple =(21,2,12,2,12)

print(mynewTuple.count(21))  # count occurences 

print(mynewTuple)