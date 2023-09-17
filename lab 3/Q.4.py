number=input("enter a three digit no.: ")
no_1=int(number[0])
no_2=int(number[1])
no_3=int(number[2])
sum=no_1+no_2+no_3
print(sum)
if sum%3==0:
    print(f"{number} is divisible by 3")
else:
    print(f"{number} is not divisible by 3")

