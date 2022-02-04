"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def inorderSuccessor(self, node: 'Node') -> 'Optional[Node]':
        # when node is left leaf -> parent node
        # when node is right leaf -> leftmost child of grand parent's right child else None
        # when node is parent with right child -> leftmost of right child
        # when node has no right child -> leftmost child of parent's right node
        def get_leftmost(node):
            if node is None:
                return
            while node.left:
                node = node.left
            return node
        def get_next_largest(node):
            prev, parent = node, node.parent
            while parent and parent.right == prev:
                prev = parent
                parent = parent.parent
            return parent
            
        
        if node.right:
            return get_leftmost(node.right)
        else:
            if node.parent:
                return get_next_largest(node)
        return None
        