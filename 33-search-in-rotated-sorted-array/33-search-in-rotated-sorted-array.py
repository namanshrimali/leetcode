class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # target == pivot
        # target on left -> > pivot and < nums[0]
        # target on right -> > pivot and > nums[0]
        
        # first task -> find pivot
        # second task -> check whether target is on left or on right of pivot
        # find target on whichever side it is in
        
        def find_pivot():
            left, right = 0, len(nums)-1
            # pivot is element who is lesser than elements on left (if present) and elements on right (if present)
            while left < right:
                mid = (left+right)//2
                if nums[mid] >= nums[0] and nums[mid] > nums[-1]:
                    left = mid + 1
                else:   # nums[mid] <  maybe on pivot or maybe on right of pivot
                    # check if mid is pivot
                    if (mid - 1 == -1 or nums[mid-1] > nums[mid]) and (mid + 1 == len(nums) or nums[mid+1] > nums[mid]):
                        return mid
                    # if not pivot, then on right of pivot
                    right = mid - 1
            return left
        
        def binary_search(left, right):
            while left <= right:
                mid = (left+right)//2
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    right = mid-1
                else:
                    left = mid + 1
            return -1
            
        
        pivot_idx = find_pivot()

        if target == nums[pivot_idx]:
            return pivot_idx
        elif target > nums[pivot_idx] and target <= nums[-1]:
            return binary_search(pivot_idx, len(nums)-1)
        else:
            return binary_search(0, pivot_idx-1)