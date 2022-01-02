class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open_paranthesis, close_paranthesis = 0, 0
        for word in s:
            if word == '(':
                close_paranthesis += 1
            elif word == ')':
                close_paranthesis -=1

            if close_paranthesis == -1:
                open_paranthesis += 1
                close_paranthesis = 0
        return open_paranthesis + close_paranthesis