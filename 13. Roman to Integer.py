class Solution:
    def romanToInt(self, s: str) -> int:
        
        symbol = ["M", "D", "C", "L", "X", "V", "I"]
        value = [1000, 500, 100, 50, 10, 5, 1]
        symbol_value = {"M":1000, "D":500, "C":100, "L":50, "X":10, "V":5, "I":1}
        
        res = []
        
        for i in s:
            res.append(symbol_value[i])
            
        result = 0
        i = 0
        
        if len(res) == 1:
            return res[0]
        
        while True:
            if res[i] >= res[i+1]:
                result += res[i]
                i += 1
                
            else:
                result += res[i+1] - res[i]
                i += 2
                
            if i >= len(res)-1:
                break
        
        if res[-2] >= res[-1]:
            result += res[-1]
        return result        