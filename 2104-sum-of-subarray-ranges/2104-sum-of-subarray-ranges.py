class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        result = 0
        for i in range(len(nums)):
            maxx, minn = nums[i], nums[i]
            for j in range(i, len(nums)):
                maxx = max(maxx, nums[j])
                minn = min(minn, nums[j])
                result += (maxx-minn)
        return result
        