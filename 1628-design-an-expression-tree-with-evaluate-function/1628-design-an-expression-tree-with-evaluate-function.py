import abc 
from abc import ABC, abstractmethod 
"""
This is the interface for the expression tree Node.
You should not remove it, and you can define some classes to implement it.
"""

class Node(ABC):    
    @abstractmethod
    # define your fields here
    def evaluate(self) -> int:
        pass
class NumericNode(Node):
    def __init__(self, val):
        self.val = val
    def evaluate(self) -> int:
        return self.val
    
class BinaryNode(Node):
    def __init__(self, left, right):
        self.left, self.right = left, right

class Addition(BinaryNode):
    def evaluate(self) -> int:
        return self.left.evaluate() + self.right.evaluate()
    
class Subtraction(BinaryNode):
    def evaluate(self) -> int:
        return self.left.evaluate() - self.right.evaluate()

class Multiplication(BinaryNode):
    def evaluate(self) -> int:
        return self.left.evaluate() * self.right.evaluate()

class Division(BinaryNode):
    def evaluate(self) -> int:
        return self.left.evaluate() // self.right.evaluate()


"""    
This is the TreeBuilder class.
You can treat it as the driver code that takes the postinfix input
and returns the expression tree represnting it as a Node.
"""

class TreeBuilder(object):
    def buildTree(self, postfix: List[str]) -> 'Node':
        
        def get_node_from_char(char, left, right):
            if char == '+':
                node = Addition(left, right)
            elif char == '-':
                node = Subtraction(left, right)
            elif char == '*':
                node = Multiplication(left, right)
            else:
                node = Division(left, right)
            return node
        
        char_stack = []
        for char in postfix:
            if char.isdigit():
                char_stack.append(NumericNode(int(char)))
            else:
                right = char_stack.pop()
                left = char_stack.pop()
                curr_node = get_node_from_char(char, left, right)
                char_stack.append(curr_node)
            # print(char, char_stack)
        return char_stack[0]
                    
                
		
"""
Your TreeBuilder object will be instantiated and called as such:
obj = TreeBuilder();
expTree = obj.buildTree(postfix);
ans = expTree.evaluate();
"""
        