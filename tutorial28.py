# def my_func():
#     """ Do nothing, but document it. """

# print(my_func.__doc__)

# def add(a , b):
#     print("Hii")
#     """ This function return the addtion of two varibles. """
#     return (a + b)

# print(add.__doc__)
# # print(add(10, 20))

def add(a:"First Value" , b: "Second Value") -> "This function returns addition of two numbers":
    return a + b


print(add.__annotations__)
# print(add("a", "b"))


