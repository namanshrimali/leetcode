# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        # dfs
        # zig -> left
        # zag -> right
        # zig for a node -> select left node's right subtree's height
        # zag for a node -> select right node's left subtree's height
        
        def dfs(node) -> int:
            nonlocal max_height
            if node is None:
                return -1, -1
            left_zig, left_zag = dfs(node.left)
            right_zig, right_zag = dfs(node.right)
            
            node_zig = 1 + left_zag
            node_zag = 1 + right_zig
            max_zig_zag = max(node_zig, node_zag)
            max_height = max(max_height, max_zig_zag)
            
            return node_zig, node_zag
            
        max_height = 0
        dfs(root)
        return max_height