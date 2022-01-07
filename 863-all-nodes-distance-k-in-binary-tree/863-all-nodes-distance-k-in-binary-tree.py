# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        def dfs(node, parent=None):
            if node is None:
                return
            node.parent = parent
            dfs(node.left, node)
            dfs(node.right, node)
        dfs(root)
        
        visited = set([target])
        queue = collections.deque([target])
        curr_level = 0
        while queue:
            curr_queue_len = len(queue)
            if curr_level == k:
                return [node.val for node in queue]
            while curr_queue_len:
                top_ele = queue.popleft()
                visited.add(top_ele)
                
                for connected_ele in [top_ele.parent, top_ele.right, top_ele.left]:
                    if connected_ele and connected_ele not in visited:
                        queue.append(connected_ele)
                curr_queue_len-=1
            curr_level+=1
        return []
            