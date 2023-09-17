x=input("enter a three digit no.: ")
a=int(x[0])
b=int(x[1])
c=int(x[2])
x=int(x)#this is written at last for a reason if upr likhenge toh indexing me erroe kr dega
if (a**3)+(b**3)+(c**3)==x:
    print(f"{x} is an armstrong no.")