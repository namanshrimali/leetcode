class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        start, end = 0, len(nums)-1
        while start<end:
            mid = (start+end)//2
            if nums[mid] > nums[mid+1]:
                # decreasing slope
                end = mid
            else:
                # increasing slope
                start = mid+1
        return start