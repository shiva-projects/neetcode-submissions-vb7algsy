class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        s = set()
        for i in nums:
            if i not in s:
                s.add(i)
            else:
                s.remove(i)
        return -1 if not s else max(s)