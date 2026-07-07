'''
s={2,4,6}
print(s)
print(type(s))
info = {"Carla", 19, False, 5.9, 19}
print(info)

david = set()
print(type(david))

for value in info:
    print(value)

'''
#this a sets in python

#s1 = {1, 2, 3, 4, 5}
#s2 = {4, 5, 6, 7, 8}    
#print(s1.union(s2)) # elements in either s1 or s2
#print(s1.intersection(s2)) # elements in both s1 and s2
#print(s1.difference(s2)) # elements in s1 but not in s2
#print(s1.symmetric_difference(s2)) # elements in s1 or s2 but not in both
#s1.remove(5)
#del s1
#print(s1) # this will raise an error because s1 has been deleted    
#s1.update(s2)
#print(s1)
#print(s1, s2)

info = {"Carla", 19, False, 5.9, 19}
if "Carla" in info:
    print("Carla is in the set")
else:
    print("Carla is not in the set")    