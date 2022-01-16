# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        max_level, level_count, max_level_sum = -1, 1, -float('inf')
        queue = collections.deque([root])
        while(queue):
            queue_len = len(queue)
            level_sum = 0
            for _ in range(queue_len):
                top_node = queue.popleft()
                level_sum+= top_node.val
                if top_node.left:
                    queue.append(top_node.left)
                if top_node.right:
                    queue.append(top_node.right)
            if level_sum > max_level_sum:
                max_level_sum = level_sum
                max_level = level_count
            level_count+=1
        return max_level
        