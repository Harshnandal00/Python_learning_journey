class employee:
    def __init__(self):
        print("this is the constructor of the class employee")
    a = 1
class programmer(employee):
    def __init__(self):
        print("this is the constructor of the class programmer")
    b = 2
class manager(programmer):
    def __init__(self):
        super().__init__() # it will make the constructor of the parent class also run whenever the manager class's object is made
        print("this is the constructor of the class manager")
    c = 3
o = employee() # as you can see that as i make the employee attribute it makes the respective costructor print but if we want to also print the constructor of the parent class then we will have to use the method known as super method