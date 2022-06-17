class Solution:
    def calculate(self, s: str) -> int:
        def get_next_number(idx):
            num = 0
            while idx < len(s) and s[idx] not in '+-*/':
                if s[idx].isdigit():
                    num = num * 10 + int(s[idx])
                idx += 1
            return num, idx - 1
        
        expression_stack = []
        last_sign = 1
        i = 0
        while i < len(s):
            if s[i] in '+-*/':
                if s[i] == '+':
                    last_sign = 1
                elif s[i] == '-':
                    last_sign = -1
                elif s[i] == '*':
                    next_num, i = get_next_number(i+1)
                    expression_stack[-1] *= last_sign * next_num
                    last_sign = 1
                else:
                    next_num, i = get_next_number(i+1)
                    if expression_stack[-1] < 0:
                        new_value = -((-expression_stack[-1])//next_num)
                    else:
                        new_value = expression_stack[-1]//next_num
                    expression_stack[-1] = new_value * last_sign
                    last_sign = 1
                    
            elif s[i].isdigit():
                next_num, i = get_next_number(i)
                expression_stack.append(next_num * last_sign)
                last_sign = 1
            i += 1
        return sum(expression_stack)
        