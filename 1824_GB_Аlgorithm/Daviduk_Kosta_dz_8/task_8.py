class UnionFindSet:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)

        if px == py:
            return False
        else:

            if self.rank[px] > self.rank[py]:
                self.parent[py] = px
            elif self.rank[px] < self.rank[py]:
                self.parent[px] = px
            else:
                self.parent[px] = py
                self.rank[px] += 1
            return True


class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:

        if len(connections) < n - 1:
            return -1

        S = UnionFindSet(n)
        for i in connections:
            S.union(i[0], i[1])

        s = set()
        for i in range(n):
            s.add(S.find(i))

        return len(s) - 1
