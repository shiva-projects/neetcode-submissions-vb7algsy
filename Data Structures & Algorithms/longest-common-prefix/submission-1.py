class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = strs[0]
        for i in range(len(strs)):
            com = ""
            for j in range(min(len(strs[i]), len(res))):
                if res[j] == strs[i][j]:
                    com += res[j]
                else:
                    break
            res = com
        return res
