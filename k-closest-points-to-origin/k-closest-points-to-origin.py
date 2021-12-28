class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        def get_euc_dist(point):
            return point[0]**2+point[1]**2    # is wrt 0
        
        def partition(l, r):
            pivot = r
            pivot_dist = get_euc_dist(points[pivot])
            i=l-1
            while(l<r):
                if get_euc_dist(points[l]) < pivot_dist:
                    i+=1
                    points[i], points[l] = points[l], points[i]
                l+=1
            i+=1
            points[i], points[r] = points[r], points[i]
            return i
        
        l, r = 0, len(points)-1
        while(True):
            pivot = partition(l, r)
            if pivot+1 == k:
                break
            elif pivot < k:
                l = pivot+1
            else:
                r = pivot-1
        return points[:k]