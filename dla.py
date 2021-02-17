#!/bin/usr/python3

import numpy as np
from random import random, seed, randrange
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure

##### define grid as matrix of zeros #####
k=8
N=2**k
grid=np.zeros([N, N])
print(grid)

##### find point closest to center #####
x,y=grid.shape
center=[np.int(np.rint(x/2)), np.int(np.rint(y/2))]
grid[center[0], center[1]]=1
print("center= " + str(center[0])+ ", " +str(center[1]))

##### define outer and inner circle #####
outer_radius=center[0]-2
inner_radius=outer_radius-3

#### initialize walk ######
seed(a=1)
plt.figure(figsize=(5,5))
x0=[]
y0=[]
for i in range (0, 120000):
	u=random()
	theta=360*u
	x0.append(center[0]+np.int(np.rint(inner_radius*np.sin(theta))))
	y0.append(center[1]+np.int(np.rint(inner_radius*np.cos(theta))))

#### random walk ####
for i in range(0, len(x0)):
	x = x0[i]
	y = y0[i]
	for i in range(0, 15000): 
		move=randrange(1, 5, 1)
		if (move==1):
			x = x-1
			y = y
		elif (move==2):
			x = x+1
			y = y
		elif (move ==3):
			x = x
			y = y-1
		else:
			x = x
			y = y+1	
	
		dist=np.sqrt((y-center[1])**2+(x-center[0])**2)	
		sum_=np.sum([grid[x+1, y], grid[x-1, y], grid[x, y-1], grid[x, y+1]])
		
		if (dist>outer_radius):		
			break
		elif (grid[x,y]==1):
			break
		elif (sum_>0):
			grid[x, y]=1
			break
		else:
			continue
plt.imshow(grid)
plt.show()
np.savetxt('grid.dat', grid)		
