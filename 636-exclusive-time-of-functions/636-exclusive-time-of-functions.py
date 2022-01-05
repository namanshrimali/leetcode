class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        sol = [0]*n
        execution_stack = []
        for log in logs:
            func, phase, time = log.split(":")
            func, time = int(func), int(time)
            if phase == 'start':
                if execution_stack:
                    prev_func, prev_time = execution_stack[-1]
                    sol[prev_func]+=time - prev_time
                execution_stack.append([func, time])
                
            else:
                _, prev_time = execution_stack.pop()
                sol[func]+= time - prev_time + 1
                if execution_stack:
                    execution_stack[-1][1]= time+1
        return sol
                    