class A:
    x = 10

    def __init__(self):
        print(self.x)

    def get_x(self):
        return self.x


class B(A):
    y = 20

    def __init__(self):
        print(self.y)

    def get_y(self):
        return self.y


# a = A()

# print(a.get_x())

b = B()

# print(b.get_y())

# print(b.get_x())

# print(b.x)
