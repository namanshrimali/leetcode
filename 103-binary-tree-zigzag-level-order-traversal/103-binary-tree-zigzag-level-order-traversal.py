# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return root
        
        reverse = False
        deque = collections.deque([root])
        zigzag_order = []
        while deque:
            deque_len = len(deque)
            level_nodes = []
            for _ in range(deque_len):
                curr_node = deque.popleft()
                level_nodes.append(curr_node.val)
                if curr_node.left:
                    deque.append(curr_node.left)
                if curr_node.right:
                    deque.append(curr_node.right)
            if reverse:
                level_nodes = level_nodes[::-1]
            zigzag_order.append(level_nodes)                     
            
            reverse = not reverse
        return zigzag_order