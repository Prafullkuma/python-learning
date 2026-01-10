# while loop 


# value = 1
# while value <= 10: 
#     print("I am here", value)
#     if value == 5:
#         break  # exit form the loop dont even start with next else part 
#     value += 1 


# value = 1
# while value <= 10: 
#     value += 1 
#     if value == 5:
#         continue # Skip one step 
#     print("I am here", value)
# else:
#     print(" value is not equal", value)



# For Loop 


# names = ["Prafull", "Revan", "Bindu"]
# for name in names:
#     if name == "Revan":
#         break
#     print(name)
    
# for name in names:
#     if name == "Revan":
#         continue # Skips 
#     print(name)
    
# for letter in "Google":
#     print(letter)


    

# for x in range(4): # start with 0 
#     print(x)


for x in range(4, 10): # start at 4 stops 10 (not include 10)
    print(x)


for x in range(0, 100, 5): # start at 0 and till end 100 and increament by 5 
    print(x)
else:
    print("Glad end")

names = ["Prafull","Revan", "Bindu"]
actions =["Code", "eats", "Sleeps"]

# name will iterate on each actions elements 
for name in names:  
    for action in actions:
        print(name+" "+ action)