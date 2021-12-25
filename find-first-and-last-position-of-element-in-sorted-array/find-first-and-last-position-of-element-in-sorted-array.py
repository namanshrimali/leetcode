class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def find_start(first, last):
            while(first<last):
                mid = (first+last)//2
                if nums[mid] == target:
                    if mid == 0 or nums[mid-1]!=target:
                        return mid
                    else:
                        last = mid-1
                else:
                    first = mid+1
            return last
        
        def find_end(first, last):
            while(first<last):
                mid = (first+last)//2
                if nums[mid] == target :
                    if mid == len(nums)-1 or nums[mid+1]!=target:
                        return mid
                    else:
                        first = mid+1
                else:
                    last = mid-1
            return first
        
        first, last = 0, len(nums)-1
        start, end = -1,-1
        
        while(first<=last):
            mid = (first+last)//2
            if nums[mid] == target:
                start = find_start(0, mid)
                end = find_end(mid, len(nums)-1)
                break
            elif nums[mid] < target:
                first = mid+1
            else:
                last = mid-1
        return [start, end]