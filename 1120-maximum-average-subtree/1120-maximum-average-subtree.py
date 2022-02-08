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
            left_sum, left_subtree_len = dfs(node.left)
            right_sum, right_subtree_len = dfs(node.right)
            total_subtree_len = 1 + left_subtree_len + right_subtree_len
            total_subtree_sum = left_sum + right_sum + node.val
            
            max_avg = max(max_avg, total_subtree_sum/total_subtree_len)
            
            return total_subtree_sum, total_subtree_len
        
        max_avg = -inf
        dfs(root)
        return max_avg