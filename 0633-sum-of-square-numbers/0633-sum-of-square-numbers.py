class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        l = 0
        r = c
        x = int(sqrt(c))
        if x**2 ==c:
            return True
        while l <= r:
            if l**2 + r**2 == c:
                return True
            elif l**2 + r**2 >c:
                r-=1
            else:
                l+=1
        return False
        