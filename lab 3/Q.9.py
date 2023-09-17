basic_salary=float(input("enter your basic salary amount: "))
basic_salary=round(basic_salary,2)
HRA=0.2*basic_salary
TA=0.05*basic_salary
DA=0.1*basic_salary
gross_salary=HRA+TA+DA+basic_salary
print(f"your gross salary is {gross_salary}")
if gross_salary<3*(10**5):
    print("income tax is 0%")
elif (3*(10**5))<gross_salary<(10*(10**5)):
    print("your tax slab is 10%")
elif (10*(10**5))<gross_salary<(25*(10**5)):
    print("your tax slab is 20%")
elif gross_salary>(25*(10**5)):
    print("slab is 30%")