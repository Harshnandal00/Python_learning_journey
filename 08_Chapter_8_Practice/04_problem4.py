# Write a recursive function to calculate the sum of first n natural numbers.
  

n = int(input("Enter your number: "))

def calculate_sum_of_natural_numbers(n):
    if(n == 1):
        return 1
    else:
        return n + calculate_sum_of_natural_numbers(n-1)
    


result = calculate_sum_of_natural_numbers(n)
print(f"sum of the first {n} natural numbers is: " , result)
    
    