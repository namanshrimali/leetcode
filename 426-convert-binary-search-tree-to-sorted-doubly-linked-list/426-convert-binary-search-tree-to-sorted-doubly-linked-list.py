"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root is None:
            return
        
        def dfs(node):
            nonlocal first, last
            if node is None:
                return
            
            dfs(node.left)
            
            if first is None:
                first = node
            
            if last:
                node.left = last
                last.right = node
            
            last = node
            
            dfs(node.right)
            
        
        first, last = None, None
        dfs(root)
        first.left = last
        last.right = first
        
        return first