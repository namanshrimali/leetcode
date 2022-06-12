# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        
        def annotate_parent(node, parent = None):
            if not node:
                return
            node.parent = parent
            annotate_parent(node.left, node)
            annotate_parent(node.right, node)
        
        def find_k_distance_nodes(node, k):
            considered_nodes = set([node])
            deque = collections.deque([target])
            while k:
                level_len = len(deque)
                for _ in range(level_len):
                    curr_node = deque.popleft()
                    parent, left, right = curr_node.parent, curr_node.left, curr_node.right
                    
                    if parent and parent not in considered_nodes:
                        deque.append(parent)
                        considered_nodes.add(parent)
                    if left and left not in considered_nodes:
                        deque.append(left)
                        considered_nodes.add(left)
                    if right and right not in considered_nodes:
                        deque.append(right)
                        considered_nodes.add(right)
                k -= 1
            return [node.val for node in deque]
        
        annotate_parent(root)
        return find_k_distance_nodes(target, k)
        
        