class Panda:
    # Initilizer 
    def __init__(self, name:str, age:int, alive:bool, weight:float):
        self.name = name
        self.age = age 
        self.alive = alive
        self.weight = weight
     
    # Methods   
    def intro(self)-> str:
        condition_alive = "Alive" if self.alive else "Dead"
        condition_age = self.age if self.age >= 0 else "Invalid age!"
        condition_weight = self.weight if self.weight >= 0 else "Invalid weight!"

        return f"""
    Name    :   {self.name}
    Age     :   {condition_age}
    Status  :   {condition_alive}
    Weight  :   {condition_weight}
    """
    
    def life_time(self)-> str:
        if 0 <= self.age < 2:
            return "The panda is a Baby"
        elif 2 <= self.age < 5:
            return "The panda is Young"
        elif self.age >= 5:
            return "The panda is an Adult"
        else:
            return "Invalid age!!"