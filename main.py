from panda import Panda

panda1 = Panda("Sarah",2,False,90.5)
panda2 = Panda("Po", 6, True, 90.5) 
panda3 = Panda("Xan", -1, True, 50.4) 
panda4 = Panda("Bamboo", 3, False, -70.2) 

print(panda1.intro())
print(panda1.life_time())

print(panda3.intro())
print(panda3.life_time())

print(panda4.intro())
print(panda4.life_time())