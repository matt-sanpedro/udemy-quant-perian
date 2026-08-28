import numpy as np
import matplotlib.pyplot as plt
a = np.linspace(0,10.,11)
b = a ** 4
x = np.arange(0,10)
y = 2 * x

# create subplots
fig,axes = plt.subplots(nrows=2,ncols=2,figsize=(10,8),dpi=200)

# axes is of data type numpy array if the nrows or ncols exceed 1
print('axes data type: {}\nshape: {}\ndata: {}'.format(type(axes), axes.shape, axes))
axes[0][0].plot(x,y)
axes[0][1].plot(x,y)
axes[1][0].plot(x,y)
axes[1][1].plot(a,b)
axes[1][1].set_ylabel('Y LABEL 1,1')
axes[1][1].set_title('TITLE 1,1')
fig.suptitle('Figure Level',fontsize=16)
# fig.set_figwidth(10)

# plt.tight_layout()

# subplots_adjust arguments are fractions of the axis
fig.subplots_adjust(wspace=1,hspace=0.5)
plt.show()

# 3x3 subplot
fig1,axes1 = plt.subplots(nrows=3,ncols=1)
for i, ax in enumerate(axes1):
    ax.plot(x,x**(i+1))
plt.tight_layout()
plt.show()

fig.savefig('output/subplots_2x2.png',bbox_inches='tight')
fig1.savefig('output/subplots_3x1.png',bbox_inches='tight')
