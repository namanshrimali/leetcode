class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left_prod = [1]*n
        prod = nums[0]
        
        for i in range(1, n):
            left_prod[i] = prod
            prod *= nums[i]
        
        prod = nums[-1]
        
        for i in range(n-2, -1, -1):
            left_prod[i] *= prod
            prod *= nums[i]
            
        return left_prod