class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hash_map = {}
        hash_map[0] = 1
        sum_ = 0
        counter = 0
        for num in nums:
            sum_+=num
            if sum_-k in hash_map:
                counter+= hash_map[sum_ - k]
            if sum_ in hash_map:
                hash_map[sum_] += 1
            else:
                hash_map[sum_] = 1
        return counter