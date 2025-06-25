from panda import Panda

personNum1 = Panda("Ahmed", 25, 150, "banana")
personNum2 = Panda("Saad", 33, 160, "apple")
personNum3 = Panda("Khalid", 45, 151, "orange")
personNum4 = Panda("Sultan", 60, 170, "carrot")

print(personNum1.name)
personNum1.eating()
personNum1.information()

print(personNum2.name)
personNum2.eating()
personNum2.information()

print(personNum3.name)
personNum3.eating()
personNum3.information()

print(personNum4.name)
personNum4.eating()
personNum4.information()
