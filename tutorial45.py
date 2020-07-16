class Student:
    student_name = ""
    def accept(self):
        self.student_name = "Anuj"
        print("accept function called")


anuj = Student()


anuj.accept()

# Student.accept(anuj)

print(anuj.student_name)
