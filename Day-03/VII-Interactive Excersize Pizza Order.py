'''
INSTRUCTION

Congratulations, you have got a job at Python Pizza! Your first job is to build an automatic pizza order program

based on users order , work out their final bill

small size(S) : 15   RS
Medium Pizza(M) : 20 RS
Large Pizza(L)  : 25 RS

Add pepperoni for small pizza ( Y or N) : 2 RS
Add pepperoni for medium large pizza ( Y or N ) : 3 RS
Add extra cheese for any size pizza ( Y or N )  : 1

Example Input 
L
Y
N

Example Output

'''

print("Thak you for choosing Python Pizza Deliveres")

bill = 0

size = input("What size pizza do you want ? S, M or L ")

add_pepperoni = input("Do you want pepperoni ? Y or N ")

extra_cheese = input("Do you want extra cheese ? Y or N ")

if size == "S":
    bill += 15
elif size == "M":
    bill += 20
else:
    bill += 25
    
if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3
    
if extra_cheese == "Y":
    bill += 1
    
print(f"Your final bill is : {bill}. ")

    
    





