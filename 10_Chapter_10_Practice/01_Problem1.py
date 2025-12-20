# Question - Create a class “Programmer” for storing information of few programmers working at Microsoft


class programmer:
    company = "microsoft"
    def __init__(self, name, salary, pincode):
        self.name = name
        self.salary = salary
        self.pincode = pincode
        
Person1 = programmer("Harry", 1200000, 124102)
print(Person1.name , Person1.salary, Person1.pincode)
Person2 = programmer("Rohan", 1100000, 322455)
print(Person2.name, Person2.salary, Person2.pincode)