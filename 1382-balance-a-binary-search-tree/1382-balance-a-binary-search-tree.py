# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        in_order_list = []
        
        def dfs(node):
            if node is None:
                return
            dfs(node.left)
            in_order_list.append(node)
            dfs(node.right)
        
        def balance_tree(low, high):
            if low > high:
                return
            mid = (low+high)//2
            mid_node = in_order_list[mid]
            
            mid_node.left = balance_tree(low, mid-1)
            mid_node.right = balance_tree(mid+1, high)
            return mid_node
            
        dfs(root)
        return balance_tree(0, len(in_order_list)-1)