class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        if n == 0:
            return 1
        
        if n < 0:
            return self.myPow(1/x, -n)
        
        half = self.myPow(x, n//2)
        
        if n % 2 == 1:
            return half * half * x
        
        return half * half
        
#         res = 1
        
#         if n > 0:
#             sign = 1
#         else:
#             sign = -1
#             n = -n
        
#         for i in range(n):
#             res *= x
            
#         if sign == -1:
#             res = 1/res
            
#         return res    