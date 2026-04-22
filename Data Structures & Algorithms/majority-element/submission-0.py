from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = defaultdict(int)
        for i in range(len(nums)):
            if nums[i] in count:
                count[nums[i]] += 1
            else:
                if count:
                    for k in list(count.keys()):
                        count[k] -= 1
                        if count[k] == 0:
                            count.pop(k)
                else:
                    count[nums[i]] += 1

        for i in count.keys():
            if count[i] > 0:
                return i