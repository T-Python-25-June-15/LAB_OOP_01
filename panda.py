class Panda:
    def __init__(self, name:str, age:int, color:str, tall:float):
        self.name = name
        self.age = age
        self.color = color
        self.tall = tall
    

    def display_info(self):
        print(f'Name panda is: {self.name} Age: {self.age} color: {self.color} tall: {self.tall}')

    
    def update_age(self, new_age:int):
        print(f'we will update panda age from: {self.age} to: {new_age}')
        self.age = new_age
        print('update is Done!')
