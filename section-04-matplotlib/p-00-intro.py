"""
Matplotlib: open source data visualization library
    - enables creation of static, animated, and interactive charts and graphs
    - "Grandfather" of plotting
    - inspired from MatLab
    - methods of plotting include
        1. function (basics)
        2. OOP (figures and subplots)
    - histograms will not be covered with matplotlib, seaborn used later in course
    - seaborn and pandas visualization are built directly off matplotlib

Coding basics:
    - plt.plot() call for quick functional visualizing relationships and data
    - if running .py scripts, need to add plt.show()
"""
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0,10)
y = 2*x

plt.plot(x,y)
plt.title('X vs Y Chart')
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.xlim(0,9)
plt.ylim(0,15)

# saving a plot
plt.savefig('firstplot.png')

# display the plot if running .py scripts
plt.show()
