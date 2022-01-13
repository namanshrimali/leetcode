# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        sol = []
        to_delete = set(to_delete)
        
        def traverse_and_delete(node, parent = None):
            nonlocal sol
            if node is None:
                return
            left, right = traverse_and_delete(node.left), traverse_and_delete(node.right)
            if left:
                node.left = None
            if right:
                node.right = None
            if node.val in to_delete:
                if node.left:
                    sol.append(node.left)
                if node.right:
                    sol.append(node.right)
                return True
            return False
            
        if not traverse_and_delete(root):
            sol.append(root)
            
        return sol
        