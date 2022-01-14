class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        missing = lambda x: nums[x]-nums[0]-x
        if k > missing(len(nums)-1):
            return nums[-1] + k - missing(len(nums)-1)
        low, high = 0, len(nums)-1
        while(low<high):
            mid = (low+high)//2
            if missing(mid) < k:
                low = mid+1
            else:
                high = mid
        return nums[low-1]+k-missing(low-1)