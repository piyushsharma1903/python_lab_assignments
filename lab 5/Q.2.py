N = int(input("Enter a positive number N: "))

if N <= 0:
    print("Please enter a positive number.")
else:
    number = 1
    while number <= 1000:
        if number%N == 0:
            number = number + 1
            continue
        print(number, end=" ")  # Print numbers not divisible by N
        number = number + 1
