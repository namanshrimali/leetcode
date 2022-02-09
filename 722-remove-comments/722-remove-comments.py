class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        in_block, sol = False, []
        
        def skip_in_block(idx, line):
            block = True
            while idx<len(line):
                if (line[idx] == '/' and idx-1 > -1 and line[idx-1]=='*'):
                    block = False
                    break
                idx+=1
            return idx, block
        code_line = []
        for line in source:
            i = 0
            line.strip()
            while i < len(line):
                if in_block:
                    i, in_block = skip_in_block(i, line)
                elif line[i] == '/':
                    if i+1 < len(line) and line[i+1] == '/':     # start of inline comment
                        break
                    elif i+1 < len(line) and line[i+1] == '*':
                        in_block = True
                        i+=3
                        continue
                    else:
                        code_line.append(line[i])
                else:
                    code_line.append(line[i])
                
                i+=1
                
            if len(code_line)>0 and not in_block:
                sol.append(''.join(code_line))
                code_line = []
        return sol