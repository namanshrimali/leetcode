class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums)-2
        while(i>=0 and nums[i]>=nums[i+1]):
            i-=1
            
        if i>=0:
            next_max_idx = i+1
            for j in range(i+1, len(nums)):
                if nums[j] <= nums[next_max_idx] and nums[j]>nums[i]:
                    next_max_idx = j
            nums[i], nums[next_max_idx] = nums[next_max_idx], nums[i]
        
        i,j = i+1, len(nums)-1
        while(i<j):
            nums[i], nums[j] = nums[j], nums[i]
            i+=1
            j-=1
        
        return nums