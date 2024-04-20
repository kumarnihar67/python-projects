first_list = [25,35,45,55,65,75]
print("original list", first_list)

first_list = list(set(first_list))
print("unique list", first_list)

t = tuple(first_list)
print("tuple", t)
print("maximum number is:", max(t))
print("minimum number is:", min(t))