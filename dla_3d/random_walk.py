class random_walk:

    def __init__(self, grid, center, inner_radius, outer_radius):
    """Constructor for random walk.

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
    """Initializes the position of the random walkers.

       Returns
       -------
       x, y, z : int
             Initial position of the random walker on the inner sphere.
    """
        scale = np.random.rand()
        theta = 180*scale
        phi = 360*scale
        x = np.rint(self.center[0] + self.inner_radius*np.sin(theta)*np.cos(phi))
        y = np.rint(self.center[1] + self.inner_radius*np.sin(theta)*np.sin(phi))
        z = np.rint(self.center[2] + self.inner_radius*np.cos(theta))
        return x, y, z

    def test_vicinity(self, x0, y0, z0):
    """Search surroundings of a point for filled points and check distance from center.

       Parameters
       ----------
       x0, y0, z0 : int
             Position of the point in question

       Returns
       -------
       sum_ : int
            Sum of grid values in the vicinity of the point. Neighbour points can only vary from the point in one dimension, i.e. [x0, y0, z+1] or [x0-1, y0, z0], but not [x0+1, y0+1, z0].
       dist :
            Distance of the point from the center.
    """
        sum_ = []

        for i in range(x0-1, x0+1, 1): 
            for j in range(y0-1, y0+1, y0):
                for k in range(z0-1, z0+1, z0):
                    if (sum([i, j, k]) == sum([x0, y0, z0]) + 1 or sum([i, j, k]) == sum([x0, y0, z0]) - 1) and self.grid[i, j, k] == 1:
                       sum_ += 1

        dist = np.sqrt((x0-center[0])**2 + (y0-center[1])**2 + (z0-center[2])**2)

        return sum_, dist

    def walk(self):
    """Random walk of an initialized walker.

       Returns
       -------
       self.grid : array-like
           Updated grid after random walker has finished.
    """
        x0, y0, z0 = initialize_walk()
        starting_point = self.grid[x0, y0, z0]
        sum_, dist = test_vicinity(x0, y0, z0)

        while dist <= self.outer_radius:

            ## generate array where two numbers are zero and one is 1
            array = np.zeros(3)
            r = np.random.randint(0, 4, 1)
            array[r] = 1

            ## get position of starting point
            indices = np.where(starting_point)

            ## add array to position of starting point
            new_indices = np.add(indices, array)

            ## assign new position 
            starting_point = self.grid[tuple(new_indices)]

            ## get sum_ and dist and check for filled points in surrounding/at new position
            sum_, dist = test_vicinity(new_indices[0], new_indices[1], new_indices[2])

            if sum_ > 1:
                self.grid[[new_indices] = 1
                break
            elif self.grid[tuple(new_indices9] == 1:
                break
            else:
                continue

        return self.grid
