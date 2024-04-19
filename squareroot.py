# squareroot.py
# Program takes positive floating number as input and output an approximation
# of its square root.
# author: Tomasz Uszynski

# Newton’s method is an iterative numerical technique used to find the roots
# of a given function (including square roots).

# The problem is to find square root of entered povitive number (n).
# We will use Newton’s method to iteratively improve our estimate until we 
# converge to an accurate value.
#
# Newton’s Method for Square Root
# Initial Guess (Assumption): start with an initial guess (x), which can be any positive value 
# (often set to 1 or n).
# Iterative Update: use the following formula to update our guess: 
# next_guess = 0.5*(x +n/x)
# Convergence Check: Calculate the difference between the current guess and 
# the next guess.# If the difference is within a specified tolerance level, 
# stop the iteration. Otherwise, repeat the process with the new guess.
# Output: The final guess after convergence is the square root of (n).

# Research and Implementation Steps:

# Understand Newton’s Method:
# Study the mathematical basis of Newton’s method for square root approximation.
# Explore how the iterative process converges to the actual square root.

# Implement the Algorithm:
# Write a function that takes the input number (n) and a tolerance level (tl) as arguments.
# Initialize the guess ((x)) to (1) or any other reasonable value.
# Use a loop to iteratively update the guess until the difference between consecutive 
# guesses is less than the tolerance.
# Return the final guess as the square root of (n).

# Test Your Implementation:
# Verify that your program produces accurate results for various input values.
# Experiment with different initial guesses and tolerances to improve convergence speed.

n = float(input("Please enter a positive number: "))
def sqrt(n, tl=0.000001):
    x0 = n                          # Initial guess
    while True:
        x1 = 0.5 * (x0 + n/x0)      # Update guess
        if abs(x1 - x0) < tl:       # Check for convergence
            break
        x0 = x1                     # Set the new guess for the next iteration
    return x1
print(f"The square root of {n} is approx. {sqrt(n)}")

# More informations on the websites:
# Information about Newton's Method for square root in document on Massachusetts 
# Institute of Technology Department of Mathematics website: https://math.mit.edu/~stevenj/18.335/newton-sqrt.pdf
# More about Newton's Method of squere root on The University of Texas at Austin website:
# https://web.ma.utexas.edu/users/m408n/CurrentWeb/LM4-8-4.php
# Very important movie to understand squareroot calculation on Dubious Insights YouTube channel: 
# https://www.youtube.com/watch?v=FpOEx6zFf1o
