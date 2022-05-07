class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        n = len(nums)
        result = 0
        for i in range(n):
            max_with_i, min_with_i = nums[i], nums[i]
            for j in range(i, n):
                max_with_i, min_with_i = max(max_with_i, nums[j]), min(min_with_i, nums[j])
                result += max_with_i - min_with_i
        return result
