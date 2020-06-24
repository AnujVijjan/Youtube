# def my_func(a, b):
#     print(a, b)

# my_func(10,b = 20)
# my_func(a = 10, b = 20)

# my_func(a = 10, 20)
# my_func(10, a = 20, b = 30)
# my_func(a = 10, c = 30)

# def my_func(a, b, c, d):
#     print(a, b, c, d)

# def my_func(*args):
#     print(args[1])

# my_func(10, 20, 30, 40, 50, 60)

# def my_func(**kwargs):
#     print(kwargs)

# myDict = {'a' : 10, 'b' : 20}
# my_func(**myDict)

# def pos_only_arg(a, /):
#     print(a)

# pos_only_arg(10)

def kwd_only_args(*, a):
    print(a)

kwd_only_args(a = 10)
