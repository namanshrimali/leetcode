# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        left, leaf, right = [], [], []
        def pre_dfs(node, flag):
            if node is None:
                return
            if flag == 'root':
                left.append(node.val)
                pre_dfs(node.left, 'left')
                pre_dfs(node.right, 'right')
                
            elif flag == 'left':
                left.append(node.val)
                if node.left:
                    pre_dfs(node.left, 'left')
                    pre_dfs(node.right, 'mid')
                else:
                    pre_dfs(node.right, 'left')
            
            elif flag == 'right':
                right.append(node.val)
                if node.right:
                    pre_dfs(node.left, 'mid')
                    pre_dfs(node.right, 'right')
                else:
                    pre_dfs(node.left, 'right')
            else: # flag == 'mid'
                if node.left == None and node.right == None:
                    leaf.append(node.val)
                else:
                    pre_dfs(node.left, 'mid')
                    pre_dfs(node.right, 'mid')
                    
        pre_dfs(root, 'root')
        return left + leaf + right[::-1]
                