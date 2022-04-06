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

class AdditionNode(Node):
    def __init__(self, left, right):
        self.left, self.right = left, right
    def evaluate(self):
        return self.left.evaluate() + self.right.evaluate()
    
class SubtractionNode(Node):
    def __init__(self, left, right):
        self.left, self.right = left, right
    def evaluate(self):
        return self.left.evaluate() - self.right.evaluate()
    
class MultiplicationNode(Node):
    def __init__(self, left, right):
        self.left, self.right = left, right
    def evaluate(self):
        return self.left.evaluate() * self.right.evaluate()
    
class DivisionNode(Node):
    def __init__(self, left, right):
        self.left, self.right = left, right
    def evaluate(self):
        return self.left.evaluate() // self.right.evaluate()
    
class ValueNode(Node):
    def __init__(self, value):
        self.value = int(value)
    def evaluate(self):
        return self.value
"""    
This is the TreeBuilder class.
You can treat it as the driver code that takes the postinfix input
and returns the expression tree represnting it as a Node.
"""

class TreeBuilder(object):
    def buildTree(self, postfix: List[str]) -> 'Node':
        expression_stack = []
        for char in postfix:
            if char.isdigit():
                expression_stack.append(ValueNode(char))
            else:
                second = expression_stack.pop()
                first = expression_stack.pop()
                if char == '+':
                    new_node = AdditionNode(first, second)
                elif char == '-':
                    new_node = SubtractionNode(first, second)
                elif char == '/':
                    new_node = DivisionNode(first, second)
                else:
                    new_node = MultiplicationNode(first, second)
                expression_stack.append(new_node)
        
        return expression_stack[0]

		
"""
Your TreeBuilder object will be instantiated and called as such:
obj = TreeBuilder();
expTree = obj.buildTree(postfix);
ans = expTree.evaluate();
"""
        