class Panda:
    def __init__(self, name, age, gender,mood):
        self.name = name
        self.age = age
        self.gender = gender
        self.mood = mood
    def introduce(self):
        panda_intorduction = "This panda is "+ self.gender + ", name is " + self.name + "and the age is " + str(self.age)
        return panda_intorduction
    def what_the_mood(self):
        return "The panda mood is " + self.mood
    

        
        