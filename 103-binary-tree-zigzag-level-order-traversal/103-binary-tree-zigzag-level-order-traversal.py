# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        deque = collections.deque([root])
        reverse = False
        zig_zag = []
        while deque:
            level_nodes = []
            deque_len = len(deque)
            for _ in range(deque_len):
                root = deque.popleft()
                level_nodes.append(root.val)
                if root.left:
                    deque.append(root.left)
                if root.right:
                    deque.append(root.right)
            if reverse:
                level_nodes = level_nodes[::-1]
            zig_zag.append(level_nodes)
            reverse = not reverse
        return zig_zag