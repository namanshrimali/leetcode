class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        str_pair = {
            '1': '1',
            '6': '9',
            '8': '8',
            '9': '6',
            '0': '0'
        }
        sol_num = []
        for i in num:
            if i not in str_pair:
                return False
            sol_num.append(str_pair[i])
        if ''.join(sol_num[::-1]) == num:
            return True
        return False