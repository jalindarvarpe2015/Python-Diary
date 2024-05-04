#Problem Statement

#Write a program that adds the digit in a 2 digit number . e.g . If the input was 35, then the  output should be 8 (like 3+5)

#Example input 35
#Example output 8

input_number_str = str(35)

first_digit_number = int(input_number_str[0])
#print(first_digit_number)  -->3

second_digit_number = int(input_number_str[1])
# print(second_digit_number) ---> 5

addition_of_two_digit = (first_digit_number + second_digit_number)

print(addition_of_two_digit)
# 8