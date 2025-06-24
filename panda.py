class Panda:
    name = None
    age = None
    gender = None
    color = None
    weight = None

    def __init__(self, name:str, age:int, gender:str, color:str, weight:str ):
         self.name = name
         self.age = age
         self.gender = gender
         self.color = color
         self.weight = weight

    def eat(self):
        print("The panda is eating")

    def sleep(self):
        print("The panda is sleeping")