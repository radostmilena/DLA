#!/usr/bin/python3
import numpy as np

class initialize_system:
#    @profile
    def __init__(self, k):
        """
        Constructor for this class.

        Parameters
        ----------
        k : int
            exponent
        N : int
            base
        grid : array-like
            3d grid of dimensions N x N x N
        """
        self.k = k
        self.N = 2**self.k
 #   @profile
    def initialize_grid(self):
        """Initialize the grid using the parameters from the constructor."""
        self.grid = np.zeros([self.N, self.N, self.N])
        return self.grid
  #  @profile
    def find_center(self):
        """Find the center of the grid and fill it."""
        x = np.int(np.rint((len(self.grid[0][0]))/2))
        center = np.array([x, x, x])
        self.grid[center[0]][center[1]][center[2]] = 1
        return self.grid, center
