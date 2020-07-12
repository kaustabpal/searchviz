import random
from matplotlib import pyplot as plt
import matplotlib.animation as animation
import math
import time
import os

def closest(nodes_x, nodes_y,rand_node):
    min_d=9999999999999
    l=len(nodes_x)
    closest_node_x = nodes_x[0]
    closest_node_y = nodes_y[0]
    for i in range(l):
        temp_node_x = nodes_x[i]
        temp_node_y = nodes_y[i]
        d=math.sqrt(((rand_node[1]-temp_node_y)**2 + (rand_node[0]-temp_node_x)**2))
        if(d<min_d):
            closest_node_x = temp_node_x
            closest_node_y = temp_node_y
            min_d = d
    return closest_node_x, closest_node_y, min_d

x_lim = 100
y_lim = 100
start_x = x_lim/2
start_y = y_lim/2
nodes_x = []
nodes_y = []
nodes_x.append(start_x)
nodes_y.append(start_y)
fig1 = plt.figure()
# plt.scatter(start_x, start_y, color='#000000', marker='.')
plt.plot(start_x, start_y, 'k')
for i in range(1000):
    x=random.uniform(0,100)
    y=random.uniform(0,100)
    closest_node_x, closest_node_y, min_d = closest(nodes_x, nodes_y, [x,y])
    t = 1/min_d
    new_node_x = ((1-t)*closest_node_x + t*x)
    new_node_y = ((1-t)*closest_node_y + t*y)
    nodes_x.append(new_node_x)
    nodes_y.append(new_node_y)
    plt.plot([new_node_x,closest_node_x],[new_node_y, closest_node_y], 'k')
    plt.xlim([0,110])
    plt.ylim([0,110])
    plt.draw()
    plt.savefig("video/{}.png".format(i))
    plt.pause(1/140)
os.system('ffmpeg -framerate 25 -i video/%d.jpg -c:v libx264 -profile:v high -crf 20 -pix_fmt yuv420p rrt.mp4')
