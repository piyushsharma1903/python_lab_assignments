#part a
height=int(input("enter the height in centimetres: "))
weight=int(input("enter the weight in kilograms: "))
if height>0 and weight>0:
    bmi=weight/(height**2)
    bmi=bmi*(10**4)
    print(f"your BMI is {bmi}")
#part b
height_b=int(input("enter the height in inches: "))
weight_b=int(input("enter the weight in pounds: "))
height_b=height_b/39.37
weight_b=weight_b/2.20
if height_b>0 and weight_b>0:
    bmi_2=weight_b/(height_b**2)
    print(f"your bmi is {bmi_2}")