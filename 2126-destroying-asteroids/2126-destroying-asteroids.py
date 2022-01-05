class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort()    # sorting the asteroids array -> O(nlogn)
        i=0
        while(i<len(asteroids)):                   #-> O(n)
            if mass >= asteroids[i]:
                mass+=asteroids[i]
            else:
                break
            i+=1
        return True if i == len(asteroids) else False
