class Employee:

    def __init__(self):
        print("Constructor Called")

    def __del__(self):
        print("Destructor Called, Employee Deleted!")


def func1():
    emp = Employee()
    emp.__del__()

def func2():
    emp = Employee()
    emp.__del__()

func1()

func2()

