a = 50
b = 60
c = 40
# if(a > b): print("a is greater than b") # Short Hand if 
# if(a > b):
#      print("a is greater than b")

# print("a is greater than b") if(a > b) else print("b is greater than a") # Short Hand If else
# if(a > b):
#     print("a is greater than b")
# else:
#     print("b is greater than a")

# print("a is greater than b") if(a > b) else print("Both are equal") if(a == b) else print("b is greater than a") 
# if(a > b):
#     print("a is greater than b") 
# else:
#     if(a == b):
#         print("Both are equal") 
#     else:
#         print("b is greater than a") 

print("a is greater") if(a > b and a > c) else print("b is greater") if(b > c) else print("c is greater")
