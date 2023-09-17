a = int(input("Enter the first integer (a): "))
b = int(input("Enter the second integer (b): "))

print(f"Before swapping: a = {a}, b = {b}")

a = a + b
b = a - b
a = a - b

print(f"After swapping: a = {a}, b = {b}")

