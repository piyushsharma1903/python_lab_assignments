basic_salary=float(input("enter your basic salary amount: "))
basic_salary=round(basic_salary,2)
HRA=0.2*basic_salary
TA=0.05*basic_salary
DA=0.1*basic_salary
gross_salary=HRA+TA+DA+basic_salary
print(f"your gross salary is {gross_salary}")