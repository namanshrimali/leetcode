class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        running_sum = nums[0]
        max_sum = nums[0]
        for i in range(1, len(nums)):
            if running_sum < 0 and nums[i] > running_sum:
                running_sum = nums[i]

            else:
                running_sum += nums[i]
            max_sum = max(max_sum, running_sum)
        return max_sum
        