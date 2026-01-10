# similar to object 
# when dict having duplicate key an try to get the print(len(band)) then it will consider as one other duplicates it will ignore 

# What it is 
# how to use 
# What it return 
# what will happen

band = {
    "rockstart":"India",
    "Post mallon": "USA",
}

band2 = dict(rockstar="India", postmallon = "USM")


print(band)
print(band2)
print(len(band))

print(type(band2))
print(isinstance(band2, dict))


# accesing 

print(band["rockstart"])
print(band.get("Post mallon")) 
print(band.keys()) # return list
print(band.values()) # return list 

# List of key value pair as tuple 

print(band.items(),"LAST")

# verify key exists 

print("rockstart" in band)
print("rockstar" in band)

#change values in th dict 


band["Post mallon"] = "DATA Science"
print(band)

band2.update({ "base": "JPJ"})
print(band2)

# removing 

# band2.pop() # invalid need to give one value 
band2.pop("base")
print(band2)

band2["Peoplex"] = "Notchangeing"

print(band2)

print(band2.popitem()) # remove last key value pair from the dict return tuple
print(band2)

# deleteing 


del band2["rockstar"] 
print(band2)

band2.clear() # clear still having space in the memory

del band2 # remove from the memory


#Copying Dict


# band2 = band  # create referece ( both are point to same memory reference, if you change at once place it will change to other also)
# print("Bad copy")

# print(band)
# print(band2)

# band["copy"] ="Not"
# print(band)
# print(band2)


# better way 
band2 = band.copy() #only one place it will change  band2 

band2["hello"] = "facebook"

print(band)
print(band2)

# or use the dict() constructor function 

band2 = dict(band)

band2["facebook"] = "delta"
print(band)
print(band2)


# Nested dictionary 



member1 = {
    "name":"Prafull",
    "job":"software"
}


member2 = {
    "name":"Revan",
    "job":"Army"
}

brothers ={
    "member1": member1,
    "member2": member2
}

print(brothers)

print(brothers["member2"]["name"])
