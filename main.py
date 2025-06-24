from panda import Panda

# create instance
panda1= Panda("momo",4,80,"Bamboo")
panda2= Panda("nunu",7,110,"Bamboo")
panda3= Panda("saso",3,90,"Bamboo")
panda4= Panda("pan",8,150,"Bamboo")



# print one aattribute value
print(f"Panda's first name : {panda1.name}")
print("Panda's Info : ")
#calling a display method 
(panda1.display())
(panda2.display())
(panda3.display())
(panda4.display())


# calling eat method
print("Panda's food Info : ")
(panda1.eat())
(panda2.eat())
(panda3.eat())
(panda4.eat())







