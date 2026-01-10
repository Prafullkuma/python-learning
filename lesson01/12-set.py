
# Set 

nums = {1, 2, 3, 4, 5 }
nums2 = set((1,2,3,4,4,3)) # No duplicates are allowed

print(nums)
print(type(nums))
print(isinstance(nums2, set))

# no duplicates are allowed 

nums3 = {1, 2, 3, 4, 4, 45}

print(nums3)

# True is consider 1 and False is considered at 0 

nums4 = {1, True, 2, 3, False, 0, 4 } 

print(nums4)

# check value is the set 

# we can able to refer with index or key 
print(False in nums4)


# add new values in set 
print(nums4.add(100))

print(nums4)

# update 

moreenums = { 5,4,6 }
nums4.update(moreenums)

print(nums4)

#we can use update with list tuples and dict too 



#merge two set and return new set 

one = { 1,2,3 }
two = { 4,5,6 }

mynewSet = one.union(two)

print(mynewSet)

# Keep only duplicates 
one = { 1,2,3 }
two = { 1,2,6 }

one.intersection_update(two)

print(one)

# Keep everything except the duplicates 


one = { 1,2,3}
two = { 2,3,4}

one.symmetric_difference_update(two)
print(one)
