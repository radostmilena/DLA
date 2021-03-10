class initialize_system:

    def __init__(self, k):
    """ Constructor for this class.

    Parameters
    ----------
    k : int
        exponent
    N : int
        base
    """
        self.k = k
        self.N = 2**self.k

    def initialize_grid(self):
    """Initialize an N x N x N grid using parameters from constructor."""
        self.grid = np.empty([self.N, self.N, self.N])
        return self.grid

    def find_center(self):
    """Find the center of the grid and fill it."""
        x = np.rint(self.grid.shape/2)
        center = [x, x, x]
        self.grid[[center]] = 1
        return self.grid, center
