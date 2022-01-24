class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:        
        start, end = 0, len(arr)-1
        while(start <= end):
            mid = (start+end)//2
            
            if arr[mid]-mid-1 < k:
                start= mid+1
            else:
                end=mid-1
                
        return arr[end]+k - (arr[end]-end-1)