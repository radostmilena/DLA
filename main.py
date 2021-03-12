#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt
from dla_3d import initialize_system, random_walk

isy = initialize_system(6)
empty_grid = isy.initialize_grid()
grid, center = isy.find_center()
print(center)

rw = random_walk(grid, center, 28, 30)

for i in range(1, 35000, 1):
    grid = rw.walk(grid)

print(np.where(grid == 1))
np.save('grid.dat', grid)
