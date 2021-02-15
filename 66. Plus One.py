class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        s = ""
        for digit in digits:
            s += str(digit)
        s = int(s)
        s += 1
        result = []
        while s:
            result.append(s % 10)
            s = s // 10
        return result[::-1]    