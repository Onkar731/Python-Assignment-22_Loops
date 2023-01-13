"""
Write a python script to calculate sum of first N natural numbers
"""

# taking input from the user
N = int(input("Enter a number : "))

# defining sum variable to store the sum of natural numbers
sum = 0

# calculating sum of first N natural numbers using range in for loop
for e in range(1, N+1) :
    sum += e

# printing sum of first N natural numbers
print("Sum of first %d natural numbers is %d" %(N, sum))