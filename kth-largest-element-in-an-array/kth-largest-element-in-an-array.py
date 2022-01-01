class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def partition(low, high):
            rand_idx = random.randint(low, high)
            nums[rand_idx], nums[high] = nums[high], nums[rand_idx]
            pivot = nums[high]
            i = low-1
            for j in range(low, high):
                if nums[j] < pivot:
                    i+=1
                    nums[i], nums[j] = nums[j], nums[i]
            i+=1
            nums[high], nums[i] = nums[i], nums[high]
            return i
        low, high = 0, len(nums)-1

        while(low <= high):
            q = partition(low, high)
            if q == len(nums)-k:
                return nums[q]
            elif q > len(nums)-k:
                high = q-1
            else:
                low = q + 1
            
                
        