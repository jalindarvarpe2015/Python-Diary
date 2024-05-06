'''
write a program that interprets the Body Mass Index (BMI) based on a users weight and height

it should tell them the interpretattion of their BMI based on the BMI vALUE

- under 18.5 they are underweight 
- over 18.5 but below 25 they have a normal weight 
- over 25 but below 30 they are slightly overweight
- over 30 but below 35 they are obese
- Above 35 they are clinically obese

'''

print("Wellcomr to the Clinic")

height = float(input("What is your height ? "))
weight = int(input("What is your weight ? "))

BMI = weight/(height * height)

if BMI <= 18.5:
    print(f"your BMI is {BMI}, and you are underweight")
elif BMI < 25:
    print(f"your BMI is {BMI}, and you have a normal weight")
elif BMI < 30:
    print(f"your BMI is {BMI}, and you are slightly overweight")
elif BMI < 35:
    print(f"your BMI is {BMI}, and you are obese")
elif BMI < 35:
    print(f"your BMI is {BMI}, and you are clinically obese")
    
    


