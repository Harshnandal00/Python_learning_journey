count = 0
total = 0
highest_number = 0

while True:
    number = int(input("enter any number(-4 to stop.): "))

    if number == -4:
        break
    count += 1
    total += number

    if highest_number<number:
        highest_number = number

    print("no. of times input entered: ",count)
    print("total addition of the numbers entered: ",total)
    print("this is the highest value entered by the user: ",highest_number)

if count>0:
    print("average of the total numbers entered is: ",total/count)
else:
    print("please enter some other no first other than -4!")