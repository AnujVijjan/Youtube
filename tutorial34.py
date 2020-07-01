def outer(num): # Outer Function

    def inner(): # Inner Function
        return num + 10
    
    num1 = inner()
    print(num, num1)

outer(20)

# inner() Error
