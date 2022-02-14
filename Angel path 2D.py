# Python code for simulate the path of angel in 2D
import numpy
import pylab
import random
import matplotlib.pyplot as plt

# defining the number of steps 
n = 981
k = 1
# creating two array for containing x and y coordinate
# of size equals to the number of size and filled up with 0's
x = numpy.zeros(n)
y = numpy.zeros(n)


# filling the coordinates with random variables
for i in range(n):
    dx = random.randint(-k, k)
    dy = random.randint(-k, k)
    x[i] = x[i-1] + dx
    y[i] = y[i-1] + dy
# plotting stuff:
figure, axes = plt.subplots()
Drawing_uncolored_circle = plt.Circle((0, 0),
                                      78,
                                      fill=False)

axes.set_aspect(1)
axes.add_artist(Drawing_uncolored_circle)
#pylab.title("Random Walk ($epsilon = 0.5" + "$ with angel power c =" + str(k)+ ")")
pylab.plot(x, y)
pylab.plot(x[n-1], y[n-1],'ro')
#pylab.savefig("rand_walk" + str(n) + ".png", bbox_inches="tight", dpi=600)
pylab.xlim(-80, 80)
pylab.ylim(-80, 80)
pylab.show()
