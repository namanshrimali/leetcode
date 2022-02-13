class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split("/")
        dir_stack = []
        for s in path:
            if s == '' or s == '.':
                continue
            elif s == '..':
                if dir_stack:
                    dir_stack.pop()
            else:
                dir_stack.append(s)
        
        return '/'+'/'.join(dir_stack)
            
        