"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        visited_set = set()
        while(q):
            visited_set.add(q)
            q = q.parent
        while(p):
            if p in visited_set:
                return p
            else:
                p = p.parent
            
            