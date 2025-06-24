class Panda:
    #define attributes
    def __init__(self, age:int, eat:str, country:str, sex:str)->None:
        self.age = age
        self.eat = eat
        self.country = country
        self.sex = sex

    #create methods
    def panda_description(self):
        description = f"This panda is {self.sex} it is {self.age} ago , it is from {self.country}.This panda can eat {self.eat}. "
        return description
    
    def panda_country(self):
        text = f"This panda live in {self.country}."
        return text