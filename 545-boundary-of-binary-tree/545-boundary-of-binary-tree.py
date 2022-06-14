# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # root flag -> 0
    # left boundry flag -> 1
    # right boundry flag -> 2
    # middle node flag -> 3
    
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        def is_left_boundry(flag):
            return flag == 1
        def is_right_boundry(flag):
            return flag == 2
        def is_root(flag):
            return flag == 0
        def is_leaf(node):
            return node.left is None and node.right is None
        
        def left_child_flag(curr, flag):
            if is_root(flag) or is_left_boundry(flag):
                return 1
            elif is_right_boundry(flag) and curr.right is None:
                return 2
            return 3
        def right_child_flag(curr, flag):
            if is_root(flag) or is_right_boundry(flag):
                return 2
            elif is_left_boundry(flag) and curr.left is None:
                return 1
            return 3
        
        def preorder(node, flag = 0):
            nonlocal leftmost_nodes, rightmost_nodes, leaf_nodes
            
            if node is None:
                return
            
            if is_leaf(node):
                leaf_nodes.append(node.val)
                return
            
            if is_root(flag) or is_left_boundry(flag):
                leftmost_nodes.append(node.val)
            
            if is_right_boundry(flag):
                rightmost_nodes.append(node.val)
            
            preorder(node.left, left_child_flag(node, flag))
            preorder(node.right, right_child_flag(node, flag))
        leftmost_nodes, rightmost_nodes, leaf_nodes = [], [], []
        preorder(root)
        return leftmost_nodes + leaf_nodes + rightmost_nodes[::-1]
        