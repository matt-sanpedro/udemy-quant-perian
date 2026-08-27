"""
The figure object in matplotlib
    - add axes for plotting
    - provides robust controls over entire plot
"""
import numpy as np
import matplotlib.pyplot as plt

# DATA
a = np.linspace(0,10,11)
print('DATA: {}\nTYPE: {}'.format(a, type(a)))
b = a**4
x = np.arange(0,10)
y = 2*x

# FIGURE
fig = plt.figure()
print(fig.get_axes)

# LARGE AXES
# .add_axes([x0, y0, Width, Height]) in terms of fractional distance in the canvas
axes1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])
axes1.plot(a,b)
# uncomment below if axis does not show by default
# axes1.tick_params(axis='both', which='both', labelsize=10)
axes1.set_xlim(0,8)
axes1.set_ylim(0,8000)
axes1.set_xlabel('x-axis')
axes1.set_ylabel('y-axis')
axes1.set_title('Power of 4')

# SMALL AXES
axes2 = fig.add_axes([0.2,0.5,0.25,0.25])
axes2.plot(a,b)
axes2.set_xlim(1,2)
axes2.set_ylim(0,20)
axes2.set_xlabel('x-axis')
axes2.set_ylabel('y-axis')
axes2.set_title('Range change')

# save figure
plt.savefig('output/figsandaxes.png')

# display figure if running .py script
plt.show()
