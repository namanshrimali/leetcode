class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        found = {}
        for i, num in enumerate(nums):
            complement = target-num
            if complement in found:
                return [found[complement], i]
            found[num] = i
