# arithmetic_operations.py
def add(*args):
    s = 0
    for i in args:
        s = s + i
    return s

def sub(a, b):
    return a - b

def div(a, b):
    return a / b

def mul(a, b):
    return a * b

def mod(a, b):
    return a % b

def floor_div(a, b):
    return a // b



# tutorial32.py
import arithmetic_operations as aop


print("Addition: ", aop.add(2, 3, 4, 10, 15,16))
print("Subtraction: ", aop.sub(2, 3))
print("Division: ", aop.div(2, 3))
print("Multiplication: ", aop.mul(2, 3))
print("Modules: ", aop.mod(2, 3))
print("Floor Division: ", aop.floor_div(2, 3))
