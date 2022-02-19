class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index, num in enumerate(nums):
            for another_index, another_num in enumerate(nums[index+1:]):
                if num+another_num == target:
                    return [index, index+another_index+1] 

