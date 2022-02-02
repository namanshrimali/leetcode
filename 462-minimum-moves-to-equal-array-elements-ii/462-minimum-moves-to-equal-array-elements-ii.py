class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        mid = len(nums)//2
        total_moves = 0
        for num in nums:
            total_moves += abs(nums[mid]-num)
        return total_moves