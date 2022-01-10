class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def find_first(idx):
            start, end = 0, idx
            while(start<end):
                mid = (start+end)//2
                if nums[mid]<target:
                    start = mid+1
                else:
                    end = mid
            return end
        
        def find_last(idx):
            start, end = idx, len(nums)-1
            while(start<end):
                mid = (start+end+1)//2
                if nums[mid]>target:
                    end = mid-1
                else:
                    start = mid
            return start
        
        sol = [-1, -1]
        start, end = 0, len(nums)-1
        
        while(start<=end):
            mid = (start+end)//2
            if nums[mid] == target:
                sol[0] = find_first(mid)
                sol[1] = find_last(mid)
                break
            elif nums[mid] > target:
                end = mid-1
            else:
                start = mid+1
        return sol