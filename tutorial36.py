def sqr(item):
    return item * item


l1 = [1,2,3,4,5]
l2 = [6,7,8,9,10]
# for i in l1:
#     print(sqr(i))


# s = map(sqr, l1)

# s = map(lambda x: x+2, l1)

def add(a, b):
    return a+ b

# print(list(map(add, l1, l2)))

a = ["1", "2", "3", "4"]

# b = "1"
# print(int(a[0]))
print(a)
print(list(map(int, a)))
# print(tuple(s))
