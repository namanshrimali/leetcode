class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        answer = []
        
        def two_sum(j, first_num):
            seen = set()
            while j < n:
                complement = -first_num - nums[j]
                if complement in seen:
                    answer.append([first_num, complement, nums[j]])
                    while j+1 < n and nums[j] == nums[j++1]:
                        j+=1
                seen.add(nums[j])
                j+=1

        for i in range(n):
            if nums[i]>0:
                break
            if i == 0 or nums[i-1] != nums[i]:
                two_sum(i+1, nums[i])
            
        return answer
        