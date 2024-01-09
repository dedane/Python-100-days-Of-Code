height = float(input("Enter your height in m "))
weight = float(input("Enter your weight in Kg "))

Bmi = weight/height ** 2

if Bmi <= 18.5:
    if Bmi <= 25:
        print(f' your bmi is {Bmi}, normal weight')
    elif Bmi <= 30:
        print(f' your bmi is {Bmi},you are overweight')
    elif Bmi <= 35:
        print(f' your bmi is {Bmi},you are obese')
    elif Bmi > 35:
        print(f' your bmi is {Bmi},You are clinically obese')

