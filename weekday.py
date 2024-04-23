# weekday.py
# Program outputs whether or not today is a weekday.
# author: Tomasz Uszynski

from datetime import datetime                               # Imports the datetime class from the datetime module.

currentDate = datetime.now()                                # Get current datetime.
day = currentDate.weekday()                                 # Return day of the week, where Monday == 0 and Sunday == 6.

if day < 5:                                                 # Realize if statement.
    print ("Yes, unfortunately today is a weekday.")
else:                                                       # Realise  else statement.
    print ("It is the weekend, yay!")                       # Print out message.