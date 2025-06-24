class Panda:
    def __init__(self,name ,age,gender,weight):
        self.name = name
        self.age = age
        self.gender = gender
        self.weight = weight

    def behavior(self):
        if self.age > 2:
            return f"{self.name} likes to be alone"
        else:
            return f"{self.name} likes to play"

    def vet_visit(self):
        return f"vet visit for {self.name} is next week "