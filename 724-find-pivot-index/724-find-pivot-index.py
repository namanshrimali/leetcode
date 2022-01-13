class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sum_arr = [0]*len(nums)
        total = 0
        for i in range(len(nums)):
            sum_arr[i] = total
            total+=nums[i]
        total, sol = 0, -1
        for i in range(len(nums)-1, -1, -1):
            if sum_arr[i] == total:
                sol = i
            total+=nums[i]
        return sol