class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l,r=0,len(arr)-1
        while(r-l+1>k):
            left_diff, right_diff = abs(arr[l]-x), abs(arr[r]-x)
            if left_diff <= right_diff:
                r-=1
            else:
                l+=1
        return arr[l:r+1]