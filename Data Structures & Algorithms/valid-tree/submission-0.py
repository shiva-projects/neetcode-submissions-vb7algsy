class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        hash = {i : [] for i in range(n)}
        for i, j in edges:
            hash[i].append(j)
            hash[j].append(i)
        visited = set()
        def dfs(cur, pre):
            nonlocal hash
            if cur in visited:
                return False
            visited.add(cur)
            for child in hash[cur]:
                if child == pre:
                    continue 
                if not dfs(child, cur):
                    return False
            return True 
            

        return dfs(0, - 1) and len(visited) == n