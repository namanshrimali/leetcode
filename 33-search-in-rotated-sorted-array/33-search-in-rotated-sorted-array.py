class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def find_pivot():
            left, right = 0, len(nums)-1
            while left < right:
                mid = (left+right)//2
                if nums[mid] >= nums[0] and nums[mid] > nums[-1]:
                    left = mid + 1
                else:
                    if (mid == 0 or nums[mid-1]> nums[mid]) and (mid == len(nums)-1 or nums[mid+1]>nums[mid]):
                        return mid
                    else:
                        right = mid - 1
            return left
        
        
        def binary_search(left, right):
            while left <= right:
                mid = (left + right)//2
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            return -1
        
        pivot_idx = find_pivot()
        print(pivot_idx)
        
        if target == nums[pivot_idx]:
            return pivot_idx
        elif target > nums[pivot_idx] and target <= nums[-1]:
            return binary_search(pivot_idx, len(nums)-1)
        else:
            
            return binary_search(0, pivot_idx - 1)