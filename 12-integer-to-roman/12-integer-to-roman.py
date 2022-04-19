class Solution:
    def intToRoman(self, num: int) -> str:
        roman = []
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        symbols = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        value_idx = 0
        while num:
            roman.append((num//values[value_idx])*symbols[value_idx])
            num = num%values[value_idx]
            value_idx +=1
        return ''.join(roman)
