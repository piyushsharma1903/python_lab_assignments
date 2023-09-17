x=int(input("enter the year: "))
if x%4==0:
    print(f"{x} is a leap year")
elif x%4 !=0:
    print(f"{x} is not a leap year")
else:
    print("invalid input")