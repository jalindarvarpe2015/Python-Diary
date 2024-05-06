'''
Write a program that works out whether if a given year is a leap year . A nomral year has 365 days 
. leap yera have 366. with an extra day in February. The reason why we have lea

'''

year = int(input("Enter a year "))

if year %4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year")
        else:
            print("not a laep year")
    else:
        print("Leap Year")
else:
    print("Not a leap year")