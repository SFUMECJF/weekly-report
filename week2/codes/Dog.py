class Dog:
    def __init__(self):
        self.name = "name"
        self.age = "age"

    def bark(self):
        print("Woof!")

    def __str__(self):
        return "Dog: " + self.name + "age :" + self.age

def test_into():
    pass