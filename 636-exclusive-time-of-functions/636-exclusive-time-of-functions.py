class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        last_start, last_func = 0, None
        sol = [0]*n
        stack = []
        for log in logs:
            func, type_, time = log.split(":")
            func, time = int(func), int(time)
            if type_ == 'start':
                if stack:
                    sol[stack[-1]] += time-last_start
                stack.append(func)
                last_start = time
                
            else:
                sol[stack.pop()]+= time - last_start+1
                last_start = time + 1
        return sol
        