# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        
        def dfs(node):
            nonlocal sol
            if node is None:
                return
            if low <= node.val <= high:
                sol+=node.val
            
            if node.val > low:
                dfs(node.left)
            if node.val < high:
                dfs(node.right)
        sol = 0
        dfs(root)
        return sol