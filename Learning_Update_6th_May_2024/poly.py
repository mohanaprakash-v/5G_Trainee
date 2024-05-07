#program to find which birds can fly and cannot fly using a single function using polymorphism concept

class Birds():
    def info(self):
        print("There are different species of birds living in the world")
    def fly(self):
        print("some can fly and some cannot fly")
    
class crow(Birds):
    def fly(self):
        print("crow can fly")

class duck(Birds):
    def fly(self):
        print("duck cannot fly")
    
obj1 = Birds()
obj2 = crow()
obj3 = duck()

obj1.info()
obj1.fly()

obj2.fly()
obj3.fly()