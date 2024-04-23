# es.py
# Program that reads in a text file and outputs the number of e's it contains.
# To realize it, we need to input the name of the file as an argument, check if the file exists, and then count 
# the number of occurrences of the letter 'e' in the file.
# author: Tomasz Uszynski

import os                                           # Import the os module to access the file system.
import sys                                          # Import the sys module to access the command line arguments.
 
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

if __name__ == "__main__":                          # Check if the script is being run directly.     
   if len(sys.argv) > 1:                            # Check if the user has provided a file name as a command line argument.
       fileName = sys.argv[1]                       # Get the file name from the command line.       
       letter = 'e'                                 # Set the letter to count.                       
       print(letterFrequency(fileName, letter))     # Call the function and display the number of occurrences of the letter 'e' in the file.
   else:                                            # If the user has not provided a file name as a command line argument.
       print("There is no agrument provided. Please provide a file name as a command line argument.")   # Print out statement.                                                                                                # user to provide a file name. 