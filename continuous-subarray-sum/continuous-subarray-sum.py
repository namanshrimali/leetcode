class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        hash_map = {0: -1}
        sum_arr = []
        total = 0
        for idx, num in enumerate(nums):
            total+=num
            k_mult = total%k
            if k_mult in hash_map:
                if idx-hash_map[k_mult]>=2:
                    return True
            else:
                hash_map[k_mult] = idx
        return False