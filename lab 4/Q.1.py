N=int(input("enter the positive no.: "))
if N>0:
    i=0
    while i<20:
         i=i+1
         k=N*i
         print(f"{N} x {i} = {k}")
else:
     print("invalid input")