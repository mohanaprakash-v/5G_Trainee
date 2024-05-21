from abc import ABC, abstractmethod 
class parent(ABC):
    @abstractmethod
    def __init__(self):
        return "parent class"

class child(parent):
    @property
    def geek(self):
        return "child class"

    
try:
    obj = parent()
    print(obj.geek)
except Exception as error:
    print(error)

obj = child()
print(obj.geek)