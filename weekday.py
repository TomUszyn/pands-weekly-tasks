# weeday.py
# Program outputs whether or not today is a weekday.
# author: Tomasz Uszynski

from datetime import datetime                               # Imports the datetime class from the datetime module.

currentDate = datetime.now()                                # Get current datetime.

day = currentDate.weekday()                                 # Return day of the week, where Monday == 0 ...
                                                            # Sunday == 6.

if day < 5:                                                 # Realize if statement.
    print ("Yes, unfortunately today is a weekday.")
else:                                                       # Realise  else statement.
    print ("It is the weekend, yay!")


# To write a program that outputs whether or not today is a weekday, we will need to use the Python datetime module, 
# which provides various functions to work with dates and times. One of the functions is weekday(),
# which returns the day of the week as an integer, where Monday is 0 and Sunday is 6. We can use this function to check 
# if the current date is a weekday or a weekend, and print a message accordingly.
# To learn more about the Python datetime module and the weekday() function visit these websites:
# https://pynative.com/python-get-the-day-of-week/; https://www.programiz.org/1340/python-code-to-get-day-of-week
# To learn more about the Python if elif else statements visit this website:
# https://www.programiz.com/python-programming/if-elif-else