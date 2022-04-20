class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        count_nums = {}
        for num in nums:
            count_nums[num] = count_nums.get(num, 0) + num
        
        sorted_nums = sorted(count_nums.keys())
        n = len(sorted_nums)
        second_prev, prev = 0, count_nums[sorted_nums[0]]

        for i in range(1, n):
            num = sorted_nums[i]
            if sorted_nums[i-1] == num - 1:
                curr_max = max(second_prev + count_nums[num], prev)
            else:
                curr_max = prev + count_nums[num]
            second_prev = prev
            prev = curr_max
        return prev 