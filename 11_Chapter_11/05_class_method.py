class employee:
    a = 1 # class attribute 
    def show(self):
        print(f"class attribute of a is {self.a}")
        
e = employee()
e.a = 45 # instance attribute 
e.show() 

# as you can see and know that it will give us the instance attribute instead of  class attribute as instance attr. is given more priority in these type of situations but to escape this delmna we need to use class method as follows.....

class employee:
    a = 1 # class attribute 
    @classmethod # decorator used 
    def show(cls): # changed self to "cls"
        print(f"class attribute of a is {cls.a}")
        
e = employee()
e.a = 45 # instance attribute 
e.show() 