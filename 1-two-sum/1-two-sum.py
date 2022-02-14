# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for index, num in enumerate(nums):
#             for another_index, another_num in enumerate(nums[index+1:]):
#                 if num+another_num == target:
#                     return [index, index+another_index+1] 

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        valueMap = {}
        for index, num in enumerate(nums):
            another_value = target-num
            if another_value in valueMap:
                return [valueMap[another_value], index]
            valueMap[num] = index