

class Panda:

    def __init__(self, Weight:int, Height:int, Habitat:str, Age:int):
        self.Weight = Weight
        self.Height = Height
        self.Habitat = Habitat
        self.Age = Age
    
    def information(self):
        print(f"The panda weight: {self.Weight}KG, Height: {self.Height}cm, Habitat: {self.Habitat}, and he is {self.Age} years old")
    
    
    def change_weight(self, weight:int):
        self.Weight = weight
