import matplotlib.pyplot as plt
import numpy as np

# DATA
a = np.linspace(0,10,11)
print('DATA: {}\nTYPE: {}'.format(a, type(a)))
b = a**4

# FIGURE
fig = plt.figure(figsize=(8,10),dpi=200)
# initial points must start at 0.1 fraction distance to display axes
axes1 = fig.add_axes([0.1,0.1,0.8,0.8])
axes1.plot(a,b)
axes1.set_xlim(0,8)
axes1.set_ylim(0,5000)
axes1.set_xlabel('x-axis')
axes1.set_ylabel('y-axis')
axes1.set_title('Power of 4')

# save figure and display
plt.savefig('output/figsandaxes.png',bbox_inches='tight')
plt.show()
