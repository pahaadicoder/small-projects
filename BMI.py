# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#First *fork* your copy. Then copy-paste your code below this line 👇
#Finally click "Run" to execute the tests
bmix = (weight) / (height**2)
if bmix < 18.5:
    print(f" Your BMI is {int(round(bmix,2))}, you are underweight.")
if bmix > 18.5:
    if bmix < 25:
        print(f"Your BMI is {int(round(bmix,0))}, you have a normal weight. ")
if bmix > 25:
    if bmix < 30:
        print(
            f"Your BMI is {int(round(bmix,0))}, you are slightly overweight. ")
if bmix > 30:
    if bmix < 35:
        print(f"Your BMI is {int(round(bmix,0))}, you are obese. ")
if bmix > 35:
    print(f"Your BMI is {int(round(bmix,0))}, you are clinically obese. ")