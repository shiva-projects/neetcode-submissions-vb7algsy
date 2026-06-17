class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        print("shiva")
        hash1 = defaultdict(int)
        count = 0
        for i in words:
            hash2 = defaultdict(int)
            for j in i:
                if not count:
                    hash2[j] = hash2[j] + 1
                else:
                    if j in hash1 and hash2[j] < hash1[j]:
                        hash2[j] = hash2[j] + 1
            count += 1
            hash1 = hash2
        res = ""
        for k, v in hash1.items():
            res += str(k) * v
        return list(res)