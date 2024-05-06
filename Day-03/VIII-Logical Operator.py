'''
logical operator

- And
- Or
- Not

a = 12
a > 15
False

a > 10
True

a > 10 and a < 13
True

a > 15 and a < 13
False


'''
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
    elif age >= 45 and age <= 55:
        print("Everything going to be okay . Have a free ride on us")
    else:
        bill = 12
        print("adults ticket are 12")
    
want_photo = input("do you want photo ? Y or N ")
if want_photo == "Y":
    bill += 3

print(f"yOu have to pay {bill}")
