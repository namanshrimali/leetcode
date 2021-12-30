# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        depth_map = {}
        def dfs(node, parent = None, level=0):
            nonlocal max_depth
            if node is None:
                return
            depth_map[node] = level
            if level > max_depth:
                max_depth = level
            
            dfs(node.left, node, level+1)
            dfs(node.right, node, level+1)
        def find_subtree(node):
            if node is None or depth_map[node] == max_depth:
                return node
            
            left = find_subtree(node.left)
            right = find_subtree(node.right)
            
            if left and right:
                return node
            if left:
                return left
            if right:
                return right
            return None
                
        max_depth = -float('inf')
        dfs(root)
        return find_subtree(root)
        