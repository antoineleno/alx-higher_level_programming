class MyObject1:
    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        return super().__ne__(other)

    def __ne__(self, other):
        return super().__eq__(other)

class MyObject2:
    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        return super().__ne__(other)

    def __ne__(self, other):
        return super().__eq__(other)

# Create instances
obj1 = MyObject1(5)
obj2 = MyObject2(10)

# Use the overridden methods in a custom function
def compare_values(x, y):
    print(f"{x.value} == {y.value}: {x == y}")
    print(f"{x.value} != {y.value}: {x != y}")




compare_values(obj1, obj2)
