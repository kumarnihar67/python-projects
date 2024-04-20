def check(t):
    return all(i == t[0] for i in t)

tuple1 = (5, 4, 5, 5)
print(check(tuple1))