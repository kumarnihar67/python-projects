numbers = [20,50,45,175,145,510,575,30]
for i in numbers:
    if i > 500:
        break
    elif i > 150:
        continue
    elif i % 5 == 0:
        print(i)
    