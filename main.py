
import panda as p

panda1 = p.Panda(100,200,'Forest',23)
panda2 = p.Panda(150,300,'China',31)
panda3 = p.Panda(225,340,'mountainous',40)
panda4 = p.Panda(250,200,'polar regions',23)

print("Pandas Weight: ")
print(panda1.Weight)
print(panda2.Weight)
print(panda3.Weight)
print(panda4.Weight)

print()

panda1.information()
panda2.information()
panda3.information()
panda4.information()

print()

panda1.change_weight(110)
panda2.change_weight(160)
panda3.change_weight(250)
panda4.change_weight(220)

print("Pandas info after weights changing: ")

panda1.information()
panda2.information()
panda3.information()
panda4.information()

