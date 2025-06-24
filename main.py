import panda


panda1= panda.Panda("panda1",10,90,False)

panda2= panda.Panda("panda2",20,110,False)

panda3= panda.Panda("panda3",30,80,True)

panda4= panda.Panda("panda4",40,120,True)

print("panda1 is_endangered ? "+ str(panda1.is_endangered))

print(panda1.introduce())
print(panda2.introduce())
print(panda3.introduce())
print(panda4.introduce())
print(f"panda {panda1.name} age in months: " + str(panda1.calculateAgeinMonths()))
print(f"panda {panda2.name} age in months: " + str(panda2.calculateAgeinMonths()))
print(f"panda {panda3.name} age in months: " + str(panda3.calculateAgeinMonths()))
print(f"panda {panda4.name} age in months: " + str(panda4.calculateAgeinMonths()))