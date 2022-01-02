# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    BOTH_DONE = 0
    LEFT_DONE = 1
    BOTH_PENDING = 2
    parent_idx = -1
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        one_found = False
        
        stack = [[root, Solution.BOTH_PENDING]]
        
        while(stack):
            node, state = stack[-1]
            # if both done on stack top element, pop it out
            if state == Solution.BOTH_DONE:
                if one_found and parent_idx == len(stack)-1:
                    parent_idx -=1
                stack.pop()
            else:
                if state == Solution.BOTH_PENDING:   # elif if both are pending
                    if node == p or node == q:
                        if one_found:
                            return stack[parent_idx][0]
                        else:
                            one_found = True
                            parent_idx = len(stack)-1
                            
                    child_node = node.left
                else:   # else if left is done
                    child_node = node.right
                stack[-1][1]-=1
                if child_node:
                    stack.append([child_node, Solution.BOTH_PENDING])
                
                