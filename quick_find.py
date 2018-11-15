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
