class Solution:
    def isValid(self, s: str) -> bool:
        char_stack = []
        char_complement = {
            '(' : ')',
            '{' : '}',
            '[' : ']'
        }
        
        for char in s:
            if char_stack and char_complement.get(char_stack[-1], '') == char:
                char_stack.pop()
            else:
                char_stack.append(char)
        return len(char_stack) == 0