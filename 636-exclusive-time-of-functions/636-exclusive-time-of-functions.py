class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        sol = [0]*n
        stack, prev_time = [], 0
        for log in logs:
            func, process, time = log.split(":")
            func, time = int(func), int(time)
            
            if process == 'start':
                if stack:
                    sol[stack[-1]]+=time-prev_time
                stack.append(func)
                prev_time = time
                    
            else:
                sol[stack.pop()]+= time-prev_time+1
                prev_time = time+1
        return sol