from typing import List


class Solution:
    def __init__(self):
        self.target = []

    def createTargetArray(self, nums: List[int], index: List[int]):
        for num, idx in zip(nums, index):
            new_target = self.target[:idx] + [num] + self.target[idx:]
            self.target = new_target

        return self.target