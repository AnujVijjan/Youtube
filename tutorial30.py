def fact(n):
    factorial = 1
    if(n < 0):
        print("Factorial of a negative number is not possible")
    elif(n == 0):
        return factorial
    else:
        for i in range(n, 0, -1):
            factorial = factorial * i

        return factorial


n = int(input("Enter a number: "))


result = fact(n)


print(f"Factorial of {n} is : ", result)
