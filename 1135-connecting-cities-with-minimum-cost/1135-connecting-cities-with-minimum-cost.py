class DisjointSet:
    def __init__(self, n):
        self.parents = [i for i in range(n+1)]
        self.weights = [1] * (n+1)
        
    def union(self, a, b):
        parent_a, parent_b = self.find_parent(a), self.find_parent(b)
        if parent_a == parent_b:
            return
        if self.weights[parent_a] > self.weights[parent_b]:
            self.parents[parent_b] = parent_a
            self.weights[parent_a] += self.weights[parent_b]
        else:
            self.parents[parent_a] = parent_b
            self.weights[parent_b] += self.weights[parent_a]    
    
    def is_connected(self, a, b):
        return self.find_parent(a) == self.find_parent(b)
    
    def find_parent(self, a):
        while a != self.parents[a]:
            self.parents[a] = self.parents[self.parents[a]]
            a = self.parents[a]
        return a
            
class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        connections.sort(key = lambda a: a[2])
        total_cost, total_connections = 0, 0
        
        dj = DisjointSet(n)
        
        for x, y, cost in connections:
            if dj.is_connected(x, y):
                continue
            dj.union(x, y)
            total_cost += cost
            total_connections += 1

        return total_cost if total_connections == n-1 else -1