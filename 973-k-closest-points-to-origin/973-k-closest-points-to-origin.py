class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def euc_dist(point):
            return point[0]**2+point[1]**2
        
        def partition(left, right):
            pivot = random.randint(left, right)
            points[pivot], points[right] = points[right], points[pivot]
            pivot = right
            pivot_dist = euc_dist(points[pivot])
            
            i = left-1
            
            while left<right:
                if euc_dist(points[left]) <= pivot_dist:
                    i+=1
                    points[i], points[left] = points[left], points[i]
                left+=1
            i+=1
            points[pivot], points[i] = points[i], points[pivot]
            return i
        
        start, end = 0, len(points)-1
        pivot = end+1
        while pivot!=k:
            pivot = partition(start, end)
            if pivot > k:
                end = pivot - 1
            else:
                start = pivot+1
        return points[:k]
                
        