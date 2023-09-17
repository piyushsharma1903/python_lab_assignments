N=int(input("enter a no.: "))
i=1
while i<=20:
    k=N*i
    print(f"{N} x {i} = {k}")
    i=i+1
    while N in range(1,N+1):
        N=N+1
        print(f"{N} x {i} = {k}")
    
