from panda import Panda
def main():
    panda1 = Panda("John",2,"M","44 KG")
    panda2 = Panda("Sarah",3,"F","60 KG")
    panda3 = Panda("Kevin",4,"M","70 KG")
    panda4 = Panda("Susan",4,"F","63 KG")

    pandas = [panda1,panda2,panda3,panda4]
    for panda in pandas:
        print(panda.behavior())
        print(panda.vet_visit())
        print()
main()

