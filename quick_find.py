class QuickFind:

    def __init__(self, n: int) -> None:
        self._id = [i for i in range(n)]

    def connected(self, p: int, q: int) -> bool:
        """ Is there at least one connected path between p and q? """
        return self._id[p] == self._id[q]

    def union(self, p: int, q: int) -> None:
        """ Register a pair of points, p and q, as connected """
        id_p = self._id[p]
        id_q = self._id[q]
        for index, _id in enumerate(self._id):
            if _id == id_p:
                self._id[index] = id_q


if __name__ == "__main__":
    """ 
    A simple illustration. Consider the 3x3 grid (grid size of 9):

        0 - 1   2
            |
        3 - 4 - 5

        6 - 7 - 8

    The following pairs of nearest neighbours share a nearest-neighbour connection:
        (0, 1)
        (1, 4)
        (3, 4)
        (4, 5)
        (6, 7)
        (7, 8)

    """

    grid_size = 9
    grid = QuickFind(grid_size)

    # Register the pairs of nearest neighbours. See docstring.
    grid.union(0, 1)
    grid.union(1, 4)
    grid.union(3, 4)
    grid.union(4, 5)
    grid.union(6, 7)
    grid.union(7, 8)

    print(grid.connected(0, 5))  # True; there is a path between 0 and 5
    print(grid.connected(6, 8))  # True; there is a path between 6 and 8
    print(grid.connected(1, 7))  # False; there is no path between 1 and 7
