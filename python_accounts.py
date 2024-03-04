# python_accounts.py
# Program reads in account number and outputs the account number
# with only the last 4 digits showing (All digits except last 4 replaced with Xs).
# author: Tomasz Uszynski


# To write this program we do some reseach to understand variables, data types and basic opertors.
# Our task involves manipulating strings, which requires knowledge of  string slicing and concatenation. 
# String slicing is used to extract a portion of the string (in this case, the last four digits), and concatenation
# is used to combine strings (in this case, 'X’s and the last four digits). Length of a String (len() function)
# in Python is used to get the number of characters in a string. We will use it to calculate the number of 'X’s
# needed. 

accountNumber = input("Please enter an account number.: ")  # Inputs account number.

accountNumberlength = len(accountNumber)                    # Checks length of account number.

toHide = accountNumber[:-4]                                 # Declarates with part will be hide.

lengthOftoHide = len(toHide)                                # Checks length of digits to hide.

x = 'X'                                                     # Declarates sign used to cover group of digits.

result = x * lengthOftoHide                                 # Counts how many Xs are needed.

print(result+accountNumber[-4:])                            # Prints out expected result.
                 
# To find out last four digits we used negative indexing. 
# In case of this program -1 refers to the last element,
# -2 refers to the second-to-last element, and so on. Omnit end index
# means the end of the sequence.

# Useful referal links to help understand basics:
# https://realpython.com/lessons/string-slicing/
# https://www.w3schools.com/python/gloss_python_string_length.asp
# https://www.w3schools.com/python/default.asp 