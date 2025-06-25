class Panda:
    def __init__(self, name, age, tall, food): 
        self.name = name
        self.age = age
        self.tall = tall
        self.food = food
        
    def eating(self):
        print(f"{self.name} eating {self.food} right now!")

    def information(self):
        print(f"\nPerson Information:\nName: {self.name}\nAge: {self.age}\nTall: {self.tall}\n")
