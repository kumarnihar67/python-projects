list = [5,6,3,5,6,11,3,9,0,11,8,0,11]
print("original list ",list)

count_dict = dict()
for item in list:
    if item in count_dict:
     count_dict[item] += 1
    else:
     count_dict[item] = 1
    print("printing count of item ", count_dict) 
