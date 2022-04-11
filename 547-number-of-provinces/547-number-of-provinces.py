class DisjointSet:
    def __init__(self, n):
        self.parents = [i for i in range(n)]
        self.weights = [1]*n
    
    def union(self, a, b):
        parent_a, parent_b = self.get_parent(a), self.get_parent(b)
        if parent_a == parent_b:
            return
        if self.weights[parent_b] > self.weights[parent_a]:
            self.parents[parent_a] = parent_b
            self.weights[parent_b] += self.weights[parent_a]
        else:
            self.parents[parent_b] = parent_a
            self.weights[parent_a] += self.weights[parent_b]
    
    
    def are_connected(self, a, b):
        parent_a, parent_b = self.get_parent(a), self.get_parent(b)
        return parent_a == parent_b
    
        
    def get_parent(self, a):
        while a != self.parents[a]:
            self.parents[a] = self.parents[self.parents[a]]
            a = self.parents[a]
        return a
    
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        dset = DisjointSet(n)
        
        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1:
                    dset.union(i, j)
        parents = set()
        for i in range(n):
            parents.add(dset.get_parent(i))
        return len(parents)
        