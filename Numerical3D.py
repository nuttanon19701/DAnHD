# Python code for higher Dimension random walk.
import numpy
import pylab
import random
import matplotlib.pyplot as plt
import math
from scipy.stats import sem
import statistics
from numpy import linalg as LA

# defining dimension
n = 3
# defining epsilon
#e = float(input('Error except: '))
# defining step
c = 1
# find the radius
k = 50
#E = math.exp(-3*k*k/(2*math.pi*c*(c+1)*(c+1)*(2*k+c-1)))
#while E > e:
#    if E > e :
#        k = k+1
#        E = E = math.exp(-3*k*k/(2*math.pi*c*(c+1)*(c+1)*(2*k+c-1)))
#    else: break

#print("k=", k)

# defining the number of steps
V = math.ceil(((math.pi**(n/2))*((k+c)**n - (k-1)**n) )/(math.gamma((n/2)+1)))
print("V=", V)

number_of_iteration = 100000
success = []
distance = []
for i in range(number_of_iteration):
# creating two array for containing x and y coordinate
# of size equals to the number of size and filled up with 0's
    x = numpy.zeros(n)
    dx = numpy.zeros(n)
# filling the coordinates with random variables
    for j in range(V):
        dx = numpy.random.randint(-c,c+1,size=n)
        x = x + dx

# calculate the distance
    d = LA.norm(x)
    distance.append(d)
    print('No.', i, ': Distance ', d)
    if d < k:
        success.append(1)
        print('success')
    else: success.append(0)
success_rate = statistics.mean(success)
Expected_distance = statistics.mean(distance)
print("The expected distance is ", Expected_distance)
print("The Standard deviation is ", statistics.stdev(distance))
print("The Standard Error of distance is ", sem(distance))
print("The success rate is ", success_rate)
print("The Standard Error is ", sem(success))