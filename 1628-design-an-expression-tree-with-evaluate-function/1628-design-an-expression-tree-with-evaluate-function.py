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

class BinaryNode(Node):
    def __init__(self, left=None, right=None, val = None):
        self.val = val
        self.right, self.left = right, left
    def evaluate(self) -> int:
        pass

class Plus(BinaryNode):
    def evaluate(self) -> int:
        return self.left.evaluate() + self.right.evaluate()
    
class Minus(BinaryNode):
    def evaluate(self) -> int:
        return self.left.evaluate() - self.right.evaluate()

class Divide(BinaryNode):
    def evaluate(self) -> int:
        return self.left.evaluate() // self.right.evaluate()

class Multiply(BinaryNode):
    def evaluate(self) -> int:
        return self.left.evaluate() * self.right.evaluate()

class Num(BinaryNode):
    def evaluate(self) -> int:
        return self.val 

"""    
This is the TreeBuilder class.
You can treat it as the driver code that takes the postinfix input
and returns the expression tree represnting it as a Node.
"""

class TreeBuilder(object):
    operators = {'+': Plus, '-': Minus, '*': Multiply, '/': Divide}
    def buildTree(self, postfix: List[str]) -> 'Node':
        stack = []
        for ele in postfix:
            if ele in self.operators:
                right, left = stack.pop(), stack.pop()
                stack.append(self.operators[ele](left, right, None))
            else:
                stack.append(Num(None, None, int(ele)))
        return stack[-1]
                
                 
"""
Your TreeBuilder object will be instantiated and called as such:
obj = TreeBuilder();
expTree = obj.buildTree(postfix);
ans = expTree.evaluate();
"""
        