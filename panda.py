class Panda:

    def __init__(self, name: str, age: int, gender: str, is_pregnant: bool, weight: float, height: float):
        self.name = name
        self.age = age
        self.gender = gender
        self.is_pregnant = False if gender.lower() == "male" else is_pregnant
        self.weight = weight
        self.height = height


    def introduce(self) -> str:
        introduction = f"The panda's name is {self.name}, age is {self.age} years, gender is {self.gender}, weight is {self.weight} kg, height is {self.height} meters, and it is {'pregnant' if self.is_pregnant else 'not pregnant'}."
        return introduction
    


    def set_pregnancy(self, status: bool):
        if self.gender.lower() != "female":
            print(f"{self.name} is not female. He Cant get pregnant.")
        else:
            self.is_pregnant = status
            print(f"{self.name}'s pregnancy status updated to pregnant.")

