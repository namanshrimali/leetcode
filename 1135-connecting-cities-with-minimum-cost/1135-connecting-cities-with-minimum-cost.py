class Disjoint:
    def __init__(self, n):
        self.parents = [[i, 1] for i in range(n+1)]
    
    def is_in_same_group(self, a, b):
        return self.find(a)[0] == self.find(b)[0]
    
    def union(self, a, b):
        root_a, weight_a  = self.find(a)
        root_b, weight_b = self.find(b)
        
        if root_a == root_b:
            return
        if weight_a >= weight_b:
            self.parents[root_b][0] = root_a
            self.parents[root_a][1]+=weight_b
        else:
            self.parents[root_a][0] = root_b
            self.parents[root_b][1]+= weight_a
            
    def find(self, a):
        while a != self.parents[a][0]:
            a = self.parents[a][0]
        return self.parents[a]
        
    
        
class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        connections.sort(key=lambda a: a[2])
        paths_required = n-1
        sol, idx = 0, 0
        disjoint_set = Disjoint(n)
        
        while idx<len(connections):
            first, second, cost = connections[idx]
            idx+=1
            if disjoint_set.is_in_same_group(first, second):
                continue
            disjoint_set.union(first, second)
            sol+=cost
            paths_required-=1
        return sol if paths_required == 0 else -1
        