# -*- coding: utf-8 -*-
"""Day1,2,3,4 assignments.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1JaUepmRBG4y96wr64amcmO7cFSqfud3S
"""

#Write a program in Jupyter Notebook to declare variables of different data types (integer, float, string, and boolean). Print each variable and its type.
integer_var = 42
float_var = 3.14
string_var = "Hello, World!"
boolean_var = True
print("Integer Variable:")
print("Value:", integer_var)
print("Type:", type(integer_var))

print("\nFloat Variable:")
print("Value:", float_var)
print("Type:", type(float_var))

print("\nString Variable:")
print("Value:", string_var)
print("Type:", type(string_var))

print("\nBoolean Variable:")
print("Value:", boolean_var)
print("Type:", type(boolean_var))

#Create a List, tuple and Dictionary with 5 elements in it and how to access few elements based on the index. Try  with different examples
my_list = [10, 20, 30, 40, 50]
print("List:")
print(my_list[0])
print(my_list[2])
print(my_list[-1])
print(my_list[1:4])

print("\nTuple:")
my_tuple = ('apple', 'banana', 'cherry', 'date', 'elderberry')
print(my_tuple[1])
print(my_tuple[3])
print(my_tuple[-2])

print("\nDictionary:")
my_dict = {
    'name': 'Alice',
    'age': 25,
    'city': 'New York',
    'country': 'USA',
    'hobby': 'painting'
}
print(my_dict['name'])
print(my_dict['city'])
print(my_dict['hobby'])

#Write a Python program that takes a student's marks in three subjects as input.
#If the average is greater than or equal to 90, print "Grade: A".
#If the average is between 80 and 89, print "Grade: B".
#If the average is between 70 and 79, print "Grade: C".
#Otherwise, print "Grade: Fail".

subject1 = float(input("Enter marks for Subject 1: "))
subject2 = float(input("Enter marks for Subject 2: "))
subject3 = float(input("Enter marks for Subject 3: "))
average = (subject1 + subject2 + subject3) / 3

if average >= 90:
    print("Grade: A")
elif 80 <= average < 90:
    print("Grade: B")
elif 70 <= average < 80:
    print("Grade: C")
else:
    print("Grade: Fail")

#Write a Python program to calculate the sum of all even numbers between 1 and a given positive integer n
def sum_of_even_numbers(n):
    if n < 1:
        return 0
    even_sum = sum(i for i in range(2, n + 1, 2))
    return even_sum
try:
    n = int(input("Enter a positive integer: "))
    if n <= 0:
        print("Please enter a positive integer greater than 0.")
    else:
        result = sum_of_even_numbers(n)
        print(f"The sum of all even numbers between 1 and {n} is: {result}")
except ValueError:
    print("Invalid input. Please enter a positive integer.")