class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        sol = []
        nums = [lower-1, *nums, upper+1]
        for i in range(1, len(nums)):
            a = nums[i-1]+1
            b = nums[i]-1
            if a>b:
                continue
            elif a == b:
                sol.append(f"{a}")
            else:
                sol.append(f"{a}->{b}")
        
        return sol
                
                
                