class Node:
    def __init__(self, key=None, val=None, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head, self.tail = Node(), Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.lru = {}
        
    def add_to_top(self, node):
        node.next = self.head.next
        node.next.prev = node
        node.prev = self.head
        self.head.next = node
    
    def remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        return node
        
    def get(self, key: int) -> int:
        if key in self.lru:
            node = self.lru[key]
            self.add_to_top(self.remove_node(node))
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.lru:
            node = self.lru[key]
            node.val = value
            self.add_to_top(self.remove_node(node))
        else:
            node = Node(key, value)
            self.lru[key] = node
            self.add_to_top(node)
            if len(self.lru)>self.capacity:
                del_node = self.remove_node(self.tail.prev)
                del self.lru[del_node.key]
                
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)