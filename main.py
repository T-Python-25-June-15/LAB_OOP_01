#Luluh Almogbil
'''
# LAB_OOP_01

## Using what you learned about classes , 
# create a class to represent a Panda. The class should have the following:
- 4 Attributes
- 2 Methods


### Create 4 instances/objects of the class Panda , print 1 attribute value,  and call the two methods on each instance. 
#### Note:
Arrange your code in seperate files (one for the main file for main logic , and another for the definition of the class). 
'''
# class Panda:
    
#     #constructor:
#     def __init__(self,name:str,gender:str,age:int,fav_food:str) -> None:
#         self.name = name
#         self.gender = gender
#         self.age = age
#         self.fav_food = fav_food
        
#     #methods/functions
#     def display(self):
#         introduce = f"The panda name is {self.name} and it a {self.gender}, {self.name} is {self.age} years old ."
#         return introduce
    
#     def my_fav_food(self):
#         food = f"The panda likes to eat {self.fav_food}"
#         return food

from mylogic import Panda

#instances > outside the class
try:
    
    panda1 = Panda("Phoebe","Female",60,"Pizza")
    panda2 = Panda("Jason","Male",45,"Pasta")

    #calling the method and accessing an attribute
    print(panda1.display())
    print(panda1.name,"'s favorite food is : ",panda1.fav_food)


    print(panda2.display())
    print(panda2.my_fav_food())  
except Exception as e:
    print(e.__class__)
 
        
        
        