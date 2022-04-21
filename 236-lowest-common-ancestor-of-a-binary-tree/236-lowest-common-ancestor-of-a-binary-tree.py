# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def map_parent(node, parent = None):
            if node is None:
                return
            node.parent = parent
            map_parent(node.left, node)
            map_parent(node.right, node)
        
        map_parent(root)
        p_ancestors = set()
        while p:
            p_ancestors.add(p)
            p = p.parent
        while q:
            if q in p_ancestors:
                break
            q = q.parent
        return q