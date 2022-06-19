class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        result = []
        def two_sum(j, target):
            seen_set = set()
            while j < n:
                complement = target - nums[j]
                if complement in seen_set:
                    result.append([-target, complement, nums[j]])
                    while j+1 < n and nums[j] == nums[j+1]:
                        j+=1
                seen_set.add(nums[j])
                
                j+=1
    
        i = 0
        while i < n:
            if nums[i] > 0:
                break
            if i < 1 or nums[i-1] != nums[i]:
                two_sum(i+1, -nums[i])

            i += 1
        return result
            