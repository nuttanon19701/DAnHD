#Monte Carlo Simulation of the distance of angel
import numpy
import pylab
import random
import matplotlib.pyplot as plt
import math
from scipy.stats import sem
import statistics
from numpy import linalg as LA

# defining dimension
n = 2
# defining epsilon
#e = float(input('Error except: '))
# defining step
c = 1
# find the radius
k = 25

# defining the number of steps
V = math.ceil(((math.pi**(n/2))*((k+c)**n - (k-1)**n) )/(math.gamma((n/2)+1)))
print("V=", V)
V = 10000
number_of_iteration = 500
success = []
highest=[]
for i in range(number_of_iteration):
# creating two array for containing x and y coordinate
# of size equals to the number of size and filled up with 0's
    x = numpy.zeros(n)
    dx = numpy.zeros(n)
    distance = []
# filling the coordinates with random variables
    for j in range(V):
        dx = numpy.random.randint(-c,c+1,size=n)
        x = x + dx
        d = LA.norm(x)
        distance.append(d)
    high = max(distance)
    print('No.', i, ': highest ', high)
    highest.append(high)
    if k > high: success.append(1)
    else: success.append(0)
    plt.plot(distance)
#h = int(numpy.ceil(max(highest)))
#plt.hist(highest,bins= h)
success_rate = statistics.mean(success)
print("The success rate is ", success_rate)
print("The Standard Error is ", sem(success))

plt.show()
