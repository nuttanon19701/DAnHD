import numpy
import seaborn as sns; sns.set_theme()
import matplotlib.pyplot as plt
import random

def walk(x,y):
    dx = numpy.random.randint(-c, c+1)
    dy = numpy.random.randint(-c, c+1)
    x_new = x + dx
    y_new = y + dy
    return (x_new,y_new)

def approx_dist(x,y):
    for i in range(1000):
    # creating two array for containing x and y coordinate
    # of size equals to the number of size and filled up with 0's
    # filling the coordinates with random variables
        x_old = x
        y_old = y
        j = 0
        while j < 10:
            (x_new, y_new) = walk(x_old,y_old)
            if [x_new,y_new] in D:
                #print('-----')
                continue
            else:
                x_old = x_new
                y_old = y_new
                j =j+1
        index = vector_index.index([x_new,y_new])
        #print(index)
        vector[index][-1] = vector[index][-1] +1
    frequency = []
    for v in vector_index:
        if v in D:
            frequency.append(-100)
        else:
            index = vector_index.index(v)
            frequency.append(vector[index][-1])
    return frequency

def Lattice_ring(k,c):
    if (c <= 0):
        return None
    list = []
    for x in range(-k-c-1, k+c+2):
        for y in range(-k-c-1, k+c+2):
            if (k <= numpy.linalg.norm([x,y]) <= k+c+1 ): list.append([x,y])
    return list
#number of grid
n = 100

#create vector of lattice and index
vector = []
vector_index = []
for y in list(reversed(range(-n,n+1))):
    for x in range(-n,n+1):
        vector.append([x,y,1])
        vector_index.append([x, y])
#print(vector)

#c = power of angel
c=3
#D = Destroy square
D = []
#(x,y) = initial position of angel
x = 0
y = 0
#k = radius destroy square
k = 80

devil_strat = [item for item in Lattice_ring(k,c) if item not in D]
i=0
while len(devil_strat) > 0:
    i = i+1
#devil move
    freq = []
    frequency_devil = []
    for v in vector_index:
        if (v in devil_strat and v != [x,y]): frequency_devil.append(1)
        else: frequency_devil.append(0)
    #print(frequency_devil)
    for j in vector:
        j[-1] = 1
    freq = approx_dist(x,y)
    prob_of_devil = [i1 * i2 for i1, i2 in zip(frequency_devil, freq)]
    #print(prob_of_devil)
    #print(random.choices(vector_index, weights=prob_of_devil))
#update
    D.append(random.choices(vector_index, weights=prob_of_devil)[0])
    devil_strat = [item for item in Lattice_ring(k, c) if item not in D]
    freq = approx_dist(x, y)
#print graph
    change = ((numpy.asarray(freq)).reshape(2*n+1,2*n+1))
    x_axis_labels = range(-n,n+1)
    y_axis_labels = list(reversed(range(-n,n+1)))
    ax = sns.heatmap(change, cmap="Blues", yticklabels=False, xticklabels=False)
    plt.title("Angel is at {}".format([x,y]))
    plt.savefig('my_angel {0}.png'.format(i))
    #print("Vertex left = ", devil_strat)
    #rint("Destroy Vertex = ", D)
    plt.close()
    #plt.show()
# angel move
    (x_1,y_1) = walk(x,y)
    while [x_1,y_1] in D:
        (x_1, y_1) = walk(x, y)
    angel = [x_1,y_1]
    print(angel)
    x = angel[0]
    y = angel[1]
