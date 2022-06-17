class Solution:
    def intToRoman(self, num: int) -> str:
        int_roman_dict = {
            1 : 'I',
            4 : 'IV',
            5 : 'V',
            9 : 'IX',
            10: 'X',
            40: 'XL',
            50: 'L',
            90: 'XC',
            100: 'C',
            400: 'CD',
            500: 'D',
            900: 'CM',
            1000:'M'
        }
        dividends = list(sorted(int_roman_dict.keys(), reverse = True))
        i = 0
        roman_rep = []
        while num and i < len(dividends):
            roman_rep.append((num//dividends[i]) * int_roman_dict[dividends[i]])
            num = num % dividends[i] 
            i += 1
        return ''.join(roman_rep)