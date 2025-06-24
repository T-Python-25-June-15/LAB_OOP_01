# created panda class
class Panda:

    # constructor
    def __init__(self,name:str,age:int,weight:int,food:str):
        self.name = name
        self.age = age
        self.food = food
        self.weight = weight

    # methods
    # Display the panda's information
    def display(self):
        print(f"Name: {self.name}, Age: {self.age}year, Weight: {self.weight}kg, Food: {self.food}")

    # Display the panda's food
    def eat(self):
        print(f"{self.name} is eating {self.food} and his weight is {self.weight}.")




