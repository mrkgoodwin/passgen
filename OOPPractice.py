from sre_constants import JUMP


class Dog:
    def __init__(self, name) -> None:
        self.name = name
        print(name)
    def add_one(self, x):
        return x + 1

    def bark(self):
        print("bark")
# d = Dog()
# print(type(d))
# d.bark()
# print(d.add_one(5))
d = Dog("Tim")
d2 = Dog("Bill")