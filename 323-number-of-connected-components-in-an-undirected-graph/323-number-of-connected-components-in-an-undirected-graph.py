class DisjointSet:
    def __init__(self, total_nodes):
        self.parent = [i for i in range(total_nodes)]
        self.rank = [0 for _ in range(total_nodes)]
    
    def union(self, node1, node2):
        root1, root2 = self.find(node1), self.find(node2)
        if root1 == root2:        # no union needed, already in same set
            return
        if self.rank[root1]>=self.rank[root2]:
            self.parent[root2] = root1
            self.rank[root1]+=self.rank[root2]
        else:
            self.parent[root1] = root2
            self.rank[root2]+=self.rank[root1]    
    
    def find(self, node):
        while self.parent[node] != node:
            node = self.parent[self.parent[node]]
        return node

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        disjoint_set = DisjointSet(n)
        
        for node1, node2 in edges:
            disjoint_set.union(node1, node2)
        parent_set = set()
        for i in range(n):
            parent_set.add(disjoint_set.find(i))
        return len(parent_set)