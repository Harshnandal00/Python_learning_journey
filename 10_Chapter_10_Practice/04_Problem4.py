# Add a static method in problem 2, to greet the user with hello.
class calculator:
    @staticmethod
    def greet():
        print("Good Morning")
    def __init__(self, n):
        self.n = n
    def square(self):
        print(f"The square of the number is {self.n*self.n}")
    def cube(self):
        print(f"The cube of the number is {self.n**3}")
    def squareroot(self):
        print(f"The squareroot of the number is {self.n**0.5}") 
i = int(input("Enter your number here: "))           
a = calculator(i)
a.greet()
a.square()
a.cube()
a.squareroot() 