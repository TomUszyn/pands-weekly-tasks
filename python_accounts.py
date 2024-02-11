# python_accounts.py
# Program reads in a 10 character account number and outputs the account number
# with only the last 4 digits showing (and the first 6 digits replaced with Xs).
# author: Tomasz Uszynski


accountNumber = input("Please enter a 10-digit account number.: ")  # Inputs 10 digits account number.

# Because we know that length of account is 10 we know how many Xs we need to use to cover account number.
# We use 6 Xs.


print('XXXXXX' + accountNumber[-4:])                 # Displays result such as 6 Xs and last four digits of account number.
                                                     # To find out last four digits we used negative indexing. 
                                                     # In case of this program -1 refers to the last element,
                                                     # -2 refers to the second-to-last element, and so on. Omnit end index
                                                     # means the end of the sequence.