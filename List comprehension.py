# List Comprehension : 

List comprehension in Python is a concise way to create lists.
It allows you to generate a new list by applying an expression to each item in an existing iterable (like a list, tuple, or string). 

Here’s the basic syntax of list comprehension:
new_list = [expression for item in iterable if condition]

# expression: The operation you want to perform on each item.
# item: The current item from the iterable.
# iterable: The collection of items you are iterating over.
# condition (optional): A filter that only includes items that meet this condition.

Examples
1 : Simple List Comprehension:

numbers = [1, 2, 3, 4, 5]
squares = [x**2 for x in numbers]
print(squares)  # Output: [1, 4, 9, 16, 25]

2 : With a Condition
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = [x for x in numbers if x % 2 == 0]
print(even_numbers)  # Output: [2, 4, 6, 8, 10]

3 : Manipulating Strings:
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
fruits_with_a = [fruit for fruit in fruits if 'a' in fruit]
print(fruits_with_a)  # Output: ['apple', 'banana', 'mango']








