length=float(input("enter the length(in foot): "))
breadth=float(input("enter the breadth(in foot): "))
length=length*0.3048
breadth=breadth*0.3048
if length>0 and breadth>0:
    print(f"area is {length*breadth}")
else:
    print('invalid input')