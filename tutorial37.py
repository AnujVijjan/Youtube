def myFunc(x):
    if(x > 18):
        return True
    else:
        return False

age = [11,12,14, 19, 25, False, True, 1, 0]

# for i in age:
#     if(myFunc(i)):
#         print(i)

# print(list(filter(myFunc, age)))

# print(tuple(filter(myFunc, age)))

# for i in filter(myFunc, age):
#     print(i)

print(list(filter(None, age)))
