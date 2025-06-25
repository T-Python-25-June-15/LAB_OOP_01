from panda import Panda

panda_1 = Panda("Lulu", 5, "Female", False, 95.0, 1.5)
#Males cant be pregnant it will be corrected automatically.
panda_2 = Panda("Bobo", 4, "Male", True, 110.0, 1.7)  
panda_3 = Panda("Nini", 6, "Female", True, 88.0, 1.4)
panda_4 = Panda("Momo", 3, "Male", False, 120.0, 1.6)


panda_1.set_pregnancy(True)
#Males cant be pregnant nothing will change
panda_2.set_pregnancy(True)

pandas = [panda_1, panda_2, panda_3, panda_4]

for index, panda in enumerate(pandas, start=1):
    print(f"- {index} {panda.introduce()}\n")
