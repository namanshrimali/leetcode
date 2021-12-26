"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def diameter(self, root: 'Node') -> int:
        """
        :type root: 'Node'
        :rtype: int
        """
        def dfs(node, height=0):
            nonlocal diameter
            if node.children:
                child_max_heights = []
                for children in node.children:
                    child_max_heights.append(dfs(children)+1)
                child_max_heights.sort()
                diameter = max(sum(child_max_heights[-2:]),diameter)
                return child_max_heights[-1]
            else:
                return height
        diameter = 0
        dfs(root)
        return diameter