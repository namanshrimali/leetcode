# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, max_so_far = float('-inf')):
            nonlocal sol
            if node is None:
                return
            if max_so_far <= node.val:
                sol+=1
                max_so_far = node.val
            
            dfs(node.left, max_so_far)
            dfs(node.right, max_so_far)

            
        sol = 0
        dfs(root)
        return sol