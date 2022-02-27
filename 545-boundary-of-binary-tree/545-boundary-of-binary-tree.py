# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        left_boundry, right_boundry, leaf = [root.val], [], []
        
        def is_leaf(node):
            return node and node.left == None and node.right == None and node != root
        
        def fill_left_boundry(node):
            while node:
                if is_leaf(node):
                    break
                left_boundry.append(node.val)
                if node.left:
                    node = node.left
                else:
                    node = node.right
        
        def fill_right_boundry(node):
            while node:
                if is_leaf(node):
                    break
                right_boundry.append(node.val)
                if node.right:
                    node = node.right
                else:
                    node = node.left
        
        def fill_leaf(node):
            if node is None:
                return
            if is_leaf(node):
                leaf.append(node.val)
            fill_leaf(node.left)
            fill_leaf(node.right)
                
        
        if root.left:
            fill_left_boundry(root.left)
        if root.right:
            fill_right_boundry(root.right)
        fill_leaf(root)
        return left_boundry + leaf + right_boundry[::-1]
        
        