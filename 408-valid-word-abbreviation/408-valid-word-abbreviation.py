class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        idx, abbr_idx = 0, 0
        L, L_ABBR = len(word), len(abbr)
        while(idx<L and abbr_idx<L_ABBR):
            if word[idx]!=abbr[abbr_idx]:
                if abbr[abbr_idx].isdigit():
                    digit = int(abbr[abbr_idx])
                    if digit == 0:
                        return False
                    while(abbr_idx+1 < L_ABBR and abbr[abbr_idx+1].isdigit()):
                        abbr_idx+=1
                        digit = digit*10+int(abbr[abbr_idx])
                    if idx+digit-1 >= L:
                        return False
                    idx+=digit-1
                else:
                    return False
            idx+=1
            abbr_idx+=1
        return True if abbr_idx == L_ABBR and idx==L else False
            