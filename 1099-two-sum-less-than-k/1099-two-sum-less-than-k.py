class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        max_sum = -1
        nums.sort()
        left, right = 0, len(nums)-1
        while left < right:
            two_sum = nums[left] + nums[right]
            if two_sum >= k:
                right -= 1
            else:
                max_sum = max(max_sum, two_sum)
                left += 1
        return max_sum