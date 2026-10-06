# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, nums: List[Pair]) -> List[List[Pair]]:
        res = []
        for i in range(len(nums)):
            j = i - 1
            while j >= 0 and nums[j].key > nums[j + 1].key:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                j -= 1
            res.append(nums.copy())
        return res