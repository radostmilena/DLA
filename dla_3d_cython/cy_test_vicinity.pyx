import numpy as np

def cy_test_vicinity(self, double[:, :, :] grid, long[:] center, long x0, long y0, long z0):
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
        cdef int isum
        cdef float dist
        cdef long[:] new_indices
        cdef long[:] a
        array = []

        dist = np.sqrt((x0-center[0])**2 + (y0-center[1])**2 + (z0-center[2])**2)
        if dist > self.inner_radius:
            return 0, dist

        isum = 0

        array = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1], [-1, 0, 0], [0, -1, 0], [0, 0, -1]], dtype=long)
        for a in array:
            new_indices = np.add([x0, y0, z0], a).astype(int)
            if grid[new_indices[0]][new_indices[1]][new_indices[2]] == 1:
                isum += 1

        return isum, dist
