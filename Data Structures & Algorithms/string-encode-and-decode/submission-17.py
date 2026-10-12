class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for i in strs:
            res += str(len(i)) + "#" + i
        return res

    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        while i < len(s):
            j = i
            num = ""
            while s[j].isdigit():
                num += s[j]
                j += 1
            i = j + 1
            res.append(s[i:i + int(num)])
            i = i + int(num)
        return res
