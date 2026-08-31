import numpy as np
import matplotlib.pyplot as plt

'''
### Task One: Creating data from an equation

It is important to be able to directly translate a real equation into a plot. \
Your first task actually is pure numpy, then we will explore how to plot it out with Matplotlib. 
The [world famous equation](https://en.wikipedia.org/wiki/Mass%E2%80%93energy_equivalence) 
from Einstein:

$$E=mc^2$$

Use your knowledge of Numpy to create two arrays: E and m , where **m** is simply 11 evenly spaced 
values representing 0 grams to 10 grams. E should be the equivalent energy for the mass. 
You will need to figure out what to provide for **c** for the units m/s, a quick google search will
 easily give you the answer (we'll use the close approximation in our solutions).

**NOTE: If this confuses you, then hop over to the solutions video for a guided walkthrough.**
'''
m = np.linspace(0,10,11)
c = 3e8
print('mass (m): {}\nspeed of light (c): {}'.format(m, c))
E = m * c**2
print('Energy (E): {}'.format(E))

'''
### Part Two: Plotting E=mc^2

Now that we have the arrays E and m, we can plot this to see the relationship between 
Energy and Mass. 

**TASK: Import what you need from Matplotlib to plot out graphs:**
'''
fig = plt.figure()
ax = fig.add_axes([0.1,0.1,0.8,0.8])
ax.plot(m,E,color='orange',lw=10)
ax.set_xlabel('Mass in Grams')
ax.set_ylabel('Energy in Joules')
plt.title('E=mc^2')
plt.show()

'''
### Part Three (BONUS)

**Can you figure out how to plot this on a logarthimic scale on the y axis? 
Place a grid along the y axis ticks as well. We didn't show this in the videos, 
but you should be able to figure this out by referencing Google, StackOverflow, 
Matplotlib Docs, or even our "Additional Matplotlib Commands" notebook. 
The plot we show here only required two more lines of code for the changes.**
'''
fig1 = plt.figure()
ax1 = fig1.add_axes([0.1,0.1,0.8,0.8])
ax1.set_yscale('log')
ax1.plot(m,E,color='orange',lw=5)
ax1.set_xlabel('Mass in Grams')
ax1.set_ylabel('Energy in Joules')
ax1.grid(True,axis='both')
ax1.grid(which='minor')
plt.title('E=mc^2')
plt.show()
