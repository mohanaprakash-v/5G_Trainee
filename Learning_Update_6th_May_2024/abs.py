from abc import ABC

class types(ABC):
    def living(self):
        pass

class human(types):
    def living(self):
        print("Human")

class animals(types):
    def living(self):
        print("Animals")


obj2 = human()
obj2.living()
obj3 = animals()
obj3.living()
print(issubclass(human, types))
print(isinstance(obj2.living(),types))
