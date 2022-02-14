class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        total, count = 0, 0
        count_dict = {}
        count_dict[0] = 1
        for i in range(len(nums)):
            total+=nums[i]
            if total-k in count_dict:
                count+=count_dict[total-k]
            if total in count_dict:
                count_dict[total]+=1
            else:
                count_dict[total] = 1
        return count
            
        
        