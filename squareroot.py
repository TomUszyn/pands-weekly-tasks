# squareroot.py
# Program takes positive floating number as input and output an approximation
# of its square root.
# author: Tomasz Uszynski

n = float(input("Please enter a positive number: "))            # Ask user for input.
def squareroot(n, tolerancelevel = 0.000001):                   # Function to calculate square root of n with tolerance level tolerancelevel
    initialGuess = n                                            # Initial guess.
    while True:                                                 # Loop to iterate until convergence.
        nextGuess = 0.5 * (initialGuess + n/initialGuess)       # Update guess.
        if abs(nextGuess - initialGuess) < tolerancelevel:      # Check for convergence.
            break                                               # Break the loop if converged.
        initialGuess = nextGuess                                # Set the new guess for the next iteration.
    return nextGuess                                            # Return the final guess.
print(f"The square root of {n} is approx. {squareroot(n)}")     # Print the result.