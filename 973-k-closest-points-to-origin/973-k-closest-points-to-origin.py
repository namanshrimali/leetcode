class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance_from_origin(x, y):
            return math.sqrt(x**2 + y**2)
        
        def partition(start, end):
            pivot = random.randint(start, end)
            points[pivot], points[end] = points[end], points[pivot]
            pivot = end
            pivot_distance = distance_from_origin(points[pivot][0], points[pivot][1])
            i = start-1
            while(start<end):
                if distance_from_origin(points[start][0], points[start][1]) <= pivot_distance:
                    i+=1
                    points[start], points[i] = points[i], points[start]
                start+=1
            i+=1
            points[pivot], points[i] = points[i], points[pivot]
            return i
        
        left, right = 0, len(points)-1
        q = right+1
        while q!=k:
            q = partition(left, right)
            if q > k:
                right = q-1
            else:
                left = q+1
        return points[:k]
        
                
                
        