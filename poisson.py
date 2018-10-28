from numpy import random
from matplotlib import pyplot

lam = 10
sample = 3000

#Generating random numbers using poisson function along with random function
data = random.poisson(lam,sample)
#printing graph's y values
print(data)

#Drawing histogram using pyplotsnhist function which takes our y-axis data
hgraph = pyplot.hist(data)
#the title of our graph
pyplot.title("Histogram using poisson function")
#showing the histograph
pyplot.show()