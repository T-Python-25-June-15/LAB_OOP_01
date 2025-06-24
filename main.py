#lab oop (wasan alqahtani)
from panda import Panda

#Create 4 instances/objects
First_Panda = Panda(10,"plants and Bamboo","China","Female")
Second_Panda = Panda(30,"leaves","America","Male")
Third_Panda = Panda(5,"Bamboo","Austuria","Female")
Fourth_Panda = Panda(15,"plants","China","Male")

print(f"the age of this panda {First_Panda.age}")
print("-"*20)

print("First instance")
print("-"*20)
print(First_Panda.panda_description())
print(First_Panda.panda_country())
print("-"*20)

print("Second instance")
print("-"*20)
print(Second_Panda.panda_description())
print(Second_Panda.panda_country())
print("-"*20)

print("Third instance")
print("-"*20)
print(Third_Panda.panda_description())
print(Third_Panda.panda_country())
print("-"*20)

print("Fourth instance")
print("-"*20)
print(Fourth_Panda.panda_description())
print(Fourth_Panda.panda_country())
print("-"*20)