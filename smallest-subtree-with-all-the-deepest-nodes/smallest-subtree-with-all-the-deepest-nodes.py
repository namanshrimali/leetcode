# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        def dfs(node, parent = None, level=0):
            nonlocal max_depth, first, last
            if node is None:
                return
            node.parent = parent
            if level > max_depth:
                max_depth = level
                first = node
            if level == max_depth:
                last = node
            dfs(node.left, node, level+1)
            dfs(node.right, node, level+1)
        
        max_depth, first, last = -float('inf'), None, None
        dfs(root)
        visited = set()
        while(first):
            visited.add(first)
            first = first.parent
        while(last):
            if last in visited:
                return last
            last = last.parent
            
        
