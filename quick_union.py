class QuickUnion:

    def __init__(self, n: int) -> None:
        self._id = [i for i in range(n)]

    def _root(self, i: int) -> int:
        """
        The id of i is its parent if it is not the root, else its id is itself. Therefore, we can chase the pointers
        until we get to the top of the tree.
        """
        while i != self._id[i]:
            i = self._id[i]
        return i

    def connected(self, p: int, q: int) -> bool:
        """ Is there at least one connected path between p and q? Only if q and p are in the same tree """
        return self._root(p) == self._root(q)

    def union(self, p: int, q: int) -> None:
        """
        Register a pair of points, p and q, as connected. Let p be in tree P with root p', and q be in tree Q with root
        q'. Make q' a child of p' and therefore make Q a subtree of P. Now p and q are both in tree P.
        """
        id_p = self._root(p)
        id_q = self._root(q)
        self._id[id_p] = id_q


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
    grid = QuickUnion(grid_size)

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
