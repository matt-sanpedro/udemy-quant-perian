import matplotlib.pyplot as plt

'''
## Task Two: Creating plots from data points

In finance, the yield curve is a curve showing several yields to maturity or interest rates 
across different contract lengths (2 month, 2 year, 20 year, etc. ...) for a similar debt contract. 
The curve shows the relation between the (level of the) interest rate (or cost of borrowing) and 
the time to maturity, known as the "term", of the debt for a given borrower in a given currency.

The U.S. dollar interest rates paid on U.S. Treasury securities for various maturities are closely 
watched by many traders, and are commonly plotted on a graph such as the one on the right, which is 
informally called "the yield curve".

**For this exercise, we will give you the data for the yield curves at two separate points in time. 
Then we will ask you to create some plots from this data.**

## Part One: Yield Curve Data

**We've obtained some yield curve data for you from the [US Treasury Dept.](https://www.treasury.gov/resource-center/data-chart-center/interest-rates/pages/textview.aspx?data=yield). 
The data shows the interest paid for a US Treasury bond for a certain contract length. The labels 
list shows the corresponding contract length per index position.**
'''
labels = ['1 Mo','3 Mo','6 Mo','1 Yr','2 Yr','3 Yr','5 Yr','7 Yr','10 Yr','20 Yr','30 Yr']

july16_2007 = [4.75,4.98,5.08,5.01,4.89,4.89,4.95,4.99,5.05,5.21,5.14]
july16_2020 = [0.12,0.11,0.13,0.14,0.16,0.17,0.28,0.46,0.62,1.09,1.31]

fig = plt.figure()
ax = fig.add_axes([0.1,0.1,0.66,0.8])
ax.set_xlabel('Contract Length')
ax.set_ylabel('Interest Rate (%)')
ax.plot(labels,july16_2007,label='2007')
ax.plot(labels,july16_2020,label='2020')
ax.legend(loc=(1.1,0.78),fontsize='large',shadow=True)
plt.title('Interest Paid for US Treasury Bonds')
plt.show()

'''
TASK: While the plot above clearly shows how rates fell from 2007 to 2020, 
putting these on the same plot makes it difficult to discern the rate differences 
within the same year. Use .suplots() to create the plot figure below, which shows 
each year's yield curve.**
'''
figs,axs = plt.subplots(nrows=2,ncols=1)
axs[0].plot(labels,july16_2007)
axs[0].set_title('July 16th, 2007')
axs[1].plot(labels,july16_2020)
axs[1].set_title('July 16th, 2020')
figs.subplots_adjust(wspace=1,hspace=0.5)
plt.show()

'''
**BONUS CHALLENGE TASK: Try to recreate the plot below that uses twin axes. 
While this plot may actually be more confusing than helpful, its a good exercise 
in Matplotlib control.**
'''
figb, axb = plt.subplots()

axb.plot(labels, july16_2007, lw=2, color='blue')
axb.set_ylabel('2007', fontsize=18, color='blue')
for label in axb.get_yticklabels():
    label.set_color('blue')
    
ax2 = axb.twinx()
ax2.plot(labels, july16_2020, lw=2, color="red")
ax2.set_ylabel('2020', fontsize=18, color="red")
for label in ax2.get_yticklabels():
    label.set_color("red")
plt.show()
