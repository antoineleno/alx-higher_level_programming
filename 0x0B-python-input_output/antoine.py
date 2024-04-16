class Student:
    def __init__(self, name, age):
        self.age = age
        self.name = name


Student_1 = Student("Antoine", 54)
name = getattr(Student_1, "name")
age = getattr(Student_1, "age")

print(name, age)

