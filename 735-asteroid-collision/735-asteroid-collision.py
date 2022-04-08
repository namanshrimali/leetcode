class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            if a > 0:
                stack.append(a)
            else:
                destroy_self = False
                while stack and stack[-1] > 0:
                    top_a = stack[-1]
                    if top_a >= -a:
                        destroy_self = True
                        if top_a == -a:
                            stack.pop()
                        break
                    else:
                        stack.pop()
                    
                if not destroy_self:
                    stack.append(a)
        return stack