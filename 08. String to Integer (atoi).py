class Solution:
    def myAtoi(self, s: str) -> int:   
        s = s.lstrip()
        if s == "":
            return 0
        
        sign = 1
        result = "" 
        start = 0
        
        if s[0] in ["+", "-"] and len(s) > 1:
            if s[0] == "-":
                sign = -1
            start = 1
             
        for i in range(start, len(s)):
            if s[i].isdigit():
                result += s[i]
            else:
                break
        
        if result == "":
            return 0
        
        result = int(result) * sign    
        
        if result > 2**31 - 1:
            return 2**31 - 1
        if result < -2**31:
            return -2**31
        
        return result         