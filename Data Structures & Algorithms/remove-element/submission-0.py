class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        replace_index = 0
        i = 0
        while i < len(nums):
            if nums[i] != val:
                nums[replace_index], nums[i] = nums[i], nums[replace_index]
                replace_index += 1
            i += 1
        return replace_index