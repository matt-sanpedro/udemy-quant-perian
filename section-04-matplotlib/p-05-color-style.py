import numpy as np
import matplotlib.pyplot as plt

# DATA
x = np.linspace(0,11,10)

# FIGURE
fig = plt.figure()
# axes below needs adjustments if legend is outside the plot
ax = fig.add_axes([0.1,0.1,0.8,0.8])
lines = ax.plot(x,x,label='linear',color='black',linewidth=1.2)
# custom line spacing
lines[0].set_dashes([5,2,10,2])
ax.plot(x,x**2,label='power of 2',color='#61d62f',lw=1.5,marker='o',markerfacecolor='red',markeredgewidth=3,markeredgecolor='lightgreen')
ax.plot(x,x**3,label='power of 3',color='#650dbd',ls='--',marker='+',markersize=10)
ax.legend(loc='upper left',fontsize='large',shadow=True)

fig.savefig('output/figandstyle.png')
plt.show()
