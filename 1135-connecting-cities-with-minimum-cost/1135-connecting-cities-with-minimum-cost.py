class DisjointSet:
    def __init__(self, N):
        self.parents = [[1, i] for i in range(N+1)]
    
    def union(self, a, b):
        parent_a, parent_b = self.get_parent(a), self.get_parent(b)
        if parent_a == parent_b:
            return
        if self.parents[parent_a][0] > self.parents[parent_b][0]:
            self.parents[parent_b][1] = parent_a
            self.parents[parent_a][0] += self.parents[parent_b][0]
        else:
            self.parents[parent_a][1] = parent_b
            self.parents[parent_b][0] += self.parents[parent_a][0]
        
    
    def get_parent(self, x):
        while x != self.parents[x][1]:
            self.parents[x][1] = self.parents[self.parents[x][1]][1]
            x = self.parents[x][1]
        return x
        
        
    def in_in_same_group(self, a, b):
        return self.get_parent(a) == self.get_parent(b)
    
class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        connections.sort(key=lambda a: a[2])
        d_set = DisjointSet(n)
        total_cost, total_paths = 0, n-1
        for city_a, city_b, cost in connections:
            if d_set.in_in_same_group(city_a, city_b):
                continue
            d_set.union(city_a, city_b)
            total_cost += cost
            total_paths -=1
        return total_cost if total_paths == 0 else -1
            
            