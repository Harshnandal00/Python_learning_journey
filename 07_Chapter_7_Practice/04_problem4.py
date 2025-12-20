# Write a program to find whether a given number
# is prime or not?

a = int(input("Enter your number: "))

for i in range(2,a):
    if (a%i == 0):
        print("Your number is not a prime number.")
        break
    
else:
    print("Your number is a prime number")    