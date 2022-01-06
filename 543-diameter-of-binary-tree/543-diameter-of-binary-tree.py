# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            nonlocal diameter
            if node is None:
                return 0
            left_height = dfs(node.left)
            right_height = dfs(node.right)
            diameter = max(diameter, left_height+right_height)
            
            return max(left_height, right_height)+1
            
        diameter = 0
        dfs(root)
        return diameter