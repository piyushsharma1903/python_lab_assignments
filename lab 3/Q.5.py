number=input("enter a five digit number: ")
if len(number)<=5:
    reversed_number=print(f"{number[-1]}{number[-2]}{number[-3]}{number[-4]}{number[-5]} is reverse of your number")
    if reversed_number==number:
       print("Number is palindrome")
    elif reversed_number!=number:
       print("Number is not palindrome")
else:
    print("invalid input")