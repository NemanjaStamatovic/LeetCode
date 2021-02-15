class Solution:
    def isNumber(self, s: str) -> bool:
        
        if s in ["inf", "-inf", "+inf", "Infinity", "-Infinity", "+Infinity"]:
            return False
        
        try:
            float(s)
        except:
            return False
        else:
            return True
        
