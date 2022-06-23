# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def can_prune(node):
            return node.val == 0 and (not node.left) and not(node.right)
        
        def dfs(node):
            if node is None:
                return False
            if node.left and dfs(node.left):
                node.left = None
            if node.right and dfs(node.right):
                node.right = None
            return can_prune(node)
        
        if not root:
            return root
        
        if dfs(root):
            return None
        return root
