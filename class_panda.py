class panda:

    def __init__(self ,name:str ,  height:float , weight:float ,color:str):
        self.name = name
        self.height = height
        self.weight = weight
        self.color = color
    
    def describe(self) -> str:
        return f"the panda weight is {self.weight} kg and it's hight is {self.height} cm and he has {self.color} color"

    def panda_name(self) -> str :
        return f"the panda nickname is {self.name}"


    