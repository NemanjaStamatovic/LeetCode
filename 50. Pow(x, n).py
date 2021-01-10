class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        res = 1
        
        if n > 0:
            sign = 1
        else:
            sign = -1
            n = -n
        
        for i in range(n):
            res *= x
            
        if sign == -1:
            res = 1/res
            
        return res    