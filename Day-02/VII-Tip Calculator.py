# Tip Calculator Program 

print("Wellcome to the Tip Clculator ! ")

Total_bill = float(input("What was the Total bill ? "))

Tip = int(input("How Much tip would like to give ? 10, 12 , or 15 ? "))

Total_people = int(input("How manuy people to split the bills ? "))

tip_as_percent = Tip / 100

total_tip_amount = Total_bill * tip_as_percent 

total_billl = Total_bill + total_tip_amount

bill_per_persom = total_billl / Total_people

final_amount = round(bill_per_persom, 2)


print(f"Each person should pay :  {final_amount}")