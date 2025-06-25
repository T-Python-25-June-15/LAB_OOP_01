
from panda import Panda


obj1 = Panda('A', 3,'red', 1.6)
obj2 = Panda('B', 4,'blue', 1.9)
obj3 = Panda('C', 7,'black', 1.2)
obj4 = Panda('D', 2,'white', 1.8)


obj1.display_info()
obj2.display_info()
obj3.display_info()
obj4.display_info()

obj1.update_age(4)
obj1.display_info()



