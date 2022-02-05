# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def str2tree(self, s: str) -> Optional[TreeNode]:
        def construct_tree():
            nonlocal idx
            parent, value = None, []
            while idx < len(s) and s[idx]!=')':
                if s[idx]=='(':
                    idx+=1
                    child = construct_tree()
                    if parent.left:
                        parent.right = child
                    else:
                        parent.left = child
                else:
                    value.append(s[idx])
                if idx+1 == len(s) or  s[idx+1] in '()':
                    if parent is None:
                        parent = TreeNode(val=int(''.join(value)))
                idx+=1
                
            return parent
        idx = 0
        return construct_tree()
                
                    