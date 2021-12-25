class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for idx in range(len(nums)):
            second = target-nums[idx]
            if second in hash_map:
                return [hash_map[second],idx]
            else:
                hash_map[nums[idx]] = idx
        