N=int(input("enter no.: "))
i=2
if N<=1:
    print("not a prime no.")
while i<N:
    if N%i==0:
        print("not a prime no.")
        break
    i=i+1
else:
    print("prime no.")
    
    
