class Panda:
    
    #constructor:
    def __init__(self,name:str,gender:str,age:int,fav_food:str) -> None:
        self.name = name
        self.gender = gender
        self.age = age
        self.fav_food = fav_food
        
    #methods/functions
    def display(self):
        introduce = f"The panda name is {self.name} and it a {self.gender}, {self.name} is {self.age} years old ."
        return introduce
    
    def my_fav_food(self):
        food = f"The panda likes to eat {self.fav_food}"
        return food