# Python code for 2D random walk.
import numpy
import pylab
import random
import matplotlib.pyplot as plt
import math
from scipy.stats import sem
import statistics

# defining epsilon
e = float(input('Error except: '))
# defining step
c = int(input('step size: '))
# find the radius
k = 1
E = math.exp(-3*k*k/(2*math.pi*c*(c+1)*(c+1)*(2*k+c-1)))
while E > e:
    if E > e :
        k = k+1
        E = math.exp(-3*k*k/(2*math.pi*c*(c+1)*(c+1)*(2*k+c-1)))
    else: break
k = k+1
print("k=", k)

# defining the number of steps
V = math.ceil(math.pi*(c+1)*(2*k+c-1))
print("V=", V)

number_of_iteration = 100000
success = []
distance = []
for i in range(number_of_iteration):

# filling the coordinates with random variables
    dx = numpy.random.randint(-c, c + 1, size=(V, 2))
    x = numpy.sum(dx, axis=0)

# calculate the distance
    d = numpy.linalg.norm(x)
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