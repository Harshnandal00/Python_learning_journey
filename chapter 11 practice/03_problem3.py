class employee:
    salary = 400
    incriment = 20

    @property
    def salaryafterincriment(self):
        return (self.salary + self.salary * (self.incriment/100))
    @salaryafterincriment.setter
    def salaryafterincriment(self, salary):
        self.incriment = ((salary/self.salary ) - 1)*100
        
e = employee()
# print(e.salaryafterincriment)
e.salaryafterincriment = 400
print(e.salary)
