#!/usr/bin/python3

import numpy as np
from dla_3d import initialize_system, random_walk

#initialize empty grid for k = 6, find and fill center
isy = initialize_system(6)
empty_grid = isy.initialize_grid()
grid, center = isy.find_center()
print(center)

#initialize random walk for inner_radius = 28 and outer_radius = 30
rw = random_walk(grid, center, 28, 30)

#run random walk on defined grid
for i in range(1, 35000, 1):
    grid = rw.walk(grid)

print(np.where(grid == 1))
np.save('grid.dat', grid)
