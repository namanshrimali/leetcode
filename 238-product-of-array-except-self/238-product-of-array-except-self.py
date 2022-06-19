class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left_product = nums[0]
        answer = [1]*n
        for i in range(1, n):
            answer[i] *= left_product
            left_product *= nums[i]
        right_product = nums[-1]
        for i in range(n-2, -1, -1):
            answer[i] *= right_product
            right_product *= nums[i]
        return answer