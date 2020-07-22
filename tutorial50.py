class Calculator:

    C = 10
    def add(self, a, b):
        return a + b

    
    @staticmethod
    def info():
        print("This is info class")
        
    
cal = Calculator()

# print(cal.add(10, 30))

# cal.info()

Calculator.info()
