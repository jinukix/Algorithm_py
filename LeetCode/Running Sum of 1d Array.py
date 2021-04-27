from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        n = 0
        result = []
        for num in nums:
            n += num
            result.append(n)

        return result
