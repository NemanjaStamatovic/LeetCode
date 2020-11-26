class Solution:
    def intToRoman(self, num: int) -> str:
        
        value = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        symbol = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        
        result = ""
        
        for i, v in enumerate(value):
            result += num//v * symbol[i]
            num %= v
            
        return result    