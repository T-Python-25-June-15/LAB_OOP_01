class Panda:
    
    
    def __init__(self, name:str,age:int, weight:int, is_endangered:bool):
        self.name= name
        self.age=age
        self.weight=weight
        self.is_endangered=is_endangered


    def introduce(self)-> str:
        return f"Panda information, name:{self.name}, age:{self.age}, weight:{self.weight}, is endangered: {self.is_endangered}"


    def calculateAgeinMonths(self):
        return int(self.age * 12)
        
