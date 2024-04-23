# collatz.py
# Program asks the user to input any positive integer and outputs the successive values of the following calculation.
# At each step calculate the next value by taking the current value and 
# if it is even, divide it by two, but if it is odd, multiply it by three and add one.
# Have the program end if the current value is one.
# author: Tomasz Uszynski

positiveInteger = int(input("Please enter an posivite integer: "))  # Inputs positive integer.

while positiveInteger <= 0:                                         # Checks if the input is positive integer.
    print("Entered integer is negative. Please enter an positive integer:") # Prints out message if input is negative.
    positiveInteger = int(input("Enter a positive integer: "))      # Inputs positive integer.

while positiveInteger != 1:                                         # Checks if the input is not equal to 1. 
    print(positiveInteger, end = " ")                               # Prints the value of the variable positiveInteger in the same line.
    if positiveInteger % 2 == 0:                                    # Checks if the value of the variable positiveInteger is even.
        positiveInteger = positiveInteger // 2                      # Divides the value of the variable positiveInteger by 2.
    else:                                                           # If the value of the variable positiveInteger is odd.
        positiveInteger = positiveInteger*3 + 1                     # Multiplies the value of the variable positiveInteger by 3 and adds 1.
print(positiveInteger, end = " ")                                   # Prints the value of the variable positiveInteger in the same line.