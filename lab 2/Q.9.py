x=float(input("enter the amount: "))
y=int(input("enter the tenure (in months): "))


if x>=500 and y>=6:
    z=7.1/100
    interest_rate_per_month = z*(y/12)
    amount_raised=x*interest_rate_per_month
    x=x*y
    amount_raised_in_six_months=amount_raised*y
    total_amount=amount_raised_in_six_months+x
    
    print(f"return after {y} months would be {total_amount}")
else:
    print("invalid input")
