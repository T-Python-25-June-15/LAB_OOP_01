
class Panda:

    def __init__ (self , name , age , weight , healthPercentage):
        self.name = name
        self.age = age
        self.weight = weight
        self.healthPercentage = healthPercentage


    def pandaInfo(self):
        print(f"# Panda Information: ")
        print(f"- Name: {self.name}.")
        print(f"- Age: {self.age}.")
        print(f"- Weight: {self.weight}KG.")
        print(f"- Health Percentage: {self.healthPercentage}%.")

    def healthCondition(self):
        if self.healthPercentage >= 80:
            print(f"Health percentage of {self.name} is: {self.healthPercentage}, which means it's Excellent!")
        elif self.healthPercentage >= 50:
            print(f"Health percentage of {self.name} is: {self.healthPercentage}, which means it's Normal!")
        else:
            print(f"Health percentage of {self.name} is: {self.healthPercentage}, which means it's Bad!")