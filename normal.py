from numpy import random
from matplotlib import pyplot
 
 #matplotlib is used to draw graph using the number we randomly generated
 #These are the attributes normal function distribution
 #m = mean
m = 1000
 #stdeviation = standard deviation
stdeviation = 1
 #s = number of samples to be generated
s = 3000

#Printing out random numbers by poisson function
nongraph = random.normal(m,stdeviation,samples)
print(nongraph)

#pyplot has a hist function to draw the histograph
hgraph = pyplot.hist(nongraph,facecolor="yellow")
#graph title
pyplot.title("Histogram using normal normal function")
#Showing the histograph
pyplot.show()