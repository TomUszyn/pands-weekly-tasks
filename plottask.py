# plottask.py
# Program that displays on the one set of axes:
# 1.Histogram of a normal distribution of a 1000 values with a mean of 5 and standard deviation of 2,
# 2.Plot of the function  h(x)=x3 in the range 0 to 10.
# author: Tomasz Uszynski


# Because the task requires to display the histogram and the plot of the function h(x)=x^3 on the one set of axes,
# we need to use the twinx() function to create a second y-axis. This function allows to create a second y-axis
# that shares the same x-axis. Using the twinx() makes plot easier to read and understand. 
# and the matplotlib library to display the histogram and the plot of the function h(x)=x^3. We also use 
# the textwrap library to wrap the title of the plot to fit within the plot. Edgecolor helps to distinguish 
# the bins in the histogram. Bins number is set to 30. to find out how many bins are needed, we can use the
# square root rule: the number of bins is the square root of the number of data points.
# We also add the mean and standard deviation to the plot. We added grid to the plot to make it easier to read.


import numpy as np                                          # Library that we will use to generate random numbers.
import matplotlib.pyplot as plt                             # Import the matplotlib library.
import textwrap                                             # Import the textwrap library.

fig, ax1 = plt.subplots()                                   # Create a figure and a set of subplots.
mu, sigma = 5, 2                                            # Mean and standard deviation
s = np.random.normal(mu, sigma, 1000)                       # Function that generates the random 1000 values with a mean of 5 and standard deviation of 2.

plt.grid(True)                                              # Add grid to the plot.

hist = ax1.hist(s, bins=30, edgecolor='black', label='Histogram')  # Create the histogram with 30 bins. Edgecolor helps to distinguish the bins.
ax1.text(4, 110, r'$\mu=5,\ \sigma=2$')                     # Add the mean and standard deviation to the plot.                         
ax1.set_xlabel('Values', color="blue")                      # Add a label to the x-axis.                      
ax1.set_ylabel('Frequency', color="blue")                   # Add a label to the y-axis.    
ax1.set_ylim(0, 120)                                        # Set the y-axis limits to 0 and 110.
ax1.legend(loc='upper left')                                # Add a legend to the plot with the location set to upper left.

def h(x):                                                   # Function that returns the value of x cubed.
    return x**3                                             # Return the value of x cubed.
x = np.linspace(0, 10, 100)                                 # Create an array of x values from 0 to 10.

ax2 = ax1.twinx()                                           # Create a second y-axis.                    
ax2.set_ylabel('h(x)', color="red")                         # Add a label to the second y-axis. 
ax2.set_ylim(0, 1200)                                       # Set the y-axis limits to 0 and 1200.
ax_twin = ax2.twiny()                                       # Create a second x-axis.

plot = ax_twin.plot(x, h(x), color='r', label=r'$h(x) = x^3$')  # Create the plot of the function h(x)=x^3.
ax_twin.set_xlabel('x', color="red")
ax_twin.set_xlim(0, 11)                                     # Set the x-axis limits to 0 and 11.

longTitle = "Histogram of a normal distribution and plot of the function "r'$h(x) = x^3$'  # Title of the plot.
wrapped_title = "\n".join(textwrap.wrap(longTitle, 50))     # Wrap the title text to fit within the plot.
plt.title(wrapped_title, loc='center', wrap=True)           # Set the title of the plot.


plt.legend(loc='upper right')                               # Add a legend to the plot with the location set to upper right.

plt.show()                                                  # Display the histogram and the plot of the function h(x)=x^3.