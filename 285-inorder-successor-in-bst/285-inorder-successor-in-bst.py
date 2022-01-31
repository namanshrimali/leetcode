# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'Optional[TreeNode]':
        def dfs(node):
            nonlocal prev, succ
            if node is None or succ:
                return
            dfs(node.left)
            if prev == p:
                succ = node
            prev = node
            dfs(node.right)
        prev, succ = None, None
        dfs(root)
        return succ