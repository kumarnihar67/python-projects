first_set = {2,5,8,11,22,45,0,100,81}
second_set = {57,8,5,11,45,11,78,90, 48}

print("First Set ", first_set)
print("Second Set ", second_set)

intersection = first_set.intersection(second_set)
print("Intersection is ", intersection)
for item in intersection:
    first_set.remove(item)

print("First Set after removing common element ", first_set)