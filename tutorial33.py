# tutorial33.py
import demo

# print(__name__)

# print("Hello from Python")

# print(demo.add(10, 20))

print(dir(demo))



# demo.py
def add(a,b):
    return a + b

def sub(a, b):
    return a - b

def greetings():
    print("Hello from demo module")


# print(__name__)
if __name__ == "__main__":
    greetings()

# print("Hello from demo module")
