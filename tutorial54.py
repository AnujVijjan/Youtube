class Father:

    surname = "xyz"
    def __init__(self):
        self.father_name = "xyz"

class Mother:

    def __init__(self):
        self.mother_name = "abc"

class Child(Father, Mother):

    def __init__(self):
        self.child_name = "pqr"

    def diplay(self):
        # print(self.father_name)
        # print(self.mother_name)
        # print(self.child_name)
        print(self.surname)
father = Father()

mother = Mother()

child = Child()

child.diplay()
