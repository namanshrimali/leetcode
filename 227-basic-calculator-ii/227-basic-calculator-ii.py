class Solution:
    def calculate(self, s: str) -> int:
            
        stack, last_sign = [], '+'
        i, L = 0, len(s)
        
        def get_number(i, last_sign):
            num = [last_sign]
            while i < L and s[i] not in '+-*/':
                if s[i].isdigit():
                    num.append(s[i])
                i+=1
            return int(''.join(num)), i-1
        
        while i<L:
            if s[i].isdigit():
                next_num, i = get_number(i, last_sign)
                stack.append(next_num)
            else:
                if s[i] == '-':
                    last_sign = '-'
                elif s[i] == '+':
                    last_sign = '+'
                elif s[i] == '*':
                    last_sign = '+'
                    next_num, i = get_number(i+1, last_sign)
                    stack[-1]*=next_num
                elif s[i] == '/':
                    last_sign = '+'
                    next_num, i = get_number(i+1, last_sign)
                    if stack[-1] < 0:
                        stack[-1] = -(-stack[-1]//next_num)
                    else:
                        stack[-1]//=next_num
            i+=1
        return sum(stack)
            
                        
                    