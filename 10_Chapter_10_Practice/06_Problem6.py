from random import randint
#Can you change the self-parameter inside a class to something else (say “harry”). Try changing self to “slf” or “harry” and see the effects.
class Train:
    def __init__(slf, trainNo):
        slf.trainNo = trainNo
    def book(slf, fro, to):
        print(f"The ticket is booked in train {slf.trainNo} from {fro} to {to}")
    def getstatus(slf, fro, to):
        print(f"The train {slf.trainNo} is running on time")
    def getfare(slf, fro, to):
        print(f"The ticket fare in train {slf.trainNo} from {fro} to {to} is {randint(300 , 5599)}")
        
t = Train(122495)
t.book("kashi", "Jaipur")
t.getstatus("kashi", "Jaipur")
t.getfare("kashi", "Jaipur")
# As you can see that i have used all slf instead of self and there is no change at all in the functions of the code and running perfectly..!