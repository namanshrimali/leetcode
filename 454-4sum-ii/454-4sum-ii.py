class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        n = len(nums1)
        sum_count = {}
        
        for i in range(n):
            for j in range(n):
                _sum = nums1[i] + nums2[j]
                sum_count[_sum] = sum_count.get(_sum, 0) + 1
        total = 0
        for i in range(n):
            for j in range(n):
                _sum = nums3[i] + nums4[j]
                total += sum_count.get(-_sum, 0)
        
        return total