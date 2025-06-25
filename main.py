from classDefinition import Panda


panda1 = Panda("Po" , 14 , 80 , 85)
panda2 = Panda("welly" , 11 , 75 , 55)
panda3 = Panda("Koma" , 18 , 105 , 40)
panda4 = Panda("Mimi" , 8 , 60 , 93)


# Panda 1
print(f"The age of this panda is: {panda1.age}.")
panda1.pandaInfo()
panda1.healthCondition()
print()

# Panda 2 
print(f"The name of this panda is: {panda2.name}.")
panda2.pandaInfo()
panda2.healthCondition()
print()

# Panda 3
print(f"The weight of this panda is: {panda3.weight}.")
panda3.pandaInfo()
panda3.healthCondition()
print()

# Panda 4
print(f"The health percentage of this panda is: {panda4.healthPercentage}.")
panda4.pandaInfo()
panda4.healthCondition()
print()



