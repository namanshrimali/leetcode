class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # the pivot index is the index from where the array is rotated
        # pivot index is smallest element and is smaller than the element
        # left to it
        
        def get_pivot(left, right):
            # binary search to get the element which is smaller than the
            # element left to it
            if nums[left]<nums[right]:
                return left
                
            while left < right:
                mid = (left+right)//2
                if nums[mid]>nums[mid+1]:
                    return mid+1
                else:
                    if nums[mid] > nums[left]:
                        left = mid+1
                    else:
                        right = mid
            return left
        
        def binary_search(left, right):
            while left <= right:
                mid = (left+right)//2
                if nums[mid]==target:
                    return mid
                elif nums[mid] > target:
                    right = mid-1
                else:
                    left = mid+1
            return -1

        L = len(nums)
        
        if L==1:
            if nums[0]==target:
                return 0
            return -1
        
        
        pivot_idx = get_pivot(0, L-1)
        print(pivot_idx)
        if target == nums[pivot_idx]:
            return pivot_idx
        else:
            if nums[pivot_idx] < nums[0] and target >= nums[0]:
                return binary_search(0, pivot_idx-1)
            else:
                return binary_search(pivot_idx+1, L-1)
        