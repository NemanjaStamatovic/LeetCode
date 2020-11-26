class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        if x%10 == 0 and x != 0:
            return False
        
        reverse_number = 0
        
        while x > reverse_number:
            reverse_number = reverse_number*10 + x%10
            x = x//10
            
        if x == reverse_number or x == reverse_number//10:
            return True
        return False
        
#         x1 = x
#         x2 = 0
        
#         while x1:
#             x2 = x2*10 + x1%10
#             x1 = x1//10
            
#         if x2 == x:
#             return True
#         else:
#             return False
