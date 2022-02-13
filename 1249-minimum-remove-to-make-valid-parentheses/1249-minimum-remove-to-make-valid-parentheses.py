class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        s = list(s)
        invalid_stack = []
        for i in range(len(s)):
            if s[i] == '(':
                invalid_stack.append(i)
            elif s[i] == ')':
                if invalid_stack and s[invalid_stack[-1]] == '(':
                    invalid_stack.pop()
                else:
                    invalid_stack.append(i)
        for idx in invalid_stack:
            s[idx] = ''
        return ''.join(s)
        