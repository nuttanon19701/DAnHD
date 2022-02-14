#Comparison between the final position of angel and hitting time
import numpy
import matplotlib.pyplot as plt
import math
import statistics

# defining dimension
n = 2
# defining step
c = 1
# maximum radius
k_total = 100
success_rate_1 = []
success_rate_2 = []
for k in range(1,k_total+1):
# defining the number of steps
    V = math.ceil(((math.pi**(n/2))*((k+c)**n - (k-1)**n) )/(math.gamma((n/2)+1)))
    print("k=", k)
    print("V=", V)
    number_of_iteration = 10000
    success_1 = []
    success_2 = []
    highest=[]
    for i in range(number_of_iteration):
# creating two array for containing x and y coordinate
# of size equals to the number of size and filled up with 0's
        distance = []
# filling the coordinates with random variables
        dx = numpy.random.randint(-c,c+1,size=(V,n))
        x = numpy.sum(dx,axis=0)
        d = numpy.linalg.norm(x)
        distance.append(d)
        high = max(distance)
        print('No.', i, ': highest ', high)
        highest.append(high)
        if k > high: success_1.append(1)
        else: success_1.append(0)
        if d < k: success_2.append(1)
        else: success_2.append(0)
    success_rate_1.append(statistics.mean(success_1))
    print('success rate 1: ', success_rate_1[k-1])
    success_rate_2.append(statistics.mean(success_2))
    print('success rate 2: ', success_rate_2[k-1])
x = range(1,k_total+1)

plt.plot(x,success_rate_1,linestyle='solid')
plt.plot(x,success_rate_2,linestyle='dashed')
plt.show()