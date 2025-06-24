import class_panda

panda1 = class_panda.panda("jack" ,90  ,80 , "black" )
panda2 = class_panda.panda("mark" , 70 , 100 , "White")
panda3 = class_panda.panda("logan" , 100 , 110 , "blue")
panda4 = class_panda.panda("elon" , 120 , 70 , "red")

print(f"panda1 height is {panda1.height} cm")

print("\n-----first panda----")

print(panda1.panda_name())
print(panda1.describe())

print("\n-----second panda----")

print(panda2.panda_name())
print(panda2.describe())


print("\n-----third panda----")

print(panda3.panda_name())
print(panda3.describe())

print("\n-----fourth panda----")

print(panda4.panda_name())
print(panda4.describe())




