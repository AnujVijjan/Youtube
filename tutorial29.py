# my_fun = lambda a: a + 10


# print(my_fun(20))

# mul = lambda a, b: a * b

# print(mul(10, 20))


# add = lambda a, b, c: a + b + c

# print(add(1,2,3))

def my_func(n):
    return lambda a : a * n


# mydoubler = my_func(2)


# print(mydoubler(10))


mytripler = my_func(3)

print(mytripler(10))
