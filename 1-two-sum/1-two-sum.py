class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        valueMap = {}
        for index, num in enumerate(nums):
            another_value = target-num
            if another_value in valueMap:
                return [valueMap[another_value], index]
            valueMap[num] = index