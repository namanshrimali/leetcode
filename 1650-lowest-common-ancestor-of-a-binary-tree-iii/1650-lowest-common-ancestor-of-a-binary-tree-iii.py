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
        p_family = set()
        while p:
            p_family.add(p)
            p = p.parent
        while q and q not in p_family:
            q = q.parent
        return q