class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums)-2
        while i > -1:
            if nums[i] < nums[i+1]:
                break
            i-=1
        # the i'th number is the smallest on the right hand side
        # finding the next largest number
        if i != -1:
            # number at i is the largest number in array, and array is in descending order
            # if not that, finding the number which is just bigger than number at i
            next_largest = len(nums)-1
            while nums[next_largest] <= nums[i]:
                next_largest-=1
            nums[i], nums[next_largest] = nums[next_largest], nums[i]
        
        left, right = i+1, len(nums)-1
        while left<right:
            nums[left], nums[right] = nums[right], nums[left]
            left+=1
            right-=1
        return nums