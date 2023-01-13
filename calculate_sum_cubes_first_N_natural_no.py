"""
Write a python script to calculate sum of cubes of first N natural numbers
"""

# taking input from the user
N = int(input("Enter a number : "))

# defining sum variable to store the sum of cubes of first N natural numbers
sum = 0

# calculating sum of cubes of first N natural numbers using range in for loop
for e in range(1, N+1) :
    sum += e**3

# printing sum of cubes of first N natural numbers
print("Sum of cubes of first %d natural numbers is %d" %(N, sum))