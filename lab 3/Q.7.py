print("complex no. is of form a+ib")
a1=float(input("enter a1: "))
b1=float(input("enter b1: "))
k=str("i")
print(f"complex1 no. is {a1} + {k}{b1}")
a2=float(input("enter a2: "))
b2=float(input("enter b2: "))
print(f"complex2 no. is {a2} + {k}{b2}")
real_part_sum=a1+a2
complex_part_sum=b1+b2
real_part_multiplication=((a1*a2)-(b1*b2))
imaginary_part_multiplication=((a1*b2)-(b1*a2))
print(f"sum is {real_part_sum} + {complex_part_sum}{k} and multiplication is {real_part_multiplication} - {k}{imaginary_part_multiplication}")
