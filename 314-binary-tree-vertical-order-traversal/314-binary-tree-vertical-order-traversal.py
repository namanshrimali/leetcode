# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return
        level_dict = {}
        deque = collections.deque([(root, 0)])
        while deque:
            node, level = deque.popleft()
            if level in level_dict:
                level_dict[level].append(node)
            else:
                level_dict[level] = [node]
            if node.left:
                deque.append((node.left, level-1))
            if node.right:
                deque.append((node.right, level+1))
        sol = []
        for level in sorted(level_dict):
            level_list = []
            for node in (level_dict[level]):
                level_list.append(node.val)
            sol.append(level_list)
        return sol