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
        
        sol = ""
        for i in range(len(s)):
            if i in stack:
                continue
            sol+=s[i]
        return sol