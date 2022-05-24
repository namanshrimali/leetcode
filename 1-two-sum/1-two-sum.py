class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complements = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in complements:
                break
            complements[num] = i
        return  [complements[complement], i]
            
        