N = int(input("Enter a positive integer N: "))
while N <= 0:
    print("N must be a positive integer.")
    N = int(input("Enter a positive integer N: "))

divisible_count = 0
not_divisible_count = 0

while True:
    user_input = int(input("Enter a number (-999 to exit): "))
    if user_input == -999:
        break

    if user_input % N == 0:
        divisible_count += 1
    else:
        not_divisible_count += 1

print("Count of numbers divisible by N:", divisible_count)
print("Count of numbers not divisible by N:", not_divisible_count)