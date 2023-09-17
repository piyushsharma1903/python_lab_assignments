N = int(input("Enter the number of lines (N): "))

# Pattern (a)
print("Pattern (a):")
line_a = 1
while line_a <= N:
    stars = 1
    while stars <= line_a:
        print("* ", end="")
        stars += 1
    print()
    line_a += 1

# Pattern (b)
print("\nPattern (b):")
line_b = 1
while line_b <= N:
    stars = 1
    while stars <= line_b:
        if stars < line_b:
            print("* ", end="")
        else:
            print("*", end="")
        stars += 1
    print()
    line_b += 1

# Pattern (c)
print("\nPattern (c):")
line_c = 1
while line_c <= N:
    spaces = 1
    while spaces <= N - line_c:
        print(" ", end="")
        spaces += 1
    stars = 1
    while stars <= (2 * line_c) - 1:
        print("*", end="")
        stars += 1
    print()
    line_c += 1
