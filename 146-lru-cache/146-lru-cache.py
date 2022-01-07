class Node:
    def __init__(self, key, val, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next
        
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.node_map = {}
        self.head = Node(None, None)
        self.tail = Node(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def delete_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def add_node(self, node):
        node.next = self.tail
        self.tail.prev.next = node
        node.prev = self.tail.prev
        self.tail.prev = node
        
        
    def move_to_tail(self, node):
        self.delete_node(node)
        self.add_node(node)
        
        
    def get(self, key: int) -> int:
        node = self.node_map.get(key, None)
        if node:
            self.move_to_tail(node)
            return node.val
        return -1
        

    def put(self, key: int, value: int) -> None:
        node = self.node_map.get(key)
        if node is None:
            node = Node(key, value)
            self.node_map[key] = node
            self.add_node(node)

            if len(self.node_map)>self.capacity:
                del self.node_map[self.head.next.key]
                self.delete_node(self.head.next)
        else:
            node.val = value
            self.move_to_tail(node)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)