class Solution:
    def intToRoman(self, num: int) -> str:
        roman = []
        values = [1000, 500, 100, 50, 10, 5, 1]
        symbol_mapping = {1000: 'M', 500: 'D', 100: 'C', 50: 'L', 10: 'X', 5: 'V', 1: 'I'}
        special_mapping = {
            'M': 100,
            'D': 100,
            'C': 10,
            'L': 10,
            'V': 1,
            'X': 1
        }
            
            
        value_idx = 0
        while num:
            curr_value = values[value_idx]
            curr_symbol = symbol_mapping[curr_value]
            roman.append((num//curr_value)*curr_symbol)
            num = num%values[value_idx]
            
            if curr_symbol in special_mapping:
            
                one_lower = curr_value - special_mapping[curr_symbol]

                if num // one_lower > 0:
                    num = num % one_lower
                    lower_symbol = symbol_mapping[special_mapping[curr_symbol]]
                    roman.append(lower_symbol + curr_symbol)

            value_idx +=1
        return ''.join(roman)
