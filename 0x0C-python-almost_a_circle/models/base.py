#!/usr/bin/python3
"""base"""
import json
import csv
import turtle
class Base:
    """Base class"""
    __nb_objects = 0
    def __init__(self, id=None):
        """Constructor method

        Args:
            id (int): _id to set if exist. Defaults to None.
        """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id
    @staticmethod
    def to_json_string(list_dictionaries):
        """to json string: method to convert a string to json"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """method to save a file to json"""
        filename = cls.__name__ + ".json"
        with open(filename, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                jsonfile.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """method to convert a json string to its original form"""
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """method to create a class instance"""
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        """method to load a file from json representation"""
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []
    
    @classmethod
    def save_to_file_csv(cls, list_objs):
        """method to save to csv"""
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as file:
            writer = csv.writer(file)
            for obj in list_objs:
                if cls.__name__ == "Rectangle":
                    writer.writerow([obj.id, obj.width, obj.height, obj.x, obj.y])
                elif cls.__name__ == "Square":
                    writer.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        filename = cls.__name__ + ".csv"
        instances = []
        try:
            with open(filename, "r", newline="") as file:
                reader = csv.reader(file)
                for row in reader:
                    if cls.__name__ == "Rectangle":
                        obj = cls.create(width=int(row[1]), height=int(row[2]), x=int(row[3]), y=int(row[4]), id=int(row[0]))
                    elif cls.__name__ == "Square":
                        obj = cls.create(size=int(row[1]), x=int(row[2]), y=int(row[3]), id=int(row[0]))
                    instances.append(obj)
        except FileNotFoundError:
            pass
        return instances
    
    @staticmethod
    def draw(list_rectangles, list_squares):
        """method to draw a list of rectangle and list of square"""
        screen = turtle.Screen()
        screen.setup(width=800, height=600)
        screen.title("Drawing Rectangles and Squares")
        turtle.bgcolor("black")
        turtle.color("green")
        j = 1
        for rectangle in list_rectangles:
            for i in range(4):
                if i % 2 == 0:
                    turtle.forward(rectangle.width)
                    turtle.right(90)
                else:
                    turtle.forward(rectangle.height)
                    turtle.right(90)

            turtle.penup()
            turtle.goto(j * 150, 0)
            turtle.pendown()
            j += 1

        turtle.penup()
        turtle.goto(0, -300)
        turtle.pendown()
        k = 1
        for square in list_squares:
            for i in range(4):
                turtle.forward(square.size)
                turtle.left(90)
            turtle.penup()
            turtle.goto(k * 150, -300)
            turtle.pendown()
            k += 1
        
        turtle.hideturtle()
        turtle.done()