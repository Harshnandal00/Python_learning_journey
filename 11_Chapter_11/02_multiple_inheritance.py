
class employee: # Base/parent class
    company = "ITC"
    def show(self):
        self.name = "default name"
        print(f"The name of the employee is {self.name} and the company is {self.company}")
        
class coder: #Base/parent class
    language = "python"
    def printlanguage(self):
        print(f"The language in which you are best is {self.language}")


class programmer(employee, coder): #derived class
    company = "ITC infotech"
    def data(self):
        print(f"The programmer of the company {self.company} is good at {self.language} language")
        
a = employee()
b = programmer()

b.show()
b.data()
b.printlanguage()