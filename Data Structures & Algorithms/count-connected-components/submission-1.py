class disjoint:
    def __init__(self, n):
        self.parent = {}
        self.rank = {}
        for i in range(n):
            self.parent[i] = i
            self.rank[i] = 1
        self.components  = n


    def find_parent(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find_parent(self.parent[x])
        return self.parent[x]
    
    def join(self, a, b):
        root_a, root_b = self.find_parent(a), self.find_parent(b)
        if root_a != root_b:
            if self.rank[root_a] > self.rank[root_b]:
                self.rank[root_a] += self.rank[root_b]
                self.parent[root_b] = root_a
            else:
                self.rank[root_b] += self.rank[root_a]
                self.parent[root_a] = root_b
            self.components -= 1
        
    
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        sets = disjoint(n)
        for i, j in edges:
            sets.join(i, j)
        return sets.components
