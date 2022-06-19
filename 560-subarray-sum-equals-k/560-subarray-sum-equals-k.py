class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        seen_sum = {
            0: 1
        }
        total_sum = 0
        total_subarrays = 0
        for num in nums:
            total_sum += num
            if total_sum - k in seen_sum:
                total_subarrays += seen_sum[total_sum - k]
            
            seen_sum[total_sum] = seen_sum.get(total_sum, 0) + 1
        return total_subarrays