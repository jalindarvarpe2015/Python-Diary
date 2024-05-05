'''
BMI - Body Mass Index

Write a program that calcualte the body mass index (BMI) From a user weight and height 

BMI = Weight(kg)/height(m²)

Note: - you should convert the bmi to a whole number and print out a 
whole number in order to pass all the tests

Example Input :
1.75
80

means : height 80 and height 1.75


Example Output 
26 

since : 80 + (1.75 * 1.75) = 26.1224

'''

height = float(input("Enter your Height : "))

weight = int(input("Enter ypur Height : "))

BMI = weight / (height * height) 

print("Your Body Mass Index (BMI) IS ", BMI)


# Your Body Mass Index (BMI) IS  26.122448979591837