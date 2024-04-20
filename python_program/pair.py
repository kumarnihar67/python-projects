first_list = [5,6,7,8,9,10,11,12]
print("First list ", first_list)

second_list = [25,36,49,64,81,100,121,144]
print("second list ", second_list)

result = zip(first_list,second_list)
result_set = set(result)
print(result_set)