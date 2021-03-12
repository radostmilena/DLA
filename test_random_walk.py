import numpy as np
from dla_3d import initialize_system
from dla_3d import random_walk

def test_random_walk():

    arg = initialize_system(3)
    initialize_system.initialize_grid(arg)
    grid, center = initialize_system.find_center(arg)

    rw = random_walk(grid, center, 2, 3)
    point = rw.initialize_walk()
    assert np.int(np.rint(np.sqrt((point[0]-rw.center[0])**2 + (point[1]-rw.center[1])**2 + (point[2]-rw.center[2])**2))) == rw.inner_radius

    some_point = np.copy(center)
    some_point[2] += 1
    sum_, dist = rw.test_vicinity(grid, center, some_point[0], some_point[1], some_point[2])
    assert sum_ == 1
    assert dist == 1
     
    for i in range(1, 6, 1):
        grid = rw.walk(grid) 
    assert np.sum(grid) > 1
    assert np.sum(grid) <= 5 
