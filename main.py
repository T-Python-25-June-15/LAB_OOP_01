
from panda import Panda

panda1 = Panda("Po", 5, 120, 30)
panda2 = Panda("Ling Ling", 3, 100, 20)
panda3 = Panda("Mei Mei", 4, 110, 25)
panda4 = Panda("Bao Bao", 2, 90, 15)

pandas = [panda1, panda2, panda3, panda4]


print(panda1.name)
panda1.eat_bamboo(5)
panda1.sleep(2)
