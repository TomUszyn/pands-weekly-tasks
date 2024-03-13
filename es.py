# es.py
# Program that reads in a text file and outputs the number of e's it contains.
# To realize it, we need to input the name of the file as an argument, check if the file exists, and then count 
# the number of occurrences of the letter 'e' in the file.
# author: Tomasz Uszynski

# Research:
# Method: Using the in-built count() method.

# Approach:
# 1. Read the file.
# 2. Store the content of the file in a variable.
# 3. Use the count() method with the argument as a letter whose frequency is required.
# 4. Display the count of the letter.

import os
import sys
 
def letterFrequency(fileName, letter):                       # Define function to count the number of occurrences of a letter in a text file
    if not fileName.endswith('.txt'):                        # Check if the file is a .txt file.              
        return f"The file {fileName} is not a .txt file."    # Return an error message if the file is not a .txt file.
    
    try:                                                     # Use a try block to handle the FileNotFoundError exception.                                            
       file = open(fileName, "r")                            # Open the file in read mode.             
    except FileNotFoundError:                                # Use an except block to handle the FileNotFoundError exception.                  
       return f"The file {fileName} was not found."          # Return an error message if the file is not found.  
    file = open(fileName, 'r')                               # Open the file in read mode
  
    text = file.read()                                       # Store the content of the file in a variable                                          
  
    return text.count(letter)                                # Return the count of the letter
  
#print(letterFrequency(' ', 'e'))                       # Call the function and display the number of occurrences of the letter 'g' in the file.
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
# 2.How to open file using Python:
# https://www.w3schools.com/python/python_file_open.asp
# 3.Counting letter in text file: 
# https://www.geeksforgeeks.org/count-the-number-of-times-a-letter-appears-in-a-text-file-in-python/
# 4.Best source of information about file processing:
# https://www.freecodecamp.org/news/python-write-to-file-open-read-append-and-other-file-handling-functions-explained/
# 5. try except in while True: 
# https://forum.freecodecamp.org/t/issue-about-try-except-in-while-true/464980/2
# 6. More about try except: 
# https://python.land/deep-dives/python-try-except
# https://www.idkrtm.com/error-handling-in-python-using-with-and-try/