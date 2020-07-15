class College:
    college_name = "xyz"


x = College()

x.branch = "Computer"

# print(x.branch)

# print(x.college_name)

y = College()
y.branch = "Electrical"

# print(y.branch)
# print(x.__dict__)
# print(y.__dict__)

x.college_name = "abc"

# print(x.college_name)
# print(y.college_name)
# print(x.__dict__)

College.college_name = "abc"

# print(x.college_name)
print(y.college_name)
# print(College.college_name)
