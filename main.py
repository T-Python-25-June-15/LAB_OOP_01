from panda import Panda

panda1 = Panda("Meomo", "3","beby gril","Black and White")
panda2 = Panda("Koala", "5"," gril","Black")
panda3 = Panda("Jojo", "2","beby gril","Black and White")
panda4 = Panda("More", "6","Boy","White with Red")

for panda in[panda1,panda2,panda3,panda4]:
    print(f"\n Name of Panda: {panda.name}")
    
    panda.eat()
    panda.sleep()
    #panda.play()   # this Try to call the method play() in Panda class, but it does not exist in Panda class#
    