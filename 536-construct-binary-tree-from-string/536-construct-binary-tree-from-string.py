# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def str2tree(self, s: str) -> Optional[TreeNode]:
        def construct_node():
            nonlocal curr_ptr
            curr_ptr+=1
            node, node_val = TreeNode(), []
            
            while(curr_ptr < len(s) and s[curr_ptr]!=')'):
                if s[curr_ptr] == '(':
                    child = construct_node()
                    if node.left:
                        node.right = child
                    else:
                        node.left = child
                else:
                    node_val.append(s[curr_ptr])
                curr_ptr+=1
            
            node.val = int(''.join(node_val))
            return node
        if s:
            curr_ptr = -1
            return construct_node()