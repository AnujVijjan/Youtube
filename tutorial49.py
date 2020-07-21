class Student:

    holiday = 10

    def __init__(self):
        self.name = "Anuj"

    def output(self):
        print(self.name)

    @classmethod
    def set_holiday(cls):
        cls.holiday = 20


anuj = Student()

# anuj.output()
    
# anuj.set_holiday()
# print(anuj.holiday)

Student.set_holiday()

print(anuj.__dir__())

print(Student.holiday)

