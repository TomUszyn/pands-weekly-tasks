# bank.py
# Program that reads in two money accounts, add those accounts and shows result in EUR
# author: Tomasz Uszynski

amount1 = int(input("Enter amount1(in cent): "))    # Function input() take user input as a string, that's why we use
amount2 = int(input("Enter amount2(in cent): "))    # we used function int() to convert string to integer to perform 
                                                    # mathematical operations on it


sum = amount1 + amount2                             # Adding two amounts and store them in a variable sum

txt = "The sum of these is \u20ac{conv:.2f}"        # Define text to print out with EUR currency with is \u20ac. 
                                                    # conv should be in fixed point, two-decimal format


print(txt.format(conv=sum/100))                     # The format() is used to insert values into a string. 
                                                    # The value of conv is being replaced with the result of sum/100.
                                                    # Conv is used to covert values from cents to EUR
                                                          
