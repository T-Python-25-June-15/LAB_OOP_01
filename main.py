from panda import Panda

panda = Panda("Po", 2, "Male", "Happy")
panda2 = Panda("Popo", 3, "Male", "Sad")
panda3 = Panda("Luna", 1, "Female", "Playful")
panda4 = Panda("Mei", 4, "Female", "Grumpy")

print(panda.name)
print(panda.introduce())
print(panda.what_the_mood())

print(panda2.name)
print(panda2.introduce())
print(panda2.what_the_mood())

print(panda3.name)
print(panda3.introduce())
print(panda3.what_the_mood())


print(panda4.name)
print(panda4.introduce())
print(panda4.what_the_mood())
