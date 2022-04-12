# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:
        def dfs(node):
            nonlocal max_avg
            if node is None:
                return 0, 0
            total_subtree_size, subtree_total = 0, 0
            
            left_subtree_size, left_total = dfs(node.left)
            right_subtree_size, right_total = dfs(node.right)
            
            total_subtree_size = left_subtree_size + right_subtree_size + 1
            total_subtree_val = left_total + right_total + node.val
            
            max_avg = max(max_avg, total_subtree_val/total_subtree_size)
            
            return total_subtree_size, total_subtree_val
        max_avg = 0
        dfs(root)
        return max_avg
        