print("to get solutions of your quadratic expression ax^2 + bx + c")
a=float(input("enter a: "))
b=float(input("enter b: "))
c=float(input("enter c: "))
if a==0:
    print("invalid input your expression is not quadratic")
else:
    d=(b**2)-(4*(a*c))
    sol1=((-b)+d)/(2*a)
    sol2=((-b)-d)/(2*a)
    print(f"solutions of your quadratic expressions are {(round(sol1,2))} and {(round(sol2,2))}")