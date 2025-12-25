#for loop


for i in range(5):
    print(i)

for i in range(1,6):
    print(i)
    
for i in range(100,1001,100):
    print(i)

#while loop

count = 1
while count <= 10:
    print(count)
    count += 1


while True:
    value = input("please enter q to Quit: ")
    if value == 'q':
        break
    print("you entered:" , value)

i = 10
while i > 0:
    print(i)
    i -=1
a = 0
while a <= 20:
    print(a)
    a += 2
for b in range (0,21,2):
    print(b)

while True:
    number = int(input("To quit please enter 2341\nPlease enter any number: "))
    if number == 2341:
        break
    print("you entered this number: ",number)