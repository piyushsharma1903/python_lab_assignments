x=float(input("enter the length of first parallel sides of trapezoid: "))
y=float(input("enter the length of second parallel side of trapezoid: "))
h=float(input("enter the length of height of trapezoid: "))
if x>0 and y>0 and h>0:
    area=(1/2*(x+y))*h
    print(area)