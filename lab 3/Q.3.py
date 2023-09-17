a1=float(input("enter the first side: "))
a2=float(input("enter the second side: "))
a3=float(input("enter the third side: "))
if a1>0 and a2>0 and a3>0:
    if a1+a2>=a3 and a1+a3>=a2 and a2+a3>=a1:
        print("given sides form a triangle")
    else:
        print("given sides don't form a triangle")
else:
    print("invalid input")