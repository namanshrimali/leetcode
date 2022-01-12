class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        str_pair = {
            '1': '1',
            '6': '9',
            '8': '8',
            '9': '6',
            '0': '0'
        }
        first, last = 0, len(num)-1
        while(first<=last):
            if num[last] not in str_pair or num[first] != str_pair[num[last]]:
                return False
            first+=1
            last-=1
        return True