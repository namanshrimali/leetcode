# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return
        sol = []
        deque = collections.deque([root])
        direction = 1
        while deque:
            lev_sol = []
            deque_len = len(deque)
            for _ in range(deque_len):
                ele = deque.popleft()
                if ele.left:
                    deque.append(ele.left)
                if ele.right:
                    deque.append(ele.right)
                lev_sol.append(ele.val)
            if direction == -1:
                lev_sol = lev_sol[::-1]
            sol.append(lev_sol)
            direction*=-1
        return sol