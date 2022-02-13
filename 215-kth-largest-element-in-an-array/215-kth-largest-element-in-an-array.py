class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def partition(start, end):
            pivot = random.randint(start, end)
            nums[pivot], nums[end] = nums[end], nums[pivot]
            pivot = end
            i = start-1
            while start<end:
                if nums[start] <= nums[pivot]:
                    i+=1
                    nums[start], nums[i] = nums[i], nums[start]
                start+=1
            i+=1
            nums[i], nums[pivot] = nums[pivot], nums[i]
            return i
        
        left, right = 0, len(nums)-1
        k = right-k+1
        pivot =  partition(left, right)
        
        while pivot != k:
            if pivot > k:
                right = pivot-1
            else:
                left = pivot+1
            pivot =  partition(left, right)
        return nums[pivot]
        