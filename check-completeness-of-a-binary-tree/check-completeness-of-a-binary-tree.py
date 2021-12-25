# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        queue = collections.deque([root])
        while(queue):
            node = queue.popleft()
            if node is None:
                break
            queue.append(node.left)
            queue.append(node.right)
        return True if len([a for a in queue if a is not None])==0 else False 
        