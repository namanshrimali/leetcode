# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def pre_order(node):
            nonlocal prev
            if node is None:
                return
            prev, right_node = node, node.right
            
            pre_order(node.left)
            node.right = node.left
            prev.right = right_node
            node.left = None

            pre_order(right_node)
        prev = None
        pre_order(root)
        return prev