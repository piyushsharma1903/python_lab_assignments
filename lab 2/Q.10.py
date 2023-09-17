x=int(input("enter a number (in seconds): "))
if 1<=x<=86400:
   minutes,seconds=x//60,x%60
   hrs,minutes_2=minutes//60,minutes%60
   print(f"time is {hrs} hrs and {minutes_2} minutes and {seconds} seconds")