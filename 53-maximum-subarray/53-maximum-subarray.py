class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        total, largest_sum = nums[0], nums[0]
        for num in nums[1:]:
            if total < 0 and num > total:
                total = num
            else:
                total += num
            largest_sum = max(largest_sum, total)
        return largest_sum
        