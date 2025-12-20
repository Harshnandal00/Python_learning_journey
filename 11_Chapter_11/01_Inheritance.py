# Inheritance is a way of creating a new class from an existing class.
class employee: # Base/parent class
    company = "ITC"
    def show(self):
        self.name = "default name"
        print(f"The name of the employee is {self.name} and the company is {self.company}")
# now i want to make a another class which has same functions as employee like:
# class programmer:
#     company = "ITC infotech"
#     def show(self):
#         print(f"The name of the employee is {self.name} and the salary is {self.salary}")
#     def data(self):
#         print(f"The programmer {self.name} is good at {self.language} language")
        
# now as you can see i have used the all part of class employee in the class programmer by copy paste but it is not good and is time consuming so we will use the inheritance method and we will not have to copy paste all the classes of the parent/base class like...

class programmer(employee): #derived class
    company = "ITC infotech"
    def data(self):
        print(f"The programmer of the company {self.company} is good at {self.language} language")
        
a = employee()
b = programmer()
print(a.company , b.company)