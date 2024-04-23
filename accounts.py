# accounts.py
# Program reads in account number and outputs the account number
# with only the last 4 digits showing (All digits except last 4 replaced with Xs).
# author: Tomasz Uszynski

accountNumber = input("Please enter an account number.: ")  # Inputs account number.
accountNumberlength = len(accountNumber)                    # Checks length of account number.
toHide = accountNumber[:-4]                                 # Declarates with part will be hide.
lengthOftoHide = len(toHide)                                # Checks length of digits to hide.
x = 'X'                                                     # Declarates sign used to cover group of digits.
result = x * lengthOftoHide                                 # Counts how many Xs are needed.
print(result+accountNumber[-4:])                            # Prints out expected result.