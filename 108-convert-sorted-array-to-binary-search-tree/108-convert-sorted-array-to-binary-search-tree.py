# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 0:
            return None
        
        def create_bst(start, end):
            if start > end:
                return None
            mid = (start + end)//2
            curr_node = TreeNode(nums[mid])
            curr_node.left = create_bst(start, mid-1)
            curr_node.right = create_bst(mid+1, end)
            return curr_node
        
        return create_bst(0, len(nums)-1)
        