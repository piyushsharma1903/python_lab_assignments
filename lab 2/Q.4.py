x=int(input("enter a no.: "))
if x==0:
    print("neither even nor odd")
elif x>0 and x%2==0:
    print(f"{x} is even no.")
elif x>0:
    print(f"{x} is odd no.")
elif x<0:
    print("invalid input")
