# Question:- Take two numbers as an input from the user, store them in two variables. 
# Then swap the values of both the variables.

a = int(input ("first value"))
b = int(input ("second value"))

print("Before Swapping: ")
print("a = ",a)
print("b = ",b)

a,b = b,a

# temp = a
# a = b
# b = temp
# c , d = 10, 20

print("After Swapping: ")
print("a = ",a)
print("b = ",b)
