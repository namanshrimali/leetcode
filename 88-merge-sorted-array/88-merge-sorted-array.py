class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = len(nums1)-1
        m, n = m-1, n-1
        while(m>=0 and n>=0):
            if nums2[n] >= nums1[m]:
                nums1[i] = nums2[n]
                n-=1
            else:
                nums1[i] = nums1[m]
                m-=1
            i-=1
        if m>=0:
            nums1[0:i+1] = nums1[0:m+1]
        else:
            nums1[0:i+1] = nums2[0:n+1]
            
        return nums1