'''
Problem Statements

create a python program using maths and f-strings that tells us how many weeks we have left , if we live until 90 years old

it will take your current age as the input and output a message with our time left in this format

You have x weeks left.

Where is replaced with the actual calculated number of weeks input age has left until age 90 

Warning your output should match the example output format exactly 
even the position of the commas and full stops 

Example Input :
56

Example Output 
You have 1768 weeks left

'''

age = int(input("Enter your age : "))
years = 90 - int(age)
weeks = years * 52

print(f"You have {weeks} left")

# You have 1768 left





