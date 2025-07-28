print('_________________Task nr. 1_____________________')
# Task nr.1. Variables and data types
# Objective: Learn to store data in variables and display it on the screen.

# Create variables
name = 'Arina'  # Text (str)
age = 29       # Numeric (int)
height = 1.69  # Numeric (float)
is_junior = True  # Boolean (Bool)
location = 'Vilnius, Lithuania' # Text (str)

# Displaying variables on display
print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Is a junior data analytic", is_junior)

print('_________________Task nr. 2_____________________')

# Task nr.2. Arithmetic operations
# Objective: To learn how to perform simple calculations.

# Variables
a = 8
b = 5

# Addition
result = a + b
print('Sum:', result)

# Multiplication
result = a * b
print('Product of numbers:', result)

# Division
result = a / b
print('Division:', result)

# Subtraction
result = a - b
print('Subtraction:', result)

# Remainder from division
result = a % b
print('Remainder from division:', result)

print('_________________Task nr. 3_____________________')

# Task nr.3. Conditional operators
# Objective: To learn to perform different actions depending on the conditions.

age = 35
# age = int( input('Enter your age:') )
if age >= 65:
    print('You are retired')
elif age >= 18:
    print('You are an adult')
else:
    print('You are a minor')

print('_________________Task nr. 4_____________________')

# Task nr.4. Loops
# Objective: Learn to repeat actions.

# For loops
for i in range(5):
    print('Iteration number:', i)

print('---------------------------')

for a in range(1, 6):
    print('Iteration number:', a)

print('---------------------------')

# While loops
count = 0
while count < 3:
    print('Counter:', count)
    count += 1

print('---------------------------')

vr = 1
while vr <= 5:
    print('Counter:', vr)
    vr += 1





