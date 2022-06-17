# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def find_common_ancestor(node):
            nonlocal common_ancestor
            if node is None or common_ancestor is not None:
                return False
            is_node_wanted = node == p or node == q
            is_left_child_wanted = find_common_ancestor(node.left)
            is_right_child_wanted = find_common_ancestor(node.right)
            
            is_common_ancestor_found = (is_node_wanted and (is_left_child_wanted or is_right_child_wanted)) or (is_left_child_wanted and is_right_child_wanted)
            
            if is_common_ancestor_found:
                common_ancestor = node
            
            return is_node_wanted or is_left_child_wanted or is_right_child_wanted
        common_ancestor = None
        find_common_ancestor(root)
        return common_ancestor
        