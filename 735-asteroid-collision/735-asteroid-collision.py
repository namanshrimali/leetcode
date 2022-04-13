class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            if asteroid < 0:
                is_destroyed = False
                while stack and stack[-1] > 0:
                    top_asteroid = stack[-1]
                    if top_asteroid >= -asteroid:
                        if top_asteroid == -asteroid:
                            stack.pop()
                        is_destroyed = True
                        break    
                    else:
                        stack.pop()
                if not is_destroyed:
                    stack.append(asteroid)
            else:
                stack.append(asteroid)
        
        return stack            
        