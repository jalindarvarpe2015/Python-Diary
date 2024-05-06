print("Wellcome to the rollercoaster")

height = int(input("What is your height in cm ? " ))

if height >= 120:
    print("you can ride the rollercoaster")
    age = int(input("What is your age ? "))
    if age < 12:
        print("plaese pay 200")
    elif age <= 18:
        print("please pay 300")
    else:
        print("please pay 400")
else:
    print("sorry, you have to grow taller before you can ride")