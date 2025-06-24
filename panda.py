
class Panda:
    def __init__(self, name: str, age: str, gender: str, weight: float):
        self.name = name
        self.age = age
        self.gender = gender
        self.weight = weight


    def info(self):
        print(f"{self.name} is a {self.age} year old {self.gender} panda weighing {self.weight} kg.")
    def sleep(self, hours: int):
        print(f"{self.name} is sleeping for {hours} hours.")



