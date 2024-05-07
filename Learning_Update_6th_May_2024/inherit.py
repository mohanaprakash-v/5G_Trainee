class Parent:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def moto(self):
        print(f"Parent is driving {self.name}")


class Child1(Parent):
    def __init__(self, name, age):
        super().__init__(name, age)
        print(f"Child1 is driving {self.name}")

class Child2(Parent):
    def __init__(self, name, age, valid):
        super().__init__(name, age)
        self.valid = valid
        print(f"Child2 is driving {self.name}")
        print(f"Child2 is driving {self.age}")
        

class Child3(Child1, Child2):
    def __init__(self, name, age, valid):
        super().__init__(name, age, valid)
        print(f"Hi {self.valid}")

obj1 = Child3("bike", 31, 21)
print(obj1.valid)