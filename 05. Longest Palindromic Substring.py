class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ""
        
        for i in range(len(s)):
            #odd case
            current = self.expand_inner_outer(s, i, i)
            if len(current) > len(result):
                result = current
                
            #even case
            current = self.expand_inner_outer(s, i, i+1)
            if len(current) > len(result):
                result = current
                
        return result        
    
    def expand_inner_outer(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
            
        return s[left+1:right]    