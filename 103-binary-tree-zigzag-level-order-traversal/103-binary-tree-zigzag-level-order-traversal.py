# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        answer = []
        deque = collections.deque([root])
        reverse = False
        while deque:
            que_len, local_ans = len(deque), []
            for _ in range(que_len):
                top_ele = deque.popleft()
                local_ans.append(top_ele.val)
                if top_ele.left:
                    deque.append(top_ele.left)
                if top_ele.right:
                    deque.append(top_ele.right)
            if reverse:
                local_ans = local_ans[::-1]
            answer.append(local_ans)
            reverse = not reverse
        return answer