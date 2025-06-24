from panda import Panda

panda1 = Panda("bamboo", 22, "male", "Brown and White ", "249kg")
panda2 = Panda("Po", 55, "male", "black and white", "288kg")
panda3 = Panda("Bao Bao", 44, "male", "mostly white", "522kg")
panda4 = Panda("Chao", 9, "male", "black", "30kg")

print(f"The oldest panda age is: {panda2.age}")
panda2.eat()
panda2.sleep()

print("=" * 100)

print(f"The name of the youngest panda is: {panda4.name}")
panda4.eat()
panda4.sleep()

print("=" * 100)

print(f"The most overweight panda do weight around: {panda3.weight}")
panda3.eat()
panda3.sleep()

print("=" * 100)

print(f"the most uniqe color of the pandas is: {panda1.color} and the name of this panda is: {panda1.name}")
panda1.eat()
panda1.sleep()

print("=" * 100)