class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        seen_sum = {
            0 : 1
        }
        total = 0
        count = 0
        for num in nums:
            total += num
            if total - k in seen_sum:
                count += seen_sum[total-k]
            seen_sum[total] = seen_sum.get(total, 0) + 1
                
        return count