# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        def map_parent(node, parent=None):
            if node is None:
                return
            node.parent = parent
            map_parent(node.left, node)
            map_parent(node.right, node)
        
        def find_k_dist_nodes(node, distance = 0):
            nonlocal k_distance_nodes, visited
            
            if node is None or node in visited:
                return
            visited.add(node)
            if distance == k:
                k_distance_nodes.append(node.val)
                return
            find_k_dist_nodes(node.left, distance+1)
            find_k_dist_nodes(node.right, distance+1)
            find_k_dist_nodes(node.parent, distance+1)
            
            
            
        map_parent(root)
        k_distance_nodes, visited = [], set()
        find_k_dist_nodes(target)
        return k_distance_nodes
        