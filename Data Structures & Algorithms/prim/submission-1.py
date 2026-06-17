class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        adj = {i : [] for i in range(n)}
        for s, d, w in edges:
            adj[s].append((w, d))
            adj[d].append((w, s))
        heap = []
        for w, d in adj[0]:
            heapq.heappush(heap, (w, 0, d))
        mst_weight = 0
        mst_edges = []
        visited = {0}
        while heap and len(visited) < n:
            w, s, d = heapq.heappop(heap)
            if d in visited:
                continue 
            visited.add(d)
            mst_weight += w
            mst_edges.append((s, d))
            for neigh_weight, new_neigh in adj[d]:
                if new_neigh not in visited:
                    heapq.heappush(heap, (neigh_weight, d, new_neigh))
             
        return mst_weight if len(visited) == n else -1 