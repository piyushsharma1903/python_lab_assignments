N = int(input("Enter a positive number to find factorial: "))
# factorial is n! = n × (n - 1) × (n - 2) × ... × 2 × 1
factorial_result = 1
i = N
while i != 0:
    factorial_result = factorial_result* i
    i =i-1 
print(f"The factorial of {N} is {factorial_result}")