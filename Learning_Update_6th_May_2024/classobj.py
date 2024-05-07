class dog:
    pass

    def __init__(self, dname):
        self.dogname = dname

    def sleep(self, time):
        self.sleephrs = time

obj1 = dog(dname="Beagle")
obj1.sleep(time=8)

print("My Dog Name is",obj1.dogname)
print("My Dog sleeps",obj1.sleephrs, "hours a day")