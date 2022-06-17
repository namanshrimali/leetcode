# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:
        max_avg = 0
        def subtree_average_calculator(node):
            nonlocal max_avg
            if node is None:
                return 0, 0
            left_subtree_len, left_subtree_total = subtree_average_calculator(node.left)
            right_subtree_len, right_subtree_total = subtree_average_calculator(node.right)
            
            curr_tree_total = left_subtree_total + right_subtree_total + node.val
            curr_tree_len = left_subtree_len + right_subtree_len + 1
            max_avg = max(max_avg, curr_tree_total/curr_tree_len)
            return curr_tree_len, curr_tree_total
        subtree_average_calculator(root)
        return max_avg
        