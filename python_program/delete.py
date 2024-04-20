number_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
for i in range(len(number_list) -1 ,-1 ,-1):
    if number_list[i] > 50:
        del number_list[i]
print(number_list)