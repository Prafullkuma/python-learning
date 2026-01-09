# already leearned in the data-type py file Go check
# 

users= ["Prafull","Revan","Google"]

print("Prafull" in users)

print(users.index("Revan"))

print(users[-3: -1])
print(users[1:])
print(len(users))

users.append("Fixed")

print(users,"Appended")

users += ["Facebook"]
print(users)


users.extend(["roberst","gimmy"]) # return None
print(users)

#Edge case 
rockband =["one","directions"]
rockband += "chainsmooker"
#Edge case 


rockbandForMethod =["one","directions"]

print(rockbandForMethod.count("one")) # return count 
print(rockbandForMethod.insert(2, "one")) # return None
print(rockbandForMethod.pop(1))  # return popped values
print(rockbandForMethod,"HELLO")


rockbandForMethod[2:2] = ["Martin garix", "AKON"]
rockbandForMethod[1:3] = ["King", "Luther"]

print(rockbandForMethod,"HELLO")

rockbandForMethod.remove("King")
print(rockbandForMethod)

del rockbandForMethod[0]
print(rockbandForMethod)

# del rockbandForMethod # remove eveything 
# rockbandForMethod.clear()

rockbandForMethod.sort()

rockbandForMethod[3:] = ["Drafull"]
rockbandForMethod.sort(key=str.lower)
print(rockbandForMethod)
nums = [2,2,3,456,32,3,23,5,2]

nums.reverse()
print(nums)

nums.sort(reverse=True)
print(nums)

# creating a new copy 

print(sorted(nums, reverse=True)) # creates a new copy 
print(nums)

numsCopy = nums.copy()
myNums = list(nums)
myCopy = nums[:]

print(numsCopy)
print(myNums)
print(myCopy)

myList = list(["Helloe",231, "faceboos",False])

print(myList)

