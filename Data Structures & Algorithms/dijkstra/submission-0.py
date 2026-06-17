class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        adj = {i : [] for i in range(n)}
        for s, d, w in edges:
            adj[s].append((w, d))
        heap = [] 
        heapq.heappush(heap, (0, src)) # distance, node
        shortest = {}
        while heap:
            weight, source = heapq.heappop(heap)
            if source in shortest :
                continue 
            shortest[source] = weight
            for w, d in adj[source]:
                if d not in shortest:
                    heapq.heappush(heap, (w + weight, d))
        for i in range(n):
            if i not in shortest:
                shortest[i] = -1
        return shortest