from random import randint
## Write a Class ‘Train’ which has methods to book a ticket,
# get status (no of seats) and get fare information of
# train running under Indian Railways?
class Train:
    def __init__(self, trainNo):
        self.trainNo = trainNo
    def book(self, fro, to):
        print(f"The ticket is booked in train {self.trainNo} from {fro} to {to}")
    def getstatus(self, fro, to):
        print(f"The train {self.trainNo} is running on time")
    def getfare(self, fro, to):
        print(f"The ticket fare in train {self.trainNo} from {fro} to {to} is {randint(300 , 5599)}")
        
t = Train(122495)
t.book("kashi", "Jaipur")
t.getstatus("kashi", "Jaipur")
t.getfare("kashi", "Jaipur")
