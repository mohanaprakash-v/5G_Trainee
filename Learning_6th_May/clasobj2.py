class person():

    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def info(self):
        print(f"My name is {self.name} and my age is {self.age}")

person1 = person(name="Mohan", age=22)
person1.info()
person2 = person(name="Kavi", age=21)
person2.info()