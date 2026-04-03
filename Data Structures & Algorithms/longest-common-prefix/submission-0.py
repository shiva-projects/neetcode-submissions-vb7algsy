class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = strs[0]
        for i in strs:
            cur = ""
            for j in range(len(i)):
                
                if j < len(res):
                    if i[j] == res[j]:
                        cur += i[j]
                    else:
                        break
            res = cur
        return res

