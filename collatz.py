# collatz.py
# Program asks the user to input any positive integer and outputs the successive values of the following calculation.
# At each step calculate the next value by taking the current value and 
# if it is even, divide it by two, but if it is odd, multiply it by three and add one.
# Have the program end if the current value is one.
# author: Tomasz Uszynski

# To write this program we to understand Collatz conjecture. Good source of information is Wikipedia.
# We will need to understand the concept of loops and conditional statements.
# We will use while loop to repeat the process until the current value is one.
# We will use if statement to check if the current value is even or odd.
# We will use the modulo operator (%) to check if the current value is even or odd.
# We will use the floor division operator (//) to divide the current value by two.
# We will use the multiplication operator (*) to multiply the current value by three.  
# We will use the addition operator (+) to add one to the current value.   
# We will use the end parameter of the print() function to print the values in the same line.

# First of all user puts the positive integer.
positiveInteger = int(input("Please enter an posivite integer: "))

# Loop while checks if this is positive integer and if the entered integer is negative or zero,
# it keeps asking for a positive integer.

while positiveInteger <= 0:
    print("Entered integer is negative. Please enter an positive integer:")
    positiveInteger = int(input("Enter a positive integer: "))

# This code generates a sequence based on the Collatz conjecture.
# It starts with a positive integer and repeatedly applies the following rules:
# Rule1: If the integer is even, divide it by 2.
# Rule2: If the integer is odd, multiply it by 3 and add 1.
# The sequence continues until the integer becomes 1.

while positiveInteger != 1:
    print(positiveInteger, end = " ")                 # Prints the value of the variable positiveInteger in the same line.
    if positiveInteger % 2 == 0:
        positiveInteger = positiveInteger // 2
    else:
        positiveInteger = positiveInteger*3 + 1
print(positiveInteger, end = " ")

# Referal links to help understand basics:
# Information about Collatz conjecture: https://en.wikipedia.org/wiki/Collatz_conjecture
# Information about Loops and Conditionals in PDF file Lecture_11.pdf from Purdue University website:
# https://www.purdue.edu/hla/sites/varalalab/wp-content/uploads/sites/20/2018/04/Lecture_11.pdf       