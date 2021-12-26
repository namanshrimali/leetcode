class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left, right= 0,0
        sol = 0
        window_zeros = 0
        while(right<len(nums)):
            if nums[right]==0:
                window_zeros+=1
            while(window_zeros>k):
                if nums[left]==0:
                    window_zeros-=1
                left+=1
            right+=1
            sol = max(sol, right-left)
            
        return sol