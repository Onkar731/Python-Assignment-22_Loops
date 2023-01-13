"""
Write a python script to calculate sum of first N even natural numbers
"""

# taking input from the user
N = int(input("Enter a number : "))

# defining sum variable to store the sum of first N even natural numbers
sum = 0

# calculating sum of first N even natural numbers using range in for loop
for e in range(2, N*2+1, 2) :
    sum += e

# printing sum of first N even natural numbers
print("Sum of first %d even natural numbers is %d" %(N, sum))

# another logic
"""
    sum1 = 0  
    for e in range(1, N+1) :
        sum1 += (e*2)
    print("Sum of first %d even natural numbers is %d" %(N, sum1))
"""