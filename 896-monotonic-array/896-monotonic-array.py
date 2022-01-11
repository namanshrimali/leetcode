class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        direction = None
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                if not direction:
                    direction = 0
            elif nums[i]>nums[i-1]:
                if direction == -1:
                    return False
                if not direction:
                    direction = 1
            elif nums[i]<nums[i-1]:
                if direction == 1:
                    return False
                if not direction:
                    direction = -1
        return True