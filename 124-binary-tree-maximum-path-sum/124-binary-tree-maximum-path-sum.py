# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def post_order_max_path(node):
            nonlocal global_max_path
            if node is None:
                return 0
            max_path_from_left = max(post_order_max_path(node.left), 0)
            max_path_from_right = max(post_order_max_path(node.right), 0)
            curr_node_max_path = node.val + max(max_path_from_left, max_path_from_right)
            curr_node_optimal_path = node.val + max_path_from_left + max_path_from_right
            global_max_path =  max(global_max_path,  curr_node_optimal_path)
            return curr_node_max_path
        
        global_max_path = float('-inf')
        post_order_max_path(root)
        return global_max_path
        