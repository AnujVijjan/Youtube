from functools import reduce

def add(a,b):
    return a + b

myList = [1,2,3,4,5]

# s = myList[0]

# for i in myList[1:]:
#     s = add(s, i)

# s = reduce(add, myList)

# s = reduce(add, myList, 20)

s = reduce(lambda a, b, c: a - b, myList)
print("Addition: ", s)
