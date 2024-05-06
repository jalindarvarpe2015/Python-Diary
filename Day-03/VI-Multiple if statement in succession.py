print("Wellcome to the rollercoaster")

height = int(input("What is your height in cm ? " ))
bill = 0


if height >= 120:
    print("you can ride the rollercoaster")
    age = int(input("What is your age ? "))
    if age < 12:
        bill = 5
        print("child ticket are 5")
    elif age <= 18:
        bill = 7
        print("your ticket is 7")
    else:
        bill = 12
        print("adults ticket are 12")
    
want_photo = input("do you want photo ? Y or N ")
if want_photo == "Y":
    bill += 3

print(f"yOu have to pay {bill}")
    