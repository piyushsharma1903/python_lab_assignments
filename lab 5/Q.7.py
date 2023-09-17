N = int(input("Enter the number of lines (N): "))

i = 1
while i <= N:
    j = 1
    while j <= i:
        print("*", end=" ")
        j += 1
    print()  # Move to the next line after each row
    i += 1
