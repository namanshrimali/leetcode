class Node:
    def __init__(self, val=None):
        self.val = val
        self.prev, self.next = None, None
        self.count = 1

class LinkedList:
    def __init__(self):
        self.head, self.tail = Node(), Node()
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def add(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
    
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def is_empty(self):
        return self.head.next == self.tail
    
    def first_unique_node(self):
        if self.is_empty():
            return None
        return self.tail.prev
        
class FirstUnique:
    def __init__(self, nums: List[int]):
        self.node_map = {}
        self.ll = LinkedList()
        for num in nums:
            if num in self.node_map:
                self.node_map[num].count += 1
            else:
                self.node_map[num] = Node(num)
        for node in self.node_map:
            if self.node_map[node].count == 1:
                self.ll.add(self.node_map[node])

    def showFirstUnique(self) -> int:
        unique_node = self.ll.first_unique_node()
        if unique_node == None:
            return -1
        return unique_node.val

    def add(self, value: int) -> None:
        if value in self.node_map:
            if self.node_map[value].count == 1:
                self.ll.remove(self.node_map[value])
        else:
            self.node_map[value] = Node(value)
            self.ll.add(self.node_map[value])
        


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)