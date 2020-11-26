class Solution:
    def reverse(self, x: int) -> int: 
        if x > 0:
            sign = 1
        elif x < 0:
            sign = -1
            x = -x
        else:
            return 0
        
        result = 0
        while x:
            result = result*10 + x%10
            x = x//10
            
        if result > 2**31 - 1 or result < -2**31:
            return 0
        
        return result*sign   
    
#         if x > 0:
#             x = str(x)
#             x = x[::-1]
#             x = int(x)
#         elif x < 0:
#             x = 0 - x
#             x = str(x)
#             x = x[::-1]
#             x = int(x)
#             x = 0 - x
#         else:
#             x = 0
        
#         if x > 2**31 - 1 or x < -2**31:
#             return 0
        
#         return x    

        