class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # + -> + : None
        # + -> - : Collision
        # - -> + : None
        # - -> - : None
        
        stack = []
        for asteroid in asteroids:
            if asteroid < 0:
                # when big negative asteroid is coming
                while stack and stack[-1] > 0 and abs(stack[-1]) < abs(asteroid):
                    stack.pop()
                if stack and stack[-1]>0:
                    if stack[-1] == -asteroid:
                        stack.pop()
                    continue
            stack.append(asteroid)
        return stack
        