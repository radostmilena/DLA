import numpy as np
from dla_3d import initialize_system

def test_initialize_system():
    
    arg = initialize_system(8)
    grid = initialize_system.initialize_grid(arg)
    new_grid, center = initialize_system.find_center(arg)
    assert new_grid[tuple(center)] == 1
