from Panda import Panda

panda1 = Panda("Lulu", 4, 95.0, "Good", 8)
panda2 = Panda("Momo", 6, 105.5, "Good", 9)
panda3 = Panda("Kiki", 2, 88.2, "Good", 7.5)
panda4 = Panda("Toto", 5, 110.0, "Good", 10)

pandas = [panda1, panda2, panda3, panda4]
print(panda1.name)

for panda in pandas:
    panda.check_health()
    print(panda.status())
    print("."*30)

