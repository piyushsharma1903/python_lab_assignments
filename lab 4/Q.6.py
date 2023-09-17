N=input("enter a positive number: ")
length_of_input=len(N)
reversed_no=int(N[-1:-(length_of_input+1):-1])
N=int(N)
if N>0:
       if N==reversed_no:
           print(f"{N} is a palindrome number")
       elif N != reversed_no:
             print(f"{N} is not palindrome")
else:
      print("invalid input")
    