# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            nonlocal min_shift
            if node is None:
                return 0
            extra_coins = node.val + dfs(node.left) + dfs(node.right) - 1
            min_shift += abs(extra_coins)
            return extra_coins
        min_shift = 0
        dfs(root)
        return min_shift