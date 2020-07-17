class Student:
    # student_name = ""

    # def __init__(self):
    #     print("init constructor called!")

    # def __init__(self):
    #     self.student_name = "Anuj"

    # def __init__(self, name):
    #     self.student_name = name

    def __init__(self, name="Anuj"):
        self.student_name = name

        
# print(Student.student_name)
anuj = Student("Anuj")

# anuj.__init__()

print(anuj.student_name)
