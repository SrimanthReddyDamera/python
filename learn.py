# Important Python Examples

# Basic Data Types
integer_example = 10
float_example = 10.5
string_example = "Hello, World!"
boolean_example = True

# Control Flow
if integer_example > 5:
    print("Integer is greater than 5")
else:
    print("Integer is 5 or less")

# Functions
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))

# Loops
numbers = [1, 2, 3, 4, 5]
for number in numbers:
    print(number)

# List Comprehensions
squared_numbers = [x**2 for x in numbers]
print(squared_numbers)
