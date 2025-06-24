
class Panda:
    def __init__(self, name:str , age:int, weight:int , bamboo_eaten : int) -> None:
        self.name = name
        self.age = age
        self.weight = weight
        self.bamboo_eaten = bamboo_eaten

    def eat_bamboo(self, amount):
        self.bamboo_eaten = self.bamboo_eaten + amount
        print(f"{self.name} ate {amount} kg of bamboo. Total bamboo eaten: {self.bamboo_eaten} kg.")

    def sleep(self, hours):
        print(f"{self.name} is sleeping for {hours} hours. Zzz...")
