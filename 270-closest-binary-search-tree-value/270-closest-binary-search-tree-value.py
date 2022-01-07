# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        closest_val, closest_node = float('inf'), None
        node = root
        while(node):
            diff = abs(target-node.val)
            if diff < closest_val:
                closest_node = node
                closest_val = diff
            if target > node.val:
                node= node.right
            else:
                node = node.left
        return closest_node.val
        