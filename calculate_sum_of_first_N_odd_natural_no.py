"""
Write a python script to calculate sum of first N odd natural numbers
"""

# taking input from the user
N = int(input("Enter a number : "))

# defining sum variable to store the sum of first N odd natural numbers
sum = 0

# calculating sum of first N odd natural numbers using range in for loop
for e in range(1, N*2+1, 2) :
    sum += e

# printing sum of first N odd natural numbers
print("Sum of first %d odd natural numbers is %d" %(N, sum))

# another logic
"""
    sum1 = 0  
    for e in range(1, N+1) :
        sum1 += (e*2-1)
    print("Sum of first %d odd natural numbers is %d" %(N, sum1))
"""