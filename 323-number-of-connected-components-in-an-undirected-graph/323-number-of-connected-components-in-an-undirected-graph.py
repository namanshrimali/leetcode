class DisjointSet:
    def __init__(self, n):
        self.parents = [i for i in range(n)]
        self.connected_count = [1]*n
    
    def union(self, a, b):
        parent_a, parent_b = self.get_parent(a), self.get_parent(b)
        if parent_a == parent_b:
            return
        if self.connected_count[parent_a] > self.connected_count[parent_b]:
            self.parents[parent_b] = parent_a
            self.connected_count[parent_a] += self.connected_count[parent_b]
        else:
            self.parents[parent_a] = parent_b
            self.connected_count[parent_b] += self.connected_count[parent_a]
            
    
    def get_parent(self, a):
        while a != self.parents[a]:
            self.parents[a] = self.parents[self.parents[a]]
            a = self.parents[a]
        return a
        
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        d_set = DisjointSet(n)
        for a, b in edges:
            d_set.union(a, b)
        uniq_graphs = set()
        for i in range(n):
            uniq_graphs.add(d_set.get_parent(i))
        return len(uniq_graphs)
