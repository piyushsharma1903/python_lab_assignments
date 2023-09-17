N=int(input("enter the no. of term(N) till upto you wnat to get fibnocci series: "))
a1=1
a2=1
count=2
if N<=0:
    print("enter valid input")
if N==1:
    print(a1)
if N==2:
    print(a2)
else:
    print(a1)
    print(a2)
    while count<N:
      a3=a1+a2
      print(a3)
      a1=a2
      a2=a3
      count=count+1