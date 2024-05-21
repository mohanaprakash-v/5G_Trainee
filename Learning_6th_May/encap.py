class Parent:
    def __init__(self):
        self.public = "Hi"
        #self.__name = "Hello"

class Child(Parent):
    def __init__(self):
        super().__init__()
        print(self.public)

obj1 = Parent()
obj2 = Child()
print(obj2.public)
    