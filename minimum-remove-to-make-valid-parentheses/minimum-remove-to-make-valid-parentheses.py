class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            elif s[i] == ')':
                if stack and s[stack[-1]] == "(":
                    stack.pop()
                else:
                    stack.append(i)
        
        sol = list(s)
        for i in stack:
            sol[i]=""
        return ''.join(sol)