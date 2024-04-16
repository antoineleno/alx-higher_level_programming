class Student:
    instances = []
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.instances.append(self)

    def to_json(self):
        return self.__dict__
    
    @classmethod
    def show_instance(cls):
        my_list = []
        for instance in cls.instances:
            my_list.append(instance.to_json())
        
        print(my_list)


Student_1 = Student("Antoine", 55)
Student_2 = Student("Theophile", 65)
Student_3 = Student("Madeleine", 65)

Student.show_instance()
