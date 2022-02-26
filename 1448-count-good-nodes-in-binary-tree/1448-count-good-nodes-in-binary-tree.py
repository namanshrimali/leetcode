# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, max_val=-inf):
            nonlocal count
            if node is None:
                return max_val
            if not (node.val < max_val):
                max_val = node.val
                count+=1
            max_from_child = max(dfs(node.left, max_val), dfs(node.right, max_val))
            return max(max_val, max_from_child)
        count = 0
        dfs(root)
        return count
        