import math

N = int(input("Enter the number of positive integers (N): "))

if N < 2:
    print("At least two positive integers are required to find the LCM.")
else:
    numbers = []

    # Gather N positive integers from the user
    for i in range(N):
        while True:
            num = int(input(f"Enter positive integer {i + 1}: "))
            if num > 0:
                numbers += [num]  # Add the positive integer to the list
                break
            else:
                print("Please enter a positive integer.")

    # Calculate LCM using the GCD function
    lcm = numbers[0]
    for i in range(1, N):
        gcd = math.gcd(lcm, numbers[i])
        lcm = (lcm * numbers[i]) // gcd

    print(f"The LCM of the {N} positive integers is: {lcm}")
