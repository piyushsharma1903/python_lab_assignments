x=input("enter 1st no.= ")
y=input("enter 2nd no.= ")
z=input("enter 3rd no.= ")
z=int(z)
x=int(x)
y=int(y)
i=x+1
while i<=y:
    if i in range(x,y):
        i=i+1
        if i%z==0:
            print(i)