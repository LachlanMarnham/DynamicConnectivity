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
