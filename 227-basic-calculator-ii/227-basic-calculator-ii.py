class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(" ", "")
        stack = []
        last_digit_start_idx = -1
        last_symbol = "+"
        idx = 0
        while idx < len(s):
            char = s[idx]
            if char in "+-*/":
                if last_digit_start_idx != -1:
                    stack.append(int(last_symbol+s[last_digit_start_idx:idx]))
                if char in "+-":
                    last_symbol = char
                else:
                    last_number = stack.pop()
                    last_digit_start_idx = idx+1
                    while(idx+1 < len(s) and s[idx+1].isdigit()):
                        idx+=1
                    curr_number = int(s[last_digit_start_idx:idx+1])
                    if char == '*':
                        stack.append(last_number*curr_number)
                    else:
                        if last_number < 0:
                            stack.append(-(abs(last_number)//curr_number))
                        else:
                            stack.append(last_number//curr_number)
                last_digit_start_idx = -1
            else:
                if last_digit_start_idx == -1:
                    last_digit_start_idx = idx
                
            idx+=1
        if last_digit_start_idx != -1:
            stack.append(int(last_symbol+s[last_digit_start_idx:]))
        
        return sum(stack)
                
                
        