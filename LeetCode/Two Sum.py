class Solution:
    def twoSum(self, nums, target):
        dict = {}
        for idx, num in enumerate(nums):
            n = target - num
            if n in dict:
                return [dict[n], idx]
            dict[num] = idx
        return []