class UnionFind:
    
    def __init__(self, n: int):
        self.parent = {}
        self.rank = {}
        for i in range(n):
            self.parent[i] = i
            self.rank[i] = 1
        self.components = n

    def find(self, x: int) -> int:
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def isSameComponent(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)


    def union(self, x: int, y: int) -> bool:
        f1, f2 = self.find(x), self.find(y)
        if f1 != f2:
            if self.rank[f1] > self.rank[f2]:
                self.parent[f2] = f1
                self.rank[f1] += self.rank[f2]
            else:
                self.parent[f1] = f2
                self.rank[f2] += self.rank[f1]
            self.components -= 1
            return True 
        return False
    def getNumComponents(self) -> int:
        return self.components
