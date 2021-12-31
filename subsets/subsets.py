class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        n = len(nums)
        for i in range(2**n):
            mask = bin(i)[2:].zfill(n)
            result.append([nums[i] for i in range(n) if mask[i]=='1'])
        return result