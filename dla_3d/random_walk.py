#!/usr/bin/python3
import numpy as np

class random_walk:

    def __init__(self, grid, center, inner_radius, outer_radius):
        """
        Constructor for random walk.

        Parameters
        ----------
        grid : array-like
               Three-dimensional grid with seed in the center, initialized by the initialize_system class.
        center : array-like
                 Position of the seed.
        inner_radius : int
                       Radius of the inner sphere, where random walkers start their path.
        outer_radius : 
                       Radius of the outer sphere. If a walker leaves the outer sphere, its walk will be stopped and a new walker will be released.
        """
        self.grid = grid
        self.center = center
        self.inner_radius = inner_radius
        self.outer_radius = outer_radius

    def initialize_walk(self):
        """
        Initializes the position of the random walkers.

           Returns
           -------
           x, y, z : int
                 Initial position of the random walker on the inner sphere.
        """
        scale = np.random.rand()
        theta = 180*scale
        phi = 360*scale
        x = np.int(np.rint(self.center[0] + self.inner_radius*np.sin(theta)*np.cos(phi)))
        y = np.int(np.rint(self.center[1] + self.inner_radius*np.sin(theta)*np.sin(phi)))
        z = np.int(np.rint(self.center[2] + self.inner_radius*np.cos(theta)))
        return x, y, z

    def test_vicinity(self, grid, center, x0, y0, z0):
        """
        Search surroundings of a point for filled points and check distance from center.

           Parameters
           ----------
           grid : array-like
                 Initialized grid with filled center
           center : array-like
                 Position of the center
           x0, y0, z0 : int
                 Position of the point in question

           Returns
           -------
           dist :
                Distance of the point from the center.
           isum : int
                Sum of grid values in the vicinity of the point. Neighbour points can only vary in one point, i.e. [x0, y0, z+1] or [x0-1, y0, z0], but not [x0+1, y0+1, z0].
        """
        dist = np.sqrt((x0-center[0])**2 + (y0-center[1])**2 + (z0-center[2])**2)
        if dist > self.inner_radius:
            return 0, dist

        isum = 0

        array = [[1, 0, 0], [0, 1, 0], [0, 0, 1], [-1, 0, 0], [0, -1, 0], [0, 0, -1]]
        for a in array:
            new_indices = np.add([x0, y0, z0], a).astype(int)
            if grid[new_indices[0]][new_indices[1]][new_indices[2]] == 1:
                isum += 1

        return isum, dist

    def walk(self, grid):
        """
        Random walk of an initialized walker.

           Returns
           -------
           grid : array-like
               Updated grid after random walker has finished.
        """
        x0, y0, z0 = self.initialize_walk()
        starting_point = [x0, y0, z0]
        isum, dist = self.test_vicinity(grid, self.center, x0, y0, z0)

        while dist <= self.outer_radius:

            ## generate array where two numbers are zero and one is 1
            array = np.zeros(3)
            r = np.random.randint(0, 3, 1)
            i = np.random.choice([-1, 1], 1)
            array[r] = i

            ## get position of starting point
            indices = starting_point

            ## add array to position of starting point
            new_indices = np.add(indices, array).astype(int)

            ## assign new position 
            starting_point = [new_indices[0], new_indices[1], new_indices[2]]

            ## get isum and dist and check for filled points in surrounding/at new position
            isum, dist = self.test_vicinity(grid, self.center, new_indices[0], new_indices[1], new_indices[2])

            if isum >= 1:
                grid[new_indices[0]][new_indices[1]][new_indices[2]] = 1
                break
            elif grid[new_indices[0]][new_indices[1]][new_indices[2]] == 1:
                break
            else:
                continue

        return grid
