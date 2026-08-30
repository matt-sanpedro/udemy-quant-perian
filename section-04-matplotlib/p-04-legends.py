import numpy as np
import matplotlib.pyplot as plt

# DATA
x = np.linspace(0,11,10)

# FIGURE
fig = plt.figure()
# axes below needs adjustments if legend is outside the plot
ax = fig.add_axes([0.1,0.1,0.6,0.8])
ax.plot(x,x,label='linear')
ax.plot(x,x**2,label='power of 2')
ax.plot(x,x**3,label='power of 3')
# ax.legend(loc='upper left',fontsize='large',shadow=True)
ax.legend(loc=(1.1,0.78),fontsize='large',shadow=True)

fig.savefig('output/figandlegend.png')
plt.show()
