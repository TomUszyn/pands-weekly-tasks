# es.py
# Program that reads in a text file and outputs the number of e's it contains.
# To realize it, we need to input the name of the file, check if the file exists, and then count 
# the number of occurrences of the letter 'e' in the file.
# author: Tomasz Uszynski


# Research:
# Method: Iterate through the file content in order to compare each character with the given letter.
# 
# Approach:
# 1. Open the file in read mode using the provided file name.
# 2. If the file is not found, return an error message.
# 3. Read the content of the file and store it in a variable.
# 4. Initialize a counter variable with 0.
# 5. Iterate through each character in the file content.
# 6. If the character is equal to the given letter, increment the counter.
# 7. Return the final count of the letter occurrences.

# The program has implented error handling to handle the FileNotFoundError exception and prompt the user to provide a file name if it 
# is not provided as a command line argument. The program also checks if the file is a .txt file and returns an error message if it is not.
 

import sys                                          # import the sys module
import os

def letterFrequency(fileName, letter):              # define function to count the number of occurrences of a letter in a text file
    
    if not fileName.endswith('.txt'):               # Check if the file is a .txt file.
        return f"The file {fileName} is not a .txt file." # Return an error message if the file is not a .txt file.
    
    try:                                            # Use a try block to handle the FileNotFoundError exception.
           file = open(fileName, "r")               # Open the file in read mode.                    
    except FileNotFoundError:                       # Use an except block to handle the FileNotFoundError exception.
           return f"The file {fileName} was not found." # Return an error message if the file is not found.
       
    text = file.read()                              # Store the content of the file in a variable.                             
    count = 0                                       # Initialize a counter variable with 0.                                      

    for char in text:                               # Iterate through each character in the file content.                              
        if char == letter:                          # If the character is equal to the given letter.
            count += 1                              # Increment the counter.                             
    
    return count                                    # Return the final count of the letter occurrences.              
             
    
if __name__ == "__main__":                          # Check if the script is being run directly.                          
   if len(sys.argv) > 1:                            # Check if the user has provided a file name as a command line argument.                               
       
       fileName = sys.argv[1]                       # Get the file name from the command line.                          
       
       letter = 'e'                                 # Set the letter to count.                                    
       
       print(letterFrequency(fileName, letter))     # Call the function and display the number of occurrences of the letter 'e' in the file.        
   else:                                            # If the user has not provided a file name as a command line argument.                                               
       print("There is no agrument provided. Please provide a file name as a command line argument.")   # Print a message to prompt the
                                                                                                        # user to provide a file name.  


# References:

# 1.Source of moby-dick.txt file: 
# https://web.stanford.edu/class/archive/cs/cs110/cs110.1224/examples/map-reduce/long-novels/
# 2. How to Use sys.argv in Python:
# https://www.knowledgehut.com/blog/programming/sys-argv-python-examples
# 4. Control the Execution of Your Code:
# https://realpython.com/python-main-function/
# 3.Counting letter in text file: 
# https://www.geeksforgeeks.org/count-the-number-of-times-a-letter-appears-in-a-text-file-in-python/
# 4.Best source of information about file processing:
# https://www.freecodecamp.org/news/python-write-to-file-open-read-append-and-other-file-handling-functions-explained/
# 5. try except in while True: 
# https://forum.freecodecamp.org/t/issue-about-try-except-in-while-true/464980/2
# 6. More about try except: 
# https://python.land/deep-dives/python-try-except
# https://www.idkrtm.com/error-handling-in-python-using-with-and-try/