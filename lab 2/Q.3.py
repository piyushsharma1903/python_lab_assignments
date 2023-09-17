x=int(input("enter a no.: "))
y=int(input("enter a no.: "))
if x>0 and y>0:
    if x%y==0:
        print(f"{x} is divisible by {y}")
    elif x%y != 0:
        print(f"{x} is not divisible by {y}")
elif x<0 or y<0:
    print("invalid input")
