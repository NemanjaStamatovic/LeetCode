class Solution:
    def climbStairs(self, n: int) -> int:
        
        if n == 1:
            return 1
        
        first = 1
        second = 2
        
        for i in range(3, n+1):
            third = first + second
            first = second
            second = third
            
        return second    
        
#         def stairs(i, n):
#             if i > n:
#                 return 0
#             if i == n:
#                 return 1
#             return stairs(i+1, n) + stairs(i+2, n)
        
#         return stairs(0, n)