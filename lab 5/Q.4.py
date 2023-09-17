N = int(input("Enter a positive integer N: "))
if N <= 0:
    print("N must be a positive integer.")
else:
    divisible_count = 0
    not_divisible_count = 0
    num = 0  # Initialize num to 0

    while num != -999:
        num = int(input("Enter a number (or -999 to stop): "))
        
        if num != -999:
            if num % N == 0:
                divisible_count += 1
            else:
                not_divisible_count += 1

    print(f"Count of numbers divisible by {N}: {divisible_count}")
    print(f"Count of numbers not divisible by {N}: {not_divisible_count}")
