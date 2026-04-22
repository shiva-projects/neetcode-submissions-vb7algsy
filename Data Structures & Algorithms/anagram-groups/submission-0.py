class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}
        for i in range(len(strs)):
            index_maping = [0] * 26
            for j in range(len(strs[i])):
                index_maping[ord(strs[i][j]) - ord("a")] += 1
            index_maping = tuple(index_maping)
            if index_maping in group:
                group[index_maping].append(strs[i])
            else:
                group[index_maping] = [strs[i]]
        return list(group.values())