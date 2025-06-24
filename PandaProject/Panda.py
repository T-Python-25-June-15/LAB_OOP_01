class Panda:
    def __init__(self, name, height, weight, color):
        self.name = name
        self.height = height
        self.weight = weight
        self.color = color

    def print_name(self):
        print("Panda name is:", self.name)

    def print_details(self):
        print("Height:", self.height, "cm")
        print("Weight:", self.weight, "kg")
        print("Color:", self.color)

