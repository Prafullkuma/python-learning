# String Data type

# literal assingment

first = "Prafull"
second = "Bhendwade"
print(type(first))

print(type(first))
print(type(first) == str)
print(isinstance(first, str))


# constructor functions 

print("--------- constructor functions---------")

pizza = str("Google Pizza")

print(type(pizza))
print(type(pizza) == str)
print(isinstance(pizza, str))


# concatination 
print(" ------- concatination ---------- ")

fullName = first +" "+ second 

print(fullName)

print(fullName + " "+ "Hello")


print(" ------- casting ---------- ")

# casting a number to string 
decade = str(192132123)

print(decade,"DECADe")

print(" ------- using it casting ---------- ")

mysentence = "I am poor, need to earn more money " + decade
print("Yes it is") if isinstance(decade, str) else print("No its not")
print(mysentence)

print(" ------- Mult line ---------- ")

multiline = '''


Hey its me, do even remember me   


i was just checking in 


                            all Good?


'''
print(multiline)


print(" ------- Escaping special character ---------- ")

sentence = 'I\'m back at work!\t hey \n \n Good moring \\located'

print(sentence)

