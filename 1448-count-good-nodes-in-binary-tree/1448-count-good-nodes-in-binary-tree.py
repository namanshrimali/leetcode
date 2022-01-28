# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, parent_list=[]):
            nonlocal sol
            if node is None:
                return
            parent_list.append(node.val)
            dfs(node.left, parent_list)
            dfs(node.right, parent_list)
            parent_list.pop()
            
            for parent in parent_list:
                if node.val < parent:
                    return
            sol+=1
            
        sol = 0
        dfs(root)
        return sol