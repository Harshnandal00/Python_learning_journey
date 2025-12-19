# used to give logic  
# to a func. so that we can use that logic just by writing func()

a = int(input("enter your number: "))
b = int(input("enter your number: "))
c = int(input("enter your number: "))

print("average of the numbers:", (a+b+c)/2)

# now assume that we have to use the above programm many times that will
# take too much time and lines so we will add all this program as 
# logic in func.

def func():
    a = int(input("enter your number: "))
    b = int(input("enter your number: "))
    c = int(input("enter your number: "))
    print("average of the numbers:", (a+b+c)/2)

# now all that data has been transfered into this function whenever we 
# have to apply this data just do this

func()   # this is called function call with this we can run the whole 
func()         # thing by just using this small function call
func()    
func()    
func()    